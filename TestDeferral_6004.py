# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import get_data, sql_query
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6004')
class TestDeferral(BaseTest):

	@allure.step('1. Список актуальных отводов: проверка соответствия выпадающего списка отводов на форме и списка записей, возвращаемых по запросу в БД; проверка на корректное сохранение отвода')
	@pytest.mark.parametrize('deferral_system_name, expected_result, test_data_set_number', get_data('data_test_deferral.csv'))
	def test_deferral(self, deferral_system_name, expected_result, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()

		deferrals_gui = []
		
		deferrals_db = []

		main_page.newdonor_click()

		main_page.ndp_filling_first_page('Сидоров', "Алексей", "", "05.06.1980", "8914", "650235")
		
		main_page.select_gender('male')

		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()

		main_page.if_donor_is_in_local_cabinet()

		main_page.ndp_filling_region('Москва г')

		main_page.ndp_filling_street('Перовская ул')

		aistium.fill('8', elements=main_page.reg_fias_address_house)

		assert main_page.is_deferral_type_field_disabled() == ('true', 'true')

		active_deferrals = sql_query("select DefT.Code+' '+DefT.Name Otvod from ref.DeferralTypes DefT join ref.DeferralTypeParams DefTP on DefT.UniqueId = DefTP.DeferralTypeId where DefTP.IsActive = 1 order by DefT.Code asc")

		for defer in main_page.ndp_deferrals_listbox():
			deferrals_gui.append(self.driver.execute_script("return jQuery(arguments[0]).text();", defer))

		for deferral in active_deferrals:
			deferrals_db.append(deferral[0])

		assert deferrals_gui == deferrals_db

		main_page.ndp_filling_deferral(deferral_system_name)

		main_page.ndp_save_new_donor('success')

		assert expected_result.upper() in aistium.get_text(elements=main_page.deferral_from_minicard).upper()

		assert aistium.get_text(elements=main_page.fio_minicard) == 'Сидоров Алексей'

if __name__ == "__main__":
	pytest.main()