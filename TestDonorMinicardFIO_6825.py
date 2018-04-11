# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import sql_query, get_data
from donors_registry import DonorsModuleRegistryPage
from donors_card_title import DonorsCardTitle

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6825')
class TestDonorCardFIO(BaseTest):

	@allure.step('1. МД. ФИО донора (карточка донора в регистратуре донорского отделения) (автотест)')
	@pytest.mark.parametrize('query, test_data_set_number', get_data('data_test_donor_minicard_fio_a.csv'))
	def test_donor_minicard_fio_a(self, query, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		full_query = sql_query(query)

		donorid = str(full_query[0][0])

		expected_result = str(full_query[0][1])

		main_page.clear_localstorage()

		main_page.open()

		aistium.fill(donorid, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC left join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and (PerC.UniqueId = '"+donorid+"' or IDoc.Number = '"+donorid+"')) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		main_page.get_grid_values('UniqueId', ind, main_page.main_grid, 'click')

		main_page.loading_is_completed()

		assert aistium.get_text(elements=main_page.fio_minicard) == expected_result

	@allure.step('2. МД. ФИО донора (карточка донора в регистратуре донорского отделения) (автотест)')
	@pytest.mark.parametrize('query, expected_text_color, test_data_set_number', get_data('data_test_donor_minicard_fio_b.csv'))
	def test_donor_minicard_fio_b(self, query, expected_text_color, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		full_query = sql_query(query)

		donorid = str(full_query[0][0])

		main_page.clear_localstorage()

		main_page.open()

		aistium.fill(donorid, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC left join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and (PerC.UniqueId = '"+donorid+"' or IDoc.Number = '"+donorid+"')) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		main_page.get_grid_values('UniqueId', ind, main_page.main_grid, 'click')

		main_page.loading_is_completed()

		assert main_page.get_donor_minicard_fio_color() == expected_text_color

	@allure.step('3. МД. ФИО донора (карточка донора в регистратуре донорского отделения) (автотест)')
	def test_donor_minicard_fio_c(self):
		main_page = DonorsModuleRegistryPage()

		donorid = str(sql_query("select top(1) PerC.UniqueId Ent from PersonCards PerC where PerC.IsDeleted != 1 and PerC.LastName not like '%[a-zA-Z0-9.- ,:;?!_+=*\/|%()}{<>`~@#$^&№«»]%' and PerC.FirstName not like '%[a-zA-Z0-9.- ,:;?!_+=*\/|%()}{<>`~@#$^&№«»]%' and PerC.MiddleName not like '%[a-zA-Z0-9.- ,:;?!_+=*\/|%()}{<>`~@#$^&№«»]%' and len(PerC.LastName) > 0 and len(PerC.FirstName) > 0 and len(PerC.MiddleName) > 0")[0][0])

		donors_card_title_page = DonorsCardTitle(donorid)

		main_page.clear_localstorage()

		main_page.open()

		aistium.fill(donorid, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC left join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and (PerC.UniqueId = '"+donorid+"' or IDoc.Number = '"+donorid+"')) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		main_page.get_grid_values('UniqueId', ind, main_page.main_grid, 'click')

		main_page.loading_is_completed()

		main_page.fio_minicard.click()

		donors_card_title_page.loading_is_completed()

		assert donors_card_title_page.get_url() == BaseTest.stand+'/Donor/Registration/Edit/'+donorid+'?showDeleted=False'

if __name__ == "__main__":
	pytest.main()