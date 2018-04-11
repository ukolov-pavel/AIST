# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import sql_query, get_data, date_calculation
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6129')
class TestExtendedSearchByBirthdate(BaseTest):

	@allure.step('1. МД. Поиск донора по Дате рождения (запрещающие сообщения) (расширенный поиск в регистратуре донорского отделения)')
	@pytest.mark.parametrize('birthdate_from, birthdate_to, expected_result, test_data_set_number', get_data('data_test_extended_search_by_birthdate_validation_messages.csv'))
	def test_extended_search_by_birthdate_validation_messages(self, birthdate_from, birthdate_to, expected_result, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()

		main_page.extended_search_click('open')

		aistium.fill(birthdate_from, elements=main_page.extended_birthdate_from)

		aistium.fill(birthdate_to, elements=main_page.extended_birthdate_to)

		aistium.click_on(elements=main_page.extended_search_button)

		main_page.loading_is_completed()

		assert main_page.get_alert_text() == expected_result

if __name__ == "__main__":
	pytest.main()