# -*- coding: utf-8 -*-
import pytest
import allure
import selenium
import datetime
from selenium import webdriver
from base import BaseTest
from base import Driver
from donors_registry import DonorsModuleRegistryPage
from donors_list_of_directed import DonorsListOfDirected

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6093')
class TestAgreeCheckboxes(BaseTest):

	@allure.step('Проверка работы кнопки "К списку"')
	def test_to_list_of_directed(self):
		main_page = DonorsModuleRegistryPage()

		main_page.open()

		main_page.list_of_directed_button_click()

		list_of_directed = DonorsListOfDirected()

		list_of_directed.get_title() == 'Список направленных'

		list_of_directed.get_directed_date_value() == datetime.date.today().strftime('%d.%m.%Y')

if __name__ == "__main__":
	pytest.main()