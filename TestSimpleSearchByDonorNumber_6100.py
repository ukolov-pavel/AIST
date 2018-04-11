# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import sql_query
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6100')
class TestSimpleSearchByDonorNumber(BaseTest):

	@allure.step('Поиск донора по номеру (быстрый поиск в регистратуре донорского отделения)')
	def test_simple(self):
		main_page = DonorsModuleRegistryPage()

		donor_number = str(sql_query("select top (1) PerC.UniqueId from PersonCards PerC join IdentityDocs IDoc on IDoc.UniqueId = PerC.IdentityDocId where convert(nvarchar(10), PerC.UniqueId) not in (select IDoc.Number from IdentityDocs IDoc) and PerC.IsDeleted != 1")[0][0])

		main_page.clear_localstorage()

		main_page.open()

		aistium.fill(donor_number, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		assert main_page.get_grid_values('UniqueId', 'active_cell', main_page.main_grid) == donor_number

if __name__ == "__main__":
	pytest.main()