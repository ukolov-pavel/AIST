# -*- coding: utf-8 -*-
import pytest
import allure
import selenium
import aistium
from locators import donors_registry_locators as locators
from base import BaseTest, Driver
from additional_functions import get_data
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-2926')
class TestBirthDateValidation(BaseTest):

	@allure.step('Валидация поля Дата рождения (предупреждающие сообщения) при добавлении донора, проверка текста предупреждающего сообщения, подверждение - нет')
	@pytest.mark.parametrize('birthdate, test_data_set_number', get_data('data_test_birthdate_validation_no.csv'))
	def test_birthdate_validation_confirm_no(self, birthdate, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.open()

		main_page.newdonor_click()
		
		main_page.ndp_filling_first_page("Сидоров", "Кирилл", '', birthdate, "8910", "650231")

		main_page.select_gender('male')

		aistium.click_on(elements=main_page.next_step_ndp)

		assert aistium.get_text(locators_list=locators, element_name='confirm_popup') == 'Возраст донора меньше рекомендуемого для сдачи донаций. Продолжить?'

		aistium.click_on(locators_list=locators, element_name='confirm_popup_no_btn')

		assert main_page.is_birthdate_field_focused() == True

	@allure.step('Валидация поля Дата рождения (предупреждающие сообщения) при добавлении донора, проверка текста предупреждающего сообщения, подверждение - да')
	@pytest.mark.parametrize('birthdate, test_data_set_number', get_data('data_test_birthdate_validation_yes.csv'))
	def test_birthdate_validation_confirm_yes(self, birthdate, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.open()

		main_page.newdonor_click()
		
		main_page.ndp_filling_first_page("Сидоров", "Кирилл", '', birthdate, "8910", "650231")

		main_page.select_gender('male')

		aistium.click_on(elements=main_page.next_step_ndp)

		assert aistium.get_text(locators_list=locators, element_name='confirm_popup') == 'Возраст донора меньше рекомендуемого для сдачи донаций. Продолжить?'

		aistium.click_on(locators_list=locators, element_name='confirm_popup_yes_btn')

		main_page.if_donor_is_in_local_cabinet()

		main_page.ndp_second_page_loaded()

if __name__ == "__main__":
	pytest.main()