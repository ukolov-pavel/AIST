# -*- coding: utf-8 -*-
import pytest
import allure
import selenium
import aistium
from base import BaseTest, Driver
from additional_functions import get_data
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6053')
class TestNdpMobPhoneMessage(BaseTest):

	@allure.step('Валидация поля Мобильный телефон (Контактная информация) (запрещающие сообщения) при добавлении донора')
	@pytest.mark.parametrize('mobphone, expected_result, test_data_set_number', get_data('data_test_ndp_mobphone_message.csv'))
	def test_ndp_mobphone_validation_message(self, mobphone, expected_result, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()

		main_page.newdonor_click()

		main_page.ndp_filling_first_page("Сидоров", "Кирилл", "", "01.06.1980", "8910", "650231")

		main_page.select_gender('male')

		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()

		main_page.if_donor_is_in_local_cabinet()

		main_page.ndp_second_page_loaded()

		main_page.ndp_filling_contacts(mobphone, "", "")

		main_page.ndp_filling_region('Москва г')

		main_page.ndp_filling_street('Перовская ул')

		main_page.ndp_filling_house('4')

		main_page.ndp_save_new_donor('check')

		main_page.loading_is_completed()

		assert main_page.get_validation_message_text() == expected_result

if __name__ == "__main__":
	pytest.main()