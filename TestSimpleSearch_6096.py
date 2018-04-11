# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from locators import donors_registry_locators as locators
from base import BaseTest, Driver
from additional_functions import sql_query, get_data, convert_to_hex
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6096')
class TestSimpleSearch(BaseTest):

	@allure.step('1. МД. Регистратура. Проверка быстрого поиска. Поиск при незаполненном поле быстрого поиска.')
	def test_simple_search_a(self):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()

		main_page.quick_search('click')

		main_page.loading_is_completed()

		assert main_page.number_of_entities_at_grid() == 0

	@allure.step('2. МД. Регистратура. Проверка быстрого поиска. Успешный поиск, в гриде есть запись с нужным номером донора.')
	@pytest.mark.parametrize('query, mode, test_data_set_number', get_data('data_test_simple_search_b.csv'))
	def test_simple_search_b(self, query, mode, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		donorid = str(sql_query(query)[0][0])

		main_page.clear_localstorage()

		main_page.open()

		aistium.fill(donorid, elements=main_page.quick_search_field)

		main_page.quick_search(mode)

		main_page.loading_is_completed()

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC left join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and (PerC.UniqueId = '"+donorid+"' or IDoc.Number = '"+donorid+"')) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		assert main_page.ndp_get_grid_values('№', ind) == donorid

	@allure.step('3. МД. Регистратура. Проверка быстрого поиска. В гриде нет записи с номером донора в столбце "№".')
	def test_simple_search_c(self):
		main_page = DonorsModuleRegistryPage()

		donorid = str(sql_query("select top (1) PerC.UniqueId Ent from PersonCards PerC where PerC.IsDeleted = '1' and convert(nvarchar(10), PerC.UniqueId) not in (select IDoc.Number Nb from IdentityDocs IDoc)")[0][0])

		main_page.clear_localstorage()

		main_page.open()

		aistium.fill(donorid, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		assert main_page.get_alert_text() == 'Донор не найден.'

		assert main_page.number_of_entities_at_grid() == 0

	@allure.step('4. МД. Регистратура. Проверка быстрого поиска. Позиционирование на единственной найденной записи; открытие мини-карты найденного донора.')
	def test_simple_search_d(self):
		main_page = DonorsModuleRegistryPage()

		donorid = str(sql_query("select top (1) PerC.UniqueId from PersonCards PerC join IdentityDocs IDoc on IDoc.UniqueId = PerC.IdentityDocId where convert(nvarchar(10), PerC.UniqueId) not in (select IDoc.Number from IdentityDocs IDoc) and PerC.IsDeleted != 1")[0][0])

		main_page.clear_localstorage()

		main_page.open()

		aistium.fill(donorid, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC left join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and (PerC.UniqueId = '"+donorid+"' or IDoc.Number = '"+donorid+"')) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		assert main_page.is_grid_row_selected(ind) == True

		assert main_page.link_to_donor_card() == BaseTest.stand+'/Donor/Registration/Edit/'+donorid+'?showDeleted=False'

	@allure.step('5. МД. Регистратура. Проверка быстрого поиска. Поиск при незаполненном поле быстрого поиска.')
	def test_simple_search_e(self):
		main_page = DonorsModuleRegistryPage()

		lastname = str(sql_query("select top (1) PerC.LastName Ent from PersonCards PerC join (select PerC.LastName, count ( * ) Q from PersonCards PerC where PerC.IsDeleted != 1 group by PerC.LastName) GL on PerC.LastName = Gl.LastName where PerC.IsDeleted != 1 and PerC.LastName not like '%[a-zA-Z0-9?!_+=*\/%()}{<>^]%' and Gl.Q > 1")[0][0])

		main_page.clear_localstorage()

		main_page.open()

		aistium.fill(lastname, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		assert main_page.number_of_entities_at_grid() > 1

		assert main_page.is_element_positioned('SimpleSearchText') == True

		assert main_page.is_simple_search_text_selected() == lastname

	@allure.step('6. МД. Регистратура. Проверка быстрого поиска.')
	@pytest.mark.parametrize('string, expected_result, test_data_set_number', get_data('data_test_simple_search_f.csv'))
	def test_simple_search_f(self, string, expected_result, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()

		aistium.fill(string, elements=main_page.quick_search_field)

		assert aistium.get_value(locators_list=locators, element_name='quick_search_field') == expected_result

if __name__ == "__main__":
	pytest.main()