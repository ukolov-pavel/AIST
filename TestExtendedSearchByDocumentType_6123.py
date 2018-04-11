# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import sql_query, get_data
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6123')
class TestExtendedSearchByDocumentType(BaseTest):

	@allure.step('1. МД. Поиск донора по Типу документа (расширенный поиск в регистратуре донорского отделения)')
	def test_extended_search_by_document_type_a(self):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()

		main_page.extended_search_click('open')

		assert main_page.get_document_types_listbox_from_extended_search() == ['','Паспорт РФ','Военный билет','Загранпаспорт РФ','Паспорт СССР','Иные документы','Св-во о рождении']

	@allure.step('2. МД. Поиск донора по Типу документа (расширенный поиск в регистратуре донорского отделения)')
	def test_extended_search_by_document_type_b(self):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()

		main_page.extended_search_click('open')

		main_page.filling_doc_type_in_extended_search('Паспорт РФ')

		main_page.filling_doc_type_in_extended_search('') #вот здесь падает http://joxi.ru/a2XlR6kty8qGW2

		assert main_page.is_extended_search_button_disable() == 'true'
		
	@allure.step('3. МД. Поиск донора по Типу документа (расширенный поиск в регистратуре донорского отделения)')
	@pytest.mark.parametrize('document_type, query, test_data_set_number', get_data('data_test_extended_search_by_document_type_c.csv'))
	def test_extended_search_by_document_type_c(self, document_type, query, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		donorid = str(sql_query(query)[0][0])

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and IDoc.DocType = case when '"+document_type+"' = 'Паспорт РФ' then 1 when '"+document_type+"' = 'Военный билет' then 2 when '"+document_type+"' = 'Загранпаспорт РФ' then 3 when '"+document_type+"' = 'Паспорт СССР' then 4 when '"+document_type+"' = 'Иные документы' then 5 when '"+document_type+"' = 'Св-во о рождении' then 6 end) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		main_page.clear_localstorage()

		main_page.open()

		main_page.extended_search_click('open')

		main_page.filling_doc_type_in_extended_search(document_type)

		aistium.click_on(elements=main_page.extended_search_button)

		main_page.loading_is_completed()

		assert main_page.get_grid_values('UniqueId', ind, main_page.main_grid) == donorid

		assert main_page.number_of_entities_at_grid_including_hidden() == sql_query("select count ( * ) Q from PersonCards PerC join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and IDoc.DocType = case when '"+document_type+"' = 'Паспорт РФ' then 1 when '"+document_type+"' = 'Военный билет' then 2 when '"+document_type+"' = 'Загранпаспорт РФ' then 3 when '"+document_type+"' = 'Паспорт СССР' then 4 when '"+document_type+"' = 'Иные документы' then 5 when '"+document_type+"' = 'Св-во о рождении' then 6 end")[0][0]

if __name__ == "__main__":
	pytest.main()