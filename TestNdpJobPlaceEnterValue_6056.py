# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import sql_query
from donors_registry import DonorsModuleRegistryPage
from donors_card_title import DonorsCardTitle

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6056')
class TestNdpJobPlaceEnterValue(BaseTest):

	@allure.step('3. Ввод значения, которого нет в списке')
	def test_job_place_enter_value(self):

		i = 1

		sel = 'a'
			
		while len(sel) > 0:
			place_ent = str(sql_query("select ls.Pl from (select row_number() over (order by PerC.UniqueId asc) as rank, PerC.JobInfo + ' ООО' Pl from PersonCards PerC where len(PerC.JobInfo) < 57 and PerC.JobInfo not like '%[a-zA-Z0-9?!_+=*\/%()}{<>^]%') ls where ls.rank = '" + str(i) + "'"))[3:-5]
			sel = str(sql_query("select top (1) PerC.JobInfo from PersonCards PerC where PerC.JobInfo = '" + place_ent + "'"))[3:-5]
			i = i + 1
	
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()

		main_page.newdonor_click()

		main_page.ndp_filling_first_page('Сидоров', "Анатолий", "", "01.06.1980", "2910", "650231")
		
		main_page.select_gender('male')

		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()

		main_page.if_donor_is_in_local_cabinet()

		main_page.ndp_second_page_loaded()

		main_page.ndp_filling_region('Москва г')

		main_page.ndp_filling_street('Перова Поля 3-й проезд')

		aistium.fill('21', elements=main_page.reg_fias_address_house)

		aistium.fill(place_ent, elements=main_page.ndp_job_place_field)

		main_page.ndp_save_new_donor('success')

		main_page.loading_is_completed()

		grid_donor_id = main_page.ndp_get_grid_values('№', 'active_cell')

		donors_card_title_page = DonorsCardTitle(grid_donor_id)

		donors_card_title_page.open()

		assert donors_card_title_page.job_place() == place_ent

if __name__ == "__main__":
	pytest.main()