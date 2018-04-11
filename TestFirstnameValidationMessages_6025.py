# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import get_data
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6025')
class TestFirstnameValidationMessage(BaseTest):

	@allure.step('Проверка валидационных сообщений поля "Фамилия"')
	@pytest.mark.parametrize('firstname, expected_result, test_data_set_number', get_data('data_test_firstname_validation_message.csv'))
	def test_firstname_validation_message(self, firstname, expected_result, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.open()

		main_page.newdonor_click()

		main_page.ndp_filling_first_page("Сидоров", firstname, "", "01.06.1980", "8910", "650231")
		
		main_page.select_gender('male')

		aistium.click_on(elements=main_page.next_step_ndp)

		assert main_page.get_validation_message_text() == expected_result

if __name__ == "__main__":
	pytest.main()