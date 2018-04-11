# -*- coding: utf-8 -*-
import pytest, allure, aistium, selenium
from locators import donors_registry_locators as locators
from base import BaseTest, Driver
from additional_functions import get_data, sql_query
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6004')
class TestDeferralClearButton(BaseTest):

	@allure.step('3. Проверка кнопки "Очистить" для отводов')
	def test_deferral_clear_button(self):
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

		main_page.ndp_filling_deferral(str(sql_query("select top(1) DefT.Code+' '+DefT.Name Otvod from ref.DeferralTypes DefT join ref.DeferralTypeParams DefTP on DefT.UniqueId = DefTP.DeferralTypeId where DefTP.IsActive = 1 and DefT.BaseType = 1"))[3:-5])

		aistium.click_on(elements=main_page.ndp_deferral_clear_button)

		assert aistium.get_value(locators_list=locators, element_name='ndp_deferral_type') == ''

		assert aistium.get_value(locators_list=locators, element_name='ndp_deferral_field') == ''

		main_page.ndp_save_new_donor('success')

		main_page.mc_donor_has_not_deferral()

		assert aistium.get_text(elements=main_page.fio_minicard) == 'Сидоров Алексей'

if __name__ == "__main__":
	pytest.main()