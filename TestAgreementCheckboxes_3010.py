# -*- coding: utf-8 -*-
import pytest, allure, aistium, selenium
from base import BaseTest, Driver
from additional_functions import get_data
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-3010')
class TestAgreeCheckboxes(BaseTest):

	@allure.step('1. Проверка установленного по умолчанию значения "Получено согласие на обработку данных"')
	@pytest.mark.parametrize('expected_result, test_data_set_number', get_data('data_test_is_agree_persional_data_processing_default_value.csv'))
	def test_is_agree_persional_data_processing_default_value(self, expected_result, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.open()

		main_page.newdonor_click()

		main_page.ndp_filling_first_page("Сидоров", "Кирилл", "", "01.06.1980", "8910", "650231")
		
		main_page.select_gender('male')

		main_page.check_is_agree_persional_data_processing(expected_result)

	@allure.step('2. Проверка установленного по умолчанию значения "Получено согласие на e-mail и смс рассылку"')
	@pytest.mark.parametrize('expected_result, test_data_set_number', get_data('data_test_is_message_agree_default_value.csv'))
	def test_is_message_agree_default_value(self, expected_result, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.open()

		main_page.newdonor_click()

		main_page.ndp_filling_first_page("Сидоров", "Кирилл", "", "01.06.1980", "8910", "650231")
		
		main_page.select_gender('male')

		main_page.check_is_message_agree(expected_result)

	@allure.step('3. Проверка работы флагов и перехода на вторую страницу поп-апа при различных комбинациях"')
	@pytest.mark.parametrize('is_agree_persional_data_processing, is_message_agree, expected_result1, expected_result2, test_data_set_number', get_data('data_test_agreement_checkboxes.csv'))
	def test_agree_checkboxes(self, is_agree_persional_data_processing, is_message_agree, expected_result1, expected_result2, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.open()

		main_page.newdonor_click()

		main_page.ndp_filling_first_page("Сидоров", "Кирилл", "", "01.06.1980", "8910", "650231")
		
		main_page.select_gender('male')

		if is_agree_persional_data_processing == 'false':
			aistium.click_on(elements=main_page.is_agree_persional_data_processing)

		if is_message_agree == 'false':
			aistium.click_on(elements=main_page.is_message_agree)

		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()

		main_page.ndp_second_page_loaded()

		main_page.check_is_agree_persional_data_processing(expected_result1)

		main_page.check_is_message_agree(expected_result2)

if __name__ == "__main__":
	pytest.main()