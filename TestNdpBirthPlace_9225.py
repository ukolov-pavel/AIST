# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from locators import donors_registry_locators as locators
from base import BaseTest, Driver
from additional_functions import get_data
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-9225')
class TestNdpBirthPlace(BaseTest):

	@allure.step('Валидация поля Место рождения при добавлении донора')
	@pytest.mark.parametrize('birth_place, expected_result, test_data_set_number', get_data('data_test_ndp_birth_place.csv'))
	def test_ndp_birth_place(self, birth_place, expected_result, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.open()

		main_page.newdonor_click()

		main_page.ndp_filling_first_page("Сидоров", "Кирилл", '', "01.06.1980", "8910", "650231")
		
		main_page.select_gender('male')

		main_page.ndp_filling_birth_place(birth_place)

		assert aistium.get_value(locators_list=locators, element_name='ndp_birth_place') == expected_result

		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()

		main_page.if_donor_is_in_local_cabinet()

		main_page.ndp_second_page_loaded()

if __name__ == "__main__":
	pytest.main()