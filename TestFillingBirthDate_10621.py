# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from locators import donors_registry_locators as locators
from base import BaseTest, Driver
from additional_functions import get_data, date_calculation
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-10621')
class TestFillingBirthDate(BaseTest):

	@allure.step('Валидация поля Дата рождения при добавлении донора: проверка ввода в поле')
	@pytest.mark.parametrize('birthdate, expected_result, test_data_set_number', get_data('data_test_filling_birthdate.csv'))
	def test_filling_birthdate(self, birthdate, expected_result, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.open()

		main_page.newdonor_click()
		
		main_page.ndp_filling_first_page("Сидоров", "Кирилл", "", birthdate, "8910", "650231")

		main_page.select_gender('male')

		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()

		main_page.if_donor_is_in_local_cabinet()

		main_page.ndp_second_page_loaded()

		aistium.click_on(elements=main_page.previous_step_ndp)

		if 'today' in expected_result:

			assert aistium.get_value(locators_list=locators, element_name='birthdate_field_ndp') == date_calculation(expected_result)

		else:

			assert aistium.get_value(locators_list=locators, element_name='birthdate_field_ndp') == expected_result

if __name__ == "__main__":
	pytest.main()