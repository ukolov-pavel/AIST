# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from locators import donors_registry_locators as locators
from base import BaseTest, Driver
from additional_functions import get_data
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6066')
class TestTransferFromSearchToNdp(BaseTest):

	@allure.step('1. Заполнение быстрого поиска, проверка передачи значения быстрого поиска в соответствующие поля в поп-апе добавления нового донора')
	@pytest.mark.parametrize('search_line, expected_result1, expected_result2, expected_result3, test_data_set_number', get_data('data_test_transfer_from_quick_search_to_ndp.csv'))
	def test_transfer_from_quick_search_to_ndpr(self, search_line, expected_result1, expected_result2, expected_result3, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.open()

		aistium.fill(search_line, elements=main_page.quick_search_field)

		main_page.newdonor_click()

		assert aistium.get_value(locators_list=locators, element_name='last_name_field_ndp') == expected_result1

		assert aistium.get_value(locators_list=locators, element_name='first_name_field_ndp') == expected_result2

		assert aistium.get_value(locators_list=locators, element_name='middle_name_field_ndp') == expected_result3

	@allure.step('2. Заполнение расширенного поиска, проверка передачи значения расширенного поиска в соответствующие поля в поп-апе добавления нового донора')
	@pytest.mark.parametrize('lastname, firstname, middlename, expected_result1, expected_result2, expected_result3, test_data_set_number', get_data('data_test_transfer_from_extended_search_to_ndp.csv'))
	def test_transfer_from_extended_search_to_ndp(self, lastname, firstname, middlename, expected_result1, expected_result2, expected_result3, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.open()

		main_page.extended_search_click('open')

		main_page.filling_fio_in_extended_search(lastname, firstname, middlename)

		main_page.extended_search_click('close')

		main_page.newdonor_click()

		assert aistium.get_value(locators_list=locators, element_name='last_name_field_ndp') == expected_result1

		assert aistium.get_value(locators_list=locators, element_name='first_name_field_ndp') == expected_result2

		assert aistium.get_value(locators_list=locators, element_name='middle_name_field_ndp') == expected_result3

	@allure.step('3. Заполнение быстрого и расширенного поиска, проверка передачи значения быстрого поиска в соответствующие поля в поп-апе добавления нового донора')
	@pytest.mark.parametrize('search_line, lastname, firstname, middlename, expected_result1, expected_result2, expected_result3, test_data_set_number', get_data('data_test_transfer_from_search_fields_to_ndp.csv'))
	def test_transfer_from_search_fields_to_ndp(self, search_line, lastname, firstname, middlename, expected_result1, expected_result2, expected_result3, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.open()

		aistium.fill(search_line, elements=main_page.quick_search_field)

		main_page.extended_search_click('open')

		main_page.filling_fio_in_extended_search(lastname, firstname, middlename)

		main_page.extended_search_click('close')

		main_page.newdonor_click()

		assert aistium.get_value(locators_list=locators, element_name='last_name_field_ndp') == expected_result1

		assert aistium.get_value(locators_list=locators, element_name='first_name_field_ndp') == expected_result2

		assert aistium.get_value(locators_list=locators, element_name='middle_name_field_ndp') == expected_result3

if __name__ == "__main__":
	pytest.main()