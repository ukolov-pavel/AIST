# -*- coding: utf-8 -*-
import pytest, allure, aistium, selenium
from locators import donors_registry_locators as locators
from base import BaseTest, Driver
from additional_functions import get_data, sql_query
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6004')
class TestDeferralIncorrectInput(BaseTest):

	@allure.step('5. Проверка на ввод некорректных значений в поле "Отвод" и сохранение донора')
	@pytest.mark.parametrize('incorrect_value, test_data_set_number', get_data('data_test_deferral_incorrect_input.csv'))
	def test_deferral_incorrect_input(self, incorrect_value, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()
		
		main_page.newdonor_click()

		main_page.ndp_filling_first_page('Сидоров', "Алексей", "", "05.06.1980", "8914", "650235")
		
		main_page.select_gender('male')

		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()

		main_page.if_donor_is_in_local_cabinet()

		main_page.ndp_second_page_loaded()

		main_page.ndp_filling_region('Москва г')

		main_page.ndp_filling_street('Перовская ул')

		aistium.fill('1', elements=main_page.reg_fias_address_house)

		main_page.ndp_filling_deferral(incorrect_value, 'incorrect_input')

		main_page.is_deferral_listbox_empty()

		main_page.ndp_deferrals_press_enter()

		assert aistium.get_value(locators_list=locators, element_name='ndp_deferral_field') == ''

		main_page.ndp_save_new_donor('success')

		assert aistium.get_text(elements=main_page.fio_minicard) == 'Сидоров Алексей'

if __name__ == "__main__":
	pytest.main()