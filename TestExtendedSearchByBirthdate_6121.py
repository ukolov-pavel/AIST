# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import sql_query, get_data, date_calculation
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6121')
class TestExtendedSearchByBirthdate(BaseTest):

	@allure.step('1. МД. Поиск донора по Дате рождения (расширенный поиск в регистратуре донорского отделения)')
	@pytest.mark.parametrize('birthdate, expected_result, test_data_set_number', get_data('data_test_extended_search_by_birthdate_a.tsv', expansion='tsv'))
	def test_extended_search_by_birthdate_a(self, birthdate, expected_result, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()

		main_page.extended_search_click('open')

		if 'today' in birthdate:

			aistium.fill(date_calculation(birthdate), elements=main_page.extended_birthdate_from)

			aistium.fill(date_calculation(birthdate), elements=main_page.extended_birthdate_to)

		else:

			aistium.fill(birthdate, elements=main_page.extended_birthdate_from)

			aistium.fill(birthdate, elements=main_page.extended_birthdate_to)

		if 'today' in expected_result:

			assert main_page.get_birth_date_from_from_extended_search() == date_calculation(expected_result)

			assert main_page.get_birth_date_to_from_extended_search() == date_calculation(expected_result)

		else:

			assert main_page.get_birth_date_from_from_extended_search() == expected_result

			assert main_page.get_birth_date_to_from_extended_search() == expected_result
		
	@allure.step('2. МД. Поиск донора по Дате рождения (расширенный поиск в регистратуре донорского отделения)')
	@pytest.mark.parametrize('query_birthdate_from, query_birthdate_to, test_data_set_number', get_data('data_test_extended_search_by_birthdate_b.csv'))
	def test_extended_search_by_birthdate_b(self, query_birthdate_from, query_birthdate_to, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		full_query_from = sql_query(query_birthdate_from)

		birthdate_from = str(full_query_from[0][1])

		full_query_to = sql_query(query_birthdate_to)

		birthdate_to = str(full_query_to[0][1])

		donorid = str(full_query_from[0][0])

		if donorid == '':

			donorid = str(full_query_to[0][0])

		#ind = str(sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC where PerC.IsDeleted != 1 and PerC.BirthDate between case when '"+birthdate_from+"' = '' then '01.01.1753' else '"+birthdate_from+"' end and case when '"+birthdate_to+"' = '' then '31.12.9999' else '"+birthdate_to+"' end group by PerC.UniqueId, PerC.BirthDate) Main where Main.UniqueId = '"+donorid+"'")[0][0])

		main_page.clear_localstorage()

		main_page.open()

		main_page.extended_search_click('open')

		aistium.fill(birthdate_from, elements=main_page.extended_birthdate_from)

		aistium.fill(birthdate_to, elements=main_page.extended_birthdate_to)

		aistium.click_on(elements=main_page.extended_search_button)

		main_page.loading_is_completed()

		#assert main_page.get_grid_values('UniqueId', ind, main_page.main_grid) == donorid

		assert main_page.number_of_entities_at_grid_including_hidden() == sql_query("select count ( * ) Q from PersonCards PerC where PerC.IsDeleted != 1 and PerC.BirthDate between case when '"+birthdate_from+"' = '' then '01.01.1753' else '"+birthdate_from+"' end and case when '"+birthdate_to+"' = '' then '31.12.9999' else '"+birthdate_to+"' end")[0][0]

if __name__ == "__main__":
	pytest.main()