# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import sql_query, get_data
from donors_registry import DonorsModuleRegistryPage
from system_settings.donor_settings import change_donor_settings

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6837')
class TestDonorCardJobPlace(BaseTest):

	@allure.step('1. МД. Место работы (карточка донора в регистратуре донорского отделения) (автотест)')
	@pytest.mark.parametrize('query, test_data_set_number', get_data('data_test_donor_minicard_job_place_a.csv'))
	def test_donor_minicard_job_place_a(self, query, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		full_query = sql_query(query)

		donorid = str(full_query[0][0])

		expected_result = str(full_query[0][1])

		change_donor_settings(ShowJobInfo='true')

		main_page.clear_localstorage()

		main_page.open()

		aistium.fill(donorid, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC left join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and (PerC.UniqueId = '"+donorid+"' or IDoc.Number = '"+donorid+"')) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		main_page.get_grid_values('UniqueId', ind, main_page.main_grid, 'click')

		main_page.loading_is_completed()

		if expected_result == '':
			assert aistium.element_is_on_the_page(locators_list='minicard_job_place_label',element_name='minicard_job_place_label') == False
		else:
			assert main_page.minicard_get_job_place() == expected_result

	@allure.step('2. МД. Место работы (карточка донора в регистратуре донорского отделения) (автотест)')
	def test_donor_minicard_job_place_b(self):
		main_page = DonorsModuleRegistryPage()

		donorid = str(sql_query("select top(1) PerC.UniqueId Ent from PersonCards PerC where PerC.IsDeleted != 1 and len(PerC.JobInfo) > 0")[0][0])

		change_donor_settings(ShowJobInfo='false')

		main_page.clear_localstorage()

		main_page.open()

		aistium.fill(donorid, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC left join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and (PerC.UniqueId = '"+donorid+"' or IDoc.Number = '"+donorid+"')) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		main_page.get_grid_values('UniqueId', ind, main_page.main_grid, 'click')

		main_page.loading_is_completed()

		assert aistium.element_is_on_the_page(locators_list='minicard_job_place_label',element_name='minicard_job_place_label') == False

if __name__ == "__main__":
	pytest.main()