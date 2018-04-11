# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import sql_query
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6099')
class TestSimpleSearchByDocumentNumber(BaseTest):

	@allure.step('Поиск донора по номеру документа')
	def test_simple(self):
		main_page = DonorsModuleRegistryPage()

		document_number = sql_query("select top (1) IDoc.Number Nm from IdentityDocs IDoc join PersonCards PerC on IDoc.UniqueId = PerC.IdentityDocId where len(IDoc.Number) > 3 and IDoc.Number not like '%[а-яА-Яa-zA-Z?!_+=*\/%()}{<>^]%' and IDoc.Number not in (select convert(nvarchar(10), PerC.UniqueId) from PersonCards PerC) and PerC.IsDeleted != 1")[0][0]

		main_page.clear_localstorage()

		main_page.open()

		aistium.fill(document_number, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		assert document_number in main_page.get_grid_values('Document', 1, main_page.main_grid)

if __name__ == "__main__":
	pytest.main()