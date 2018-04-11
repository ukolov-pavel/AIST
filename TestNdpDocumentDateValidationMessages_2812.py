# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import get_data
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-2812')
class TestNdpDocumentDateValidationMessages(BaseTest):

	@allure.step('Проверка валидационных сообщений для поля даты выдачи документа, удостоверяющего личность')
	@pytest.mark.parametrize('date_issue, issued_by, expected_result, test_data_set_number', get_data('data_test_ndp_document_date_validation_messages.csv'))
	def test_ndp_document_date_validation_messages(self, date_issue, issued_by, expected_result, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()

		main_page.newdonor_click()

		main_page.ndp_filling_first_page("Сидоров", "Кирилл", "", "01.06.1980", "8910", "650231")

		main_page.select_gender('male')

		aistium.fill(issued_by, elements=main_page.identity_document_issued_by)

		main_page.filling_identity_document_issue_date(date_issue)

		main_page.identity_document_issued_date_focusout()

		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()

		assert main_page.get_validation_message_text() == expected_result

if __name__ == "__main__":
	pytest.main()