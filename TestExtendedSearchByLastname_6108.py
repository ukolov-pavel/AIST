# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import sql_query, get_data
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6108')
class TestExtendedSearchByLastname(BaseTest):

	@allure.step('1. МД. Регистратура. Валидация поля "Фамилия" в расширенном поиске.')
	@pytest.mark.parametrize('lastname, expected_result, test_data_set_number', get_data('data_test_extended_search_by_lastname_a.csv'))
	def test_extended_search_by_lastname_a(self, lastname, expected_result, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()

		main_page.extended_search_click('open')

		main_page.filling_fio_in_extended_search(lastname, '', '')

		assert main_page.get_lastname_from_extended_search() == expected_result

	@allure.step('2. МД. Регистратура. Валидация поля "Фамилия" в расширенном поиске.')
	@pytest.mark.parametrize('query, test_data_set_number', get_data('data_test_extended_search_by_lastname_b.csv'))
	def test_extended_search_by_lastname_b(self, query, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		full_query = sql_query(query)

		donorid = str(full_query[0][0])

		lastname = full_query[0][1]

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC where PerC.IsDeleted != 1 and PerC.LastName like '%"+lastname+"%') Main where Main.UniqueId = '"+donorid+"'")[0][0]

		main_page.clear_localstorage()

		main_page.open()

		main_page.extended_search_click('open')

		main_page.filling_fio_in_extended_search(lastname, '', '')

		aistium.click_on(elements=main_page.extended_search_button)

		main_page.loading_is_completed()

		assert main_page.get_grid_values('UniqueId', ind, main_page.main_grid) == donorid

		assert main_page.number_of_entities_at_grid_including_hidden() == sql_query("select count ( * ) Q from PersonCards PerC where PerC.IsDeleted != 1 and PerC.LastName like '%"+lastname+"%'")[0][0]

if __name__ == "__main__":
	pytest.main()