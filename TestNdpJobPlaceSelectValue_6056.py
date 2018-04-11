# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from selenium.webdriver.common.keys import Keys
from locators import donors_registry_locators as locators
from base import BaseTest, Driver
from additional_functions import sql_query
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6056')
class TestNdpJobPlaceSelectValue(BaseTest):

	@allure.step('2. Выбор места работы/учёбы из списка')
	def test_job_place_select_value(self):

		main_page = DonorsModuleRegistryPage()

		main_page.open()
		
		place_ent = str(sql_query("select top (1) lower(substring(PerC.JobInfo, 2, 6)) Ent from PersonCards PerC where len(PerC.JobInfo) > 10 and PerC.JobInfo not like '%[a-zA-Z0-9?!_+=*\/%()}{<>^%]'"))[3:-5]

		places_s = []

		main_page.newdonor_click()

		main_page.ndp_filling_first_page('Сидоров', "Анатолий", "", "01.06.1980", "2910", "650231")
		
		main_page.select_gender('male')

		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()

		main_page.if_donor_is_in_local_cabinet()

		main_page.ndp_second_page_loaded()

		aistium.fill(place_ent, elements=main_page.ndp_job_place_field)

		for place_s in main_page.ndp_place_list_on_form():
			places_s.append(str(place_s))

		job_place_need = places_s[0]

		aistium.fill(Keys.ENTER, elements=main_page.ndp_job_place_field)

		job_place = aistium.get_value(locators_list=locators, element_name='job_place')

		assert job_place == job_place_need
	
if __name__ == "__main__":
	pytest.main()