# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import sql_query, get_data
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6101')
class TestSimpleSearchByFullname(BaseTest):

	@allure.step('Поиск донора по ФИО (быстрый поиск в регистратуре донорского отделения)')
	@pytest.mark.parametrize('query, test_data_set_number', get_data('data_test_simple_search_by_fullname.csv'))
	def test_simple(self, query, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		full_query = sql_query(query)

		donor_id, fullname = str(full_query[0][0]), full_query[0][1]

		main_page.clear_localstorage()

		main_page.open()

		aistium.fill(fullname, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		assert main_page.ndp_get_grid_values('№', 'active_cell') == donor_id

if __name__ == "__main__":
	pytest.main()