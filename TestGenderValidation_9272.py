# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest
from base import Driver
from additional_functions import get_data
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-9272')
class TestGenderValidation(BaseTest):

	@allure.step('Валидация выбранного пола')
	@pytest.mark.parametrize('middlename, gender, expected_result, test_data_set_number', get_data('data_test_gender_validation.csv'))
	def test_gender_validation(self, middlename, gender, expected_result, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.open()

		main_page.newdonor_click()

		main_page.ndp_filling_first_page("Сидоров", "Кирилл", middlename, "01.06.1980", "8910", "650231")
		
		main_page.select_gender(gender)

		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()

		main_page.if_donor_is_in_local_cabinet()

		assert main_page.check_saved_gender(expected_result) == expected_result

if __name__ == "__main__":
	pytest.main()