# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from locators import donors_registry_locators as locators
from base import BaseTest, Driver
from additional_functions import get_data
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-16534')
class TestCancellationOfAddition(BaseTest):

	@allure.step('1. Отмена добавления донора с первой страницы')
	@pytest.mark.parametrize('element, confirmation, test_data_set_number', get_data('data_test_from_first_page_cancellation.csv'))
	def test_from_first_page_cancellation(self, element, confirmation, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.open()

		main_page.newdonor_click()
		
		main_page.ndp_filling_first_page("Сидоров", "Кирилл", '', '01.06.1980', "8910", "650231")

		main_page.select_gender('male')

		if element == 'icon':

			aistium.click_on(elements=main_page.popup_close_icon)

		elif element == 'button':

			aistium.click_on(elements=main_page.ndp_first_page_cancel_newdonor)

		assert aistium.get_text(locators_list=locators, element_name='confirm_popup') == 'Вы точно хотите покинуть форму Добавление донора?'

		if confirmation == 'yes':

			aistium.click_on(locators_list=locators, element_name='confirm_popup_yes_btn')

			assert main_page.is_ndp_closed() == True

		elif confirmation == 'no':

			aistium.click_on(locators_list=locators, element_name='confirm_popup_no_btn')

			assert aistium.get_value(locators_list=locators, element_name='birthdate_field_ndp') == '01.06.1980'

			assert aistium.get_value(locators_list=locators, element_name='last_name_field_ndp') == "Сидоров"

			assert aistium.get_value(locators_list=locators, element_name='first_name_field_ndp') == "Кирилл"

			assert aistium.get_value(locators_list=locators, element_name='document_serie_field_ndp') == "8910"

			assert aistium.get_value(locators_list=locators, element_name='document_number_field_ndp') == "650231"


	@allure.step('2. Отмена добавления донора со второй страницы')
	@pytest.mark.parametrize('element, confirmation, test_data_set_number', get_data('data_test_from_second_page_cancellation.csv'))
	def test_from_second_page_cancellation(self, element, confirmation, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.open()

		main_page.newdonor_click()
		
		main_page.ndp_filling_first_page("Сидоров", "Кирилл", '', '01.06.1980', "8910", "650231")

		main_page.select_gender('male')

		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.if_donor_is_in_local_cabinet()

		main_page.ndp_second_page_loaded()

		main_page.ndp_filling_region('Москва г')

		main_page.ndp_filling_street('Перовская ул')

		aistium.fill('4', elements=main_page.reg_fias_address_house)

		if element == 'icon':

			aistium.click_on(elements=main_page.popup_close_icon)

		elif element == 'button':

			aistium.click_on(elements=main_page.ndp_second_page_cancel_newdonor)

		assert aistium.get_text(locators_list=locators, element_name='confirm_popup') == 'Вы точно хотите покинуть форму Добавление донора?'

		if confirmation == 'yes':

			aistium.click_on(locators_list=locators, element_name='confirm_popup_yes_btn')

			assert main_page.is_ndp_closed() == True

		elif confirmation == 'no':

			aistium.click_on(locators_list=locators, element_name='confirm_popup_no_btn')

			assert main_page.ndp_second_page_check_values_of_mandatory_fields() == ('Москва г', '', 'Перовская ул', '4')

if __name__ == "__main__":
	pytest.main()