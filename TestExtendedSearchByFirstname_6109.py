# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import sql_query, get_data
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6109')
class TestExtendedSearchByFirstname(BaseTest):

	@allure.step('1. МД. Поиск донора по Имени (расширенный поиск в регистратуре донорского отделения)')
	@pytest.mark.parametrize('firstname, expected_result, test_data_set_number', get_data('data_test_extended_search_by_firstname_a.csv'))
	def test_extended_search_by_firstname_a(self, firstname, expected_result, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()

		main_page.extended_search_click('open')

		main_page.filling_fio_in_extended_search('', firstname, '')

		assert main_page.get_firstname_from_extended_search() == expected_result

	@allure.step('2. МД. Поиск донора по Имени (расширенный поиск в регистратуре донорского отделения)')
	@pytest.mark.parametrize('query, test_data_set_number', get_data('data_test_extended_search_by_firstname_b.csv'))
	def test_extended_search_by_firstname_b(self, query, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		full_query = sql_query(query)

		donorid = str(full_query[0][0])

		firstname = full_query[0][1]

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC where PerC.IsDeleted != 1 and PerC.FirstName like '%"+firstname+"%') Main where Main.UniqueId = '"+donorid+"'")[0][0]

		main_page.clear_localstorage()

		main_page.open()

		main_page.extended_search_click('open')

		main_page.filling_fio_in_extended_search('', firstname, '')

		aistium.click_on(elements=main_page.extended_search_button)

		main_page.loading_is_completed()

		assert main_page.ndp_get_grid_values('№', ind) == donorid

		assert main_page.number_of_entities_at_grid_including_hidden() == sql_query("select count ( * ) Q from PersonCards PerC where PerC.IsDeleted != 1 and PerC.FirstName like '%"+firstname+"%'")[0][0]

if __name__ == "__main__":
	pytest.main()