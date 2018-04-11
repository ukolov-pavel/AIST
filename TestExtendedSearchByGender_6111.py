# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import sql_query, get_data
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6111')
class TestExtendedSearchByGender(BaseTest):

	@allure.step('1. МД. Поиск донора по Полу (расширенный поиск в регистратуре донорского отделения)')
	def test_extended_search_by_gender_a(self):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()

		main_page.extended_search_click('open')

		assert main_page.get_genders_listbox_from_extended_search() == ['Пол','Женский','Мужской']

	@allure.step('2. МД. Поиск донора по Полу (расширенный поиск в регистратуре донорского отделения)')
	def test_extended_search_by_gender_b(self):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()

		main_page.extended_search_click('open')

		main_page.filling_gender_in_extended_search('Женский')

		main_page.filling_gender_in_extended_search('Пол')

		assert main_page.is_extended_search_button_disable() == 'true'
		
	@allure.step('3. МД. Поиск донора по Полу (расширенный поиск в регистратуре донорского отделения)')
	@pytest.mark.parametrize('gender, query, test_data_set_number', get_data('data_test_extended_search_by_gender_c.csv'))
	def test_extended_search_by_gender_c(self, gender, query, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		donorid = str(sql_query(query)[0][0])

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC where PerC.IsDeleted != 1 and PerC.Gender = case when '"+gender+"' = 'Мужской' then '1' else '2' end) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		main_page.clear_localstorage()

		main_page.open()

		main_page.extended_search_click('open')

		main_page.filling_gender_in_extended_search(gender)

		aistium.click_on(elements=main_page.extended_search_button)

		main_page.loading_is_completed()

		assert main_page.get_grid_values('UniqueId', ind, main_page.main_grid) == donorid

		assert main_page.number_of_entities_at_grid_including_hidden() == sql_query("select count ( * ) Q from PersonCards PerC where PerC.IsDeleted != 1 and PerC.Gender = case when '"+gender+"' = 'Мужской' then '1' else '2' end")[0][0]

if __name__ == "__main__":
	pytest.main()