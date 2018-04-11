# -*- coding: utf-8 -*-
import pytest, allure, aistium, selenium
from base import BaseTest, Driver
from additional_functions import get_data, date_calculation
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-2927')
class TestBirthDateValidationMessages(BaseTest):

	@allure.step('Валидация поля Дата рождения (запрещающие сообщения) при добавлении донора')
	@pytest.mark.parametrize('birthdate, expected_result, test_data_set_number', get_data('data_test_birthdate_validation_messages.csv'))
	def test_birthdate_validation_messages(self, birthdate, expected_result, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.open()

		main_page.newdonor_click()
		
		main_page.ndp_filling_first_page("Сидоров", "Кирилл", '', birthdate, "8910", "650231")

		main_page.select_gender('male')

		aistium.click_on(elements=main_page.next_step_ndp)

		if expected_result == 'Дата рождения ограничена настройками системы: от ':

			assert main_page.get_validation_message_text() == expected_result + date_calculation('today - sys_max_age') + '.'

		else:

			main_page.get_validation_message_text() == expected_result

if __name__ == "__main__":
	pytest.main()