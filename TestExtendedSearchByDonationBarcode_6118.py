# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import sql_query, get_data
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6118')
class TestExtendedSearchByDonationBarcode(BaseTest):

	@allure.step('1. МД. Поиск донора по Штрихкоду донации (расширенный поиск в регистратуре донорского отделения)')
	@pytest.mark.parametrize('barcode, expected_result, test_data_set_number', get_data('data_test_extended_search_by_donation_barcode_a.tsv', expansion='tsv'))
	def test_extended_search_by_donation_barcode_a(self, barcode, expected_result, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()

		main_page.extended_search_click('open')

		aistium.fill(barcode, elements=main_page.extended_donation_barcode)

		assert main_page.get_barcode_from_extended_search() == expected_result

	@allure.step('2. МД. Поиск донора по Штрихкоду донации (расширенный поиск в регистратуре донорского отделения)')
	@pytest.mark.parametrize('query, test_data_set_number', get_data('data_test_extended_search_by_donation_barcode_b.csv'))
	def test_extended_search_by_donation_barcode_b(self, query, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		full_query = sql_query(query)

		donorid = str(full_query[0][0])

		barcode = full_query[0][1]

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC join Donations Don on PerC.UniqueId = Don.DonorId where PerC.IsDeleted != 1 and Don.Barcode like '%' + replace('"+barcode+"', '=7', '') + '%' group by PerC.UniqueId, PerC.BirthDate) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		main_page.clear_localstorage()

		main_page.open()

		main_page.extended_search_click('open')

		aistium.fill(barcode, elements=main_page.extended_donation_barcode)

		aistium.click_on(elements=main_page.extended_search_button)

		main_page.loading_is_completed()

		assert main_page.get_grid_values('UniqueId', ind, main_page.main_grid) == donorid

		assert main_page.number_of_entities_at_grid_including_hidden() == sql_query("select count (distinct PerC.UniqueId) from PersonCards PerC join Donations Don on PerC.UniqueId = Don.DonorId where PerC.IsDeleted != 1 and Don.Barcode like '%' + replace('"+barcode+"', '=7', '') + '%'")[0][0]

if __name__ == "__main__":
	pytest.main()