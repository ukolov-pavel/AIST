# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from locators import donors_registry_locators as locators
from base import BaseTest, Driver
from additional_functions import sql_query
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6094')
class TestOpeningRegistryPage(BaseTest):

	@allure.step('1. Открытие страницы Регистратура донорского отделения. Сохранение фильтров быстрого поиска Регистратуры донорского отделения после повторного посещения страницы')
	def test_donors_registry_simple_search_filters(self):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()

		assert main_page.get_title() == 'Регистратура донорского отделения'

		aistium.fill(sql_query("select top (1) PerC.LastName + ' ' + PerC.FirstName from PersonCards PerC where PerC.Gender = '1' and PerC.LastName not like '%[a-zA-Z0-9]%' and PerC.FirstName not like '%[a-zA-Z0-9]%'")[0][0], elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		quantity = main_page.number_of_entities_at_grid()

		main_page.open()

		main_page.loading_is_completed()

		assert aistium.get_value(locators_list=locators, element_name='quick_search_field') == sql_query("select top (1) PerC.LastName + ' ' + PerC.FirstName from PersonCards PerC where PerC.Gender = '1' and PerC.LastName not like '%[a-zA-Z0-9]%' and PerC.FirstName not like '%[a-zA-Z0-9]%'")[0][0]

		assert quantity == main_page.number_of_entities_at_grid()

	@allure.step('2. Сохранение фильтров расширенного поиска Регистратуры донорского отделения после повторного посещения страницы')
	def test_donors_registry_extended_search_filters(self):

		full_name = sql_query("select top (1) PerC.LastName, PerC.FirstName from PersonCards PerC where PerC.Gender = '2' and PerC.LastName not like '%[a-zA-Z0-9]%' and PerC.FirstName not like '%[a-zA-Z0-9]%'")

		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()

		main_page.extended_search_click('open')

		main_page.filling_fio_in_extended_search(full_name[0][0], full_name[0][1])

		aistium.click_on(elements=main_page.extended_search_button)

		main_page.loading_is_completed()

		quantity = main_page.number_of_entities_at_grid()

		main_page.open()

		main_page.loading_is_completed()

		assert main_page.get_lastname_from_extended_search() == full_name[0][0]

		assert main_page.get_firstname_from_extended_search() == full_name[0][1]

		assert quantity == main_page.number_of_entities_at_grid()

	@allure.step('3. Очищение фильтров поиска Регистратуры донорского отделения при открытии страницы из меню')
	def test_donors_registry_clear_filters_by_menu(self):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()

		aistium.fill(sql_query("select top (1) PerC.LastName + ' ' + PerC.FirstName from PersonCards PerC where PerC.Gender = '1' and PerC.LastName not like '%[a-zA-Z0-9]%' and PerC.FirstName not like '%[a-zA-Z0-9]%'")[0][0], elements=main_page.quick_search_field)

		main_page.quick_search('press')

		main_page.loading_is_completed()

		main_page.hover_top_menu('1', 0)

		assert aistium.get_value(locators_list=locators, element_name='quick_search_field') == ''

		assert main_page.number_of_entities_at_grid() == 0

if __name__ == "__main__":
	pytest.main()