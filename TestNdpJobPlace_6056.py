# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import get_data, sql_query
from donors_registry import DonorsModuleRegistryPage
from donors_card_title import DonorsCardTitle

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6056')
class TestNdpJobPlaceEnterValue(BaseTest):

	@allure.step('4. Ввод в Место работы/учёбы различных символов валидных типов')
	@pytest.mark.parametrize('job_place, expected_result, test_data_set_number', get_data('data_test_ndp_job_place.csv'))
	def test_ndp_job_place(self, job_place, expected_result, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()

		main_page.newdonor_click()

		main_page.ndp_filling_first_page('Сидоров', "Анатолий", "", "01.06.1980", "2910", "650231")

		main_page.select_gender('male')

		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()

		main_page.if_donor_is_in_local_cabinet()

		main_page.ndp_second_page_loaded()

		main_page.ndp_filling_region('Москва г')

		main_page.ndp_filling_street('Перовская ул')

		aistium.fill('4', elements=main_page.reg_fias_address_house)

		aistium.fill(job_place, elements=main_page.ndp_job_place_field)

		main_page.ndp_save_new_donor('success')

		main_page.loading_is_completed()

		grid_donor_id = main_page.ndp_get_grid_values('№', 'active_cell')

		donors_card_title_page = DonorsCardTitle(grid_donor_id)

		donors_card_title_page.open()

		assert donors_card_title_page.job_place() == expected_result

if __name__ == "__main__":
	pytest.main()