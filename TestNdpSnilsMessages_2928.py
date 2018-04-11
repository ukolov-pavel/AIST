# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import get_data, sql_query
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-2928')
class TestNdpSnilsMessages(BaseTest):

	@allure.step('Проверка валидационных сообщений поля "СНИЛС"')
	@pytest.mark.parametrize('snils, expected_result, test_data_set_number', get_data('data_test_ndp_snils_validation_messages.csv'))
	def test_ndp_snils_validation_message(self, snils, expected_result, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()

		main_page.newdonor_click()

		main_page.ndp_filling_first_page("Сидоров", "Кирилл", "", "01.06.1980", "8910", "650231")

		main_page.select_gender('male')

		main_page.ndp_filling_snils(snils)

		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()

		assert main_page.get_validation_message_text() == expected_result

	@allure.step('Проверка запрещающих сообщений поля "СНИЛС"')
	def test_ndp_snils_alert(self):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()

		query = sql_query("select top (1) PerC.Snils Ent, rtrim(substring(PerC.Snils, 1, 3) + '' + substring(PerC.Snils, 4, 3) + '' + substring(PerC.Snils, 7, 3) + ' ' + substring(PerC.Snils, 10, 2) + ' ' + PerC.LastName + ' ' + PerC.FirstName + ' ' + PerC.MiddleName) Iden from PersonCards PerC where PerC.Snils is not null")

		snils = query[0][0]

		iden = query[0][1]

		iden = '-'.join(iden.split(' ')[0][i:i + 3] for i in range(0, len(iden.split(' ')[0]), 3)) + ' ' + iden.split(' ')[1] + ' ' + iden.split(' ')[2] + ' ' + iden.split(' ')[3] + ' ' + iden.split(' ')[4]

		main_page.newdonor_click()

		main_page.ndp_filling_first_page("Сидоров", "Кирилл", "", "01.06.1980", "8910", "650231")

		main_page.select_gender('male')

		aistium.fill(snils, elements=main_page.snils_field)

		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()

		assert main_page.get_alert_text() == "В картотеке найдены карты с указанным СНИЛС "+iden+" Карта со СНИЛС может быть только одна!"

if __name__ == "__main__":
	pytest.main()