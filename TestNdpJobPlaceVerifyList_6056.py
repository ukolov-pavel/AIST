# -*- coding: utf-8 -*-
import pytest
import allure
import selenium
import aistium
from collections import OrderedDict
from itertools import repeat
from base import BaseTest, Driver
from additional_functions import sql_query
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6056')
class TestNdpJobPlaceVerifyList(BaseTest):

	@allure.step('1. Выбор места работы/учёбы из списка')
	def test_ndp_job_place_verify_list(self):

		main_page = DonorsModuleRegistryPage()

		main_page.open()
		
		place_ent = str(sql_query("select top (1) lower(substring(PerC.JobInfo, 2, 3)) Ent from PersonCards PerC where len(PerC.JobInfo) > 5 and PerC.JobInfo not like '%[a-zA-Z0-9?!_+=*\/%()}{<>^%' and substring(PerC.JobInfo, 4, 1) != ' '"))[3:-5]

		places_db = []

		places_s = []

		main_page.newdonor_click()

		main_page.ndp_filling_first_page('Сидоров', "Анатолий", "", "01.06.1980", "2910", "650231")
		
		main_page.select_gender('male')

		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()

		main_page.if_donor_is_in_local_cabinet()

		main_page.ndp_second_page_loaded()

		aistium.fill(place_ent, elements=main_page.ndp_job_place_field)

		for place in sql_query("select upper(PerC.JobInfo) JobInfo from PersonCards PerC where PerC.JobInfo like '%" + place_ent + "%'"):
			places_db.append(place[0])

		places_db = list(OrderedDict(zip(places_db, repeat(None))))

		places_db.sort()

		for place_s in main_page.ndp_place_list_on_form():
			places_s.append(str(place_s).upper())

		job_place_need = places_s[0]

		places_s.sort()

		assert places_s == places_db

if __name__ == "__main__":
	pytest.main()