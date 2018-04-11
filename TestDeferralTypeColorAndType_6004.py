# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from locators import donors_registry_locators as locators
from base import BaseTest, Driver
from additional_functions import get_data, sql_query, convert_to_hex
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6004')
class TestDeferralTypeColorAndType(BaseTest):

	@allure.step('2. Проверка на цвета и значения типов отводов')
	@pytest.mark.parametrize('expected_color, expected_type, test_data_set_number', get_data('data_test_deferral_type_color_and_type.csv'))
	def test_deferral_type_color_and_type(self, expected_color, expected_type, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.open()

		main_page.newdonor_click()

		main_page.ndp_filling_first_page('Сидоров', "Алексей", "", "05.06.1980", "8914", "650235")
		
		main_page.select_gender('male')

		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()

		main_page.if_donor_is_in_local_cabinet()

		main_page.ndp_second_page_loaded()

		if expected_type == 'Временный':
			main_page.ndp_filling_deferral(str(sql_query("select top(1) DefT.Code+' '+DefT.Name Otvod from ref.DeferralTypes DefT join ref.DeferralTypeParams DefTP on DefT.UniqueId = DefTP.DeferralTypeId where DefTP.IsActive = 1 and DefT.BaseType = 3"))[3:-5])
			assert aistium.get_value(locators_list=locators, element_name='ndp_deferral_type') == expected_type
			assert convert_to_hex(main_page.ndp_get_deferral_type_color()) == expected_color
		elif expected_type == 'Контроль':
			main_page.ndp_filling_deferral(str(sql_query("select top(1) DefT.Code+' '+DefT.Name Otvod from ref.DeferralTypes DefT join ref.DeferralTypeParams DefTP on DefT.UniqueId = DefTP.DeferralTypeId where DefTP.IsActive = 1 and DefT.BaseType = 2"))[3:-5])
			assert aistium.get_value(locators_list=locators, element_name='ndp_deferral_type') == expected_type
			assert convert_to_hex(main_page.ndp_get_deferral_type_color()) == expected_color
		elif expected_type == 'Абсолютный':
			main_page.ndp_filling_deferral(str(sql_query("select top(1) DefT.Code+' '+DefT.Name Otvod from ref.DeferralTypes DefT join ref.DeferralTypeParams DefTP on DefT.UniqueId = DefTP.DeferralTypeId where DefTP.IsActive = 1 and DefT.BaseType = 1"))[3:-5])
			assert aistium.get_value(locators_list=locators, element_name='ndp_deferral_type') == expected_type
			assert convert_to_hex(main_page.ndp_get_deferral_type_color()) == expected_color

if __name__ == "__main__":
	pytest.main()