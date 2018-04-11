# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import sql_query, get_data
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6117')
class TestExtendedSearchByDonorNumber(BaseTest):

	@allure.step('1. МД. Поиск донора по Поиск донора по № в регистратуре (расширенный поиск в регистратуре донорского отделения)')
	@pytest.mark.parametrize('number, expected_result, test_data_set_number', get_data('data_test_extended_search_by_donor_number_a.tsv', expansion='tsv'))
	def test_extended_search_by_donor_number_a(self, number, expected_result, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()

		main_page.extended_search_click('open')

		aistium.fill(number, elements=main_page.extended_registry_number)

		assert main_page.get_donorid_from_extended_search() == expected_result

	@allure.step('2. МД. Поиск донора по Поиск донора по № в регистратуре(расширенный поиск в регистратуре донорского отделения)')
	@pytest.mark.parametrize('query, test_data_set_number', get_data('data_test_extended_search_by_donor_number_b.csv'))
	def test_extended_search_by_donor_number_b(self, query, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		full_query = sql_query(query)

		number = str(full_query[0][0])

		main_page.clear_localstorage()

		main_page.open()

		main_page.extended_search_click('open')

		aistium.fill(number, elements=main_page.extended_registry_number)

		aistium.click_on(elements=main_page.extended_search_button)

		main_page.loading_is_completed()

		assert main_page.get_grid_values('UniqueId', 1, main_page.main_grid) == number

		assert main_page.number_of_entities_at_grid_including_hidden() == 1

if __name__ == "__main__":
	pytest.main()