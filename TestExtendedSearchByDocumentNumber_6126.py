# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import sql_query, get_data
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6126')
class TestExtendedSearchByDDocumentNumber(BaseTest):

	@allure.step('1. МД. Поиск донора по Номеру документа (расширенный поиск в регистратуре донорского отделения)')
	@pytest.mark.parametrize('document_type, document_number, expected_result, test_data_set_number', get_data('data_test_extended_search_by_document_number_a.tsv', expansion='tsv'))
	def test_extended_search_by_document_number_a(self, document_type, document_number, expected_result, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()

		main_page.extended_search_click('open')

		main_page.filling_doc_type_in_extended_search(document_type)

		main_page.filling_doc_number_in_extended_search(document_number)

		assert main_page.get_document_number_from_extended_search() == expected_result

	@allure.step('2. МД. Поиск донора по Номеру документа (расширенный поиск в регистратуре донорского отделения)')
	@pytest.mark.parametrize('document_type, query, test_data_set_number', get_data('data_test_extended_search_by_document_number_b.csv'))
	def test_extended_search_by_document_number_b(self, document_type, query, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		full_query = sql_query(query)

		donorid = str(full_query[0][0])

		document_number = str(full_query[0][1])

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and IDoc.Number = '"+document_number+"' and cast(IDoc.DocType as varchar) like case when '"+document_type+"' = '' then '%' when '"+document_type+"' = 'Паспорт РФ' then '1' when '"+document_type+"' = 'Военный билет' then '2' when '"+document_type+"' = 'Загранпаспорт РФ' then '3' when '"+document_type+"' = 'Паспорт СССР' then '4' when '"+document_type+"' = 'Иные документы' then '5' when '"+document_type+"' = 'Св-во о рождении' then '6' end) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		main_page.clear_localstorage()

		main_page.open()

		main_page.extended_search_click('open')

		main_page.filling_doc_type_in_extended_search(document_type)

		main_page.filling_doc_number_in_extended_search(document_number)

		aistium.click_on(elements=main_page.extended_search_button)

		main_page.loading_is_completed()

		assert main_page.get_grid_values('UniqueId', ind, main_page.main_grid) == donorid

		assert main_page.number_of_entities_at_grid_including_hidden() == sql_query("select count ( * ) Q from PersonCards PerC join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and IDoc.Number = '"+document_number+"' and cast(IDoc.DocType as varchar) like case when '"+document_type+"' = '' then '%' when '"+document_type+"' = 'Паспорт РФ' then '1' when '"+document_type+"' = 'Военный билет' then '2' when '"+document_type+"' = 'Загранпаспорт РФ' then '3' when '"+document_type+"' = 'Паспорт СССР' then '4' when '"+document_type+"' = 'Иные документы' then '5' when '"+document_type+"' = 'Св-во о рождении' then '6' end")[0][0]

if __name__ == "__main__":
	pytest.main()