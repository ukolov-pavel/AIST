# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from locators import donors_registry_locators as locators
from base import BaseTest, Driver
from additional_functions import get_data
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-2849')
class TestGenderAndMiddlename(BaseTest):

	@allure.step('1. Проверка предупреждающего сообщения о несоответствии пола отчеству, проверка текста сообщения, "Продолжить?" - да, проверка правильности сохранения пола')
	@pytest.mark.parametrize('middlename, test_data_set_number', get_data('data_test_gender_and_middlename_confirm_yes.csv'))
	def test_gender_and_middlename_confirm_yes(self, middlename, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()

		main_page.newdonor_click()

		main_page.ndp_filling_first_page('Машинный', 'Проверкаполаиотчества', middlename, '10.12.1977', '2013', '312313')

		if middlename[-2:] == 'ич' or middlename[-4:] == 'оглы':
			main_page.select_gender('female')
			aistium.click_on(elements=main_page.next_step_ndp)
			assert aistium.get_text(locators_list=locators, element_name='confirm_popup') == 'Пол донора не соответствует отчеству. Продолжить?'
			aistium.click_on(locators_list=locators, element_name='confirm_popup_yes_btn')
			aistium.click_on(elements=main_page.next_step_ndp) #https://aj.srvdev.ru/browse/AIST-15978
			saved_gender = 'Ж'
		elif middlename[-2:] == 'на' or middlename[-4:] == 'кызы':
			main_page.select_gender('male')
			aistium.click_on(elements=main_page.next_step_ndp)
			assert aistium.get_text(locators_list=locators, element_name='confirm_popup') == 'Пол донора не соответствует отчеству. Продолжить?'
			aistium.click_on(locators_list=locators, element_name='confirm_popup_yes_btn')
			aistium.click_on(elements=main_page.next_step_ndp) #https://aj.srvdev.ru/browse/AIST-15978
			saved_gender = 'М'

		main_page.if_donor_is_in_local_cabinet()

		main_page.ndp_second_page_loaded()

		main_page.ndp_filling_region('Москва г')

		main_page.ndp_filling_street('Строителей ул')

		aistium.fill('13', elements=main_page.reg_fias_address_house)
		
		main_page.ndp_save_new_donor('success')

		assert main_page.get_gender_from_minicard() == saved_gender

	@allure.step('2. Проверка предупреждающего сообщения о несоответствии пола отчеству, проверка текста сообщения, "Продолжить?" - нет, проверка правильности сохранения пола')
	@pytest.mark.parametrize('middlename, test_data_set_number', get_data('data_test_gender_and_middlename_confirm_no.csv'))
	def test_gender_and_middlename_confirm_no(self, middlename, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()

		main_page.newdonor_click()

		main_page.ndp_filling_first_page('Машинный', 'Проверкаполаиотества', middlename, '10.12.1977', '2013', '312313')

		if middlename[-2:] == 'ич':
			main_page.select_gender('female')
			aistium.click_on(elements=main_page.next_step_ndp)
			assert aistium.get_text(locators_list=locators, element_name='confirm_popup') == 'Пол донора не соответствует отчеству. Продолжить?'
			aistium.click_on(locators_list=locators, element_name='confirm_popup_no_btn')
			aistium.click_on(elements=main_page.next_step_ndp)
			saved_gender = 'М' #Сохраняется для проверки в конце
		elif middlename[-2:] == 'на':
			main_page.select_gender('male')
			aistium.click_on(elements=main_page.next_step_ndp)
			assert aistium.get_text(locators_list=locators, element_name='confirm_popup') == 'Пол донора не соответствует отчеству. Продолжить?'
			aistium.click_on(locators_list=locators, element_name='confirm_popup_no_btn')
			aistium.click_on(elements=main_page.next_step_ndp)
			saved_gender = 'Ж'

		main_page.if_donor_is_in_local_cabinet()

		main_page.ndp_filling_region('Москва г')

		main_page.ndp_filling_street('Строителей ул')

		aistium.fill('13', elements=main_page.reg_fias_address_house)
		
		main_page.ndp_save_new_donor('success')

		assert main_page.get_gender_from_minicard() == saved_gender

if __name__ == "__main__":
	pytest.main()