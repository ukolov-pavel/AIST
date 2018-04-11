# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from locators import donors_registry_locators as locators
from base import BaseTest, Driver
from additional_functions import get_data
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-2830')
class TestDocumentNumberValidation(BaseTest):

	@allure.step('Проверка поля "Номер" документа при создании донора')
	@pytest.mark.parametrize('document_type, document_serie, document_number, expected_result, test_data_set_number', get_data('data_test_document_number_validation.tsv', expansion='tsv'))
	def test_document_number_validation(self, document_type, document_serie, document_number, expected_result, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.open()

		main_page.newdonor_click()

		main_page.ndp_select_document_type(document_type)

		main_page.ndp_filling_first_page("Сидоров", "Кирилл", '', "01.06.1980", document_serie, document_number)
		
		main_page.select_gender('male')

		assert aistium.get_value(locators_list=locators, element_name='document_number_field_ndp') == expected_result

		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()

		main_page.if_donor_is_in_local_cabinet()

		main_page.ndp_second_page_loaded()

if __name__ == "__main__":
	pytest.main()