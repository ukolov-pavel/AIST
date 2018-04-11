# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import sql_query, get_data, convert_phenotype, replace_phenotype
from donors_registry import DonorsModuleRegistryPage
from system_settings.general_settings import change_general_settings

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6664')
class TestGridPhenotype(BaseTest):

	@allure.step('МД. Отображение поля Фенотип в гриде (регистратура донорского отделения) - убрать флаг для настройки "Краткая форма (буквенная) для отображения фенотипа"')
	@pytest.mark.parametrize('query, test_data_set_number', get_data('data_test_grid_phenotype_a.csv'))
	def test_grid_phenotype_a(self, query, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		change_general_settings(UsePhenotypeShortFormat='false')

		full_query = sql_query(query)

		donorid, expected_result = str(full_query[0][0]), full_query[0][1]

		phenotype = convert_phenotype(expected_result)

		main_page.clear_localstorage()

		main_page.open()

		aistium.fill(donorid, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC left join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and (PerC.UniqueId = '"+donorid+"' or IDoc.Number = '"+donorid+"')) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		assert main_page.ndp_get_grid_values('Фенотип', ind) == phenotype


	@allure.step('МД. Отображение поля Фенотип в гриде (регистратура донорского отделения) - выставить флаг для настройки "Краткая форма (буквенная) для отображения фенотипа"')
	@pytest.mark.parametrize('query, test_data_set_number', get_data('data_test_grid_phenotype_b.csv'))
	def test_grid_phenotype_b(self, query, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		change_general_settings(UsePhenotypeShortFormat='true')

		full_query = sql_query(query)

		donorid, expected_result = str(full_query[0][0]), full_query[0][1]

		phenotype = replace_phenotype(convert_phenotype(expected_result))

		main_page.clear_localstorage()

		main_page.open()

		aistium.fill(donorid, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC left join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and (PerC.UniqueId = '"+donorid+"' or IDoc.Number = '"+donorid+"')) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		assert main_page.ndp_get_grid_values('Фенотип', ind) == phenotype

	@allure.step('МД. Отображение поля Фенотип в гриде (регистратура донорского отделения) - выставить флаг для настройки "Краткая форма (буквенная) для отображения фенотипа", но значения фенотипа не должны измениться')
	@pytest.mark.parametrize('query, test_data_set_number', get_data('data_test_grid_phenotype_c.csv'))
	def test_grid_phenotype_с(self, query, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		change_general_settings(UsePhenotypeShortFormat='true')

		full_query = sql_query(query)

		donorid, expected_result = str(full_query[0][0]), full_query[0][1]

		phenotype = convert_phenotype(expected_result)

		main_page.clear_localstorage()

		main_page.open()

		aistium.fill(donorid, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC left join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and (PerC.UniqueId = '"+donorid+"' or IDoc.Number = '"+donorid+"')) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		assert main_page.ndp_get_grid_values('Фенотип', ind) == phenotype


if __name__ == "__main__":
	pytest.main()