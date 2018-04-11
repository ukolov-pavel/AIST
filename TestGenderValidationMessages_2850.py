# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import get_data
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-2850')
class TestGenderValidationMessages(BaseTest):

	@allure.step('Валидация поля Пол (запрещающие сообщения) при добавлении донора')
	@pytest.mark.parametrize('middlename, expected_result, test_data_set_number', get_data('data_test_gender_validation_messages.csv'))
	def test_gender_validation_messages(self, middlename, expected_result, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.open()

		main_page.newdonor_click()

		main_page.ndp_filling_first_page("Сидоров", "Кирилл", middlename, "01.06.1980", "8910", "650231")

		aistium.click_on(elements=main_page.next_step_ndp)

		assert main_page.get_validation_message_text() == expected_result

if __name__ == "__main__":
	pytest.main()