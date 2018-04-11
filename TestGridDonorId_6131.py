# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import sql_query, get_data
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6131')
class TestGridDonorId(BaseTest):

	@allure.step('МД. Отображение поля № в гриде (регистратура донорского отделения)')
	@pytest.mark.parametrize('query, test_data_set_number', get_data('data_test_grid_donor_id.csv'))
	def test_grid_donor_id(self, query, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		full_query = sql_query(query)

		donor_id, fullname, lastname, firstname, middlename = str(full_query[0][0]), full_query[0][1], full_query[0][2], full_query[0][3], full_query[0][4]

		main_page.clear_localstorage()

		main_page.open()

		aistium.fill(fullname, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC where PerC.IsDeleted != 1 and PerC.LastName like '"+lastname+"%' and PerC.FirstName like '"+firstname+"%' and PerC.MiddleName like '"+middlename+"%') Main where Main.UniqueId = "+donor_id)[0][0]

		assert main_page.ndp_get_grid_values('№', ind) == donor_id

if __name__ == "__main__":
	pytest.main()