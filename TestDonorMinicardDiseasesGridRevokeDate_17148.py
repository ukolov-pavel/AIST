# -*- coding: utf-8 -*-
import pytest, allure, selenium, requests, aistium
from base import BaseTest, Driver
from additional_functions import sql_query, get_data
from donors_registry import DonorsModuleRegistryPage
from locators import donors_registry_locators as locators


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-17148')
class TestDonorMinicardDiseasesGridRevokeDate(BaseTest):

	@allure.step('1. МД. Поле Снято в гриде, Заболевания донора (карточка донора в регистратуре донорского отделения)')
	@pytest.mark.parametrize('query, test_data_set_number', get_data('data_test_donor_minicard_diseases_grid_revoke_date_a.csv'))
	def test_donor_minicard_diseases_grid_revoke_date_a(self, query, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		full_query = sql_query(query)

		donorid = str(full_query[0][0])

		expected_result = str(full_query[0][1])

		main_page.open()

		aistium.fill(donorid, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC left join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and (PerC.UniqueId = '"+donorid+"' or IDoc.Number = '"+donorid+"')) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		main_page.get_grid_values('№', ind, 'click')

		main_page.loading_is_completed()

		aistium.click_on(elements=main_page.diseases_button)

		main_page.loading_is_completed()

		assert main_page.get_grid_values('RevokeDate', 1, main_page.diseases_grid) == expected_result

	@allure.step('2. МД. Поле Снято в гриде, Заболевания донора (карточка донора в регистратуре донорского отделения)')
	@pytest.mark.parametrize('query, test_data_set_number', get_data('data_test_donor_minicard_diseases_grid_revoke_date_b.csv'))
	def test_donor_minicard_diseases_grid_revoke_date_b(self, query, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		full_query = sql_query(query)

		donorid = str(full_query[0][0])

		expected_result = str(full_query[0][1])

		main_page.open()

		aistium.fill(donorid, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC left join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and (PerC.UniqueId = '"+donorid+"' or IDoc.Number = '"+donorid+"')) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		main_page.get_grid_values('№', ind, 'click')

		main_page.loading_is_completed()

		aistium.click_on(elements=main_page.diseases_button)

		main_page.loading_is_completed()

		if main_page.get_diseases_only_active_value() == 'true':
			aistium.click_on(elements=main_page.diseases_only_active)

		assert main_page.get_grid_values('RevokeDate', 1, main_page.diseases_grid) == expected_result

if __name__ == "__main__":
	pytest.main()