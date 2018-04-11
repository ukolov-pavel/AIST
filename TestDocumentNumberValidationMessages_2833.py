# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import get_data
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-2833')
class TestDocumentNumberValidationMessages(BaseTest):

	@allure.step('Валидационные сообщения поля "Номер" документа при создании донора')
	@pytest.mark.parametrize('document_type, document_serie, document_number, expected_result, test_data_set_number', get_data('data_test_document_number_validation_messages.csv'))
	def test_document_number_validation_messages(self, document_type, document_serie, document_number, expected_result, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.open()

		main_page.newdonor_click()

		main_page.ndp_select_document_type(document_type)

		main_page.ndp_filling_first_page("Сидоров", "Кирилл", '', "01.06.1980", document_serie, document_number)
		
		main_page.select_gender('male')

		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()

		assert main_page.get_validation_message_text() == expected_result

if __name__ == "__main__":
	pytest.main()