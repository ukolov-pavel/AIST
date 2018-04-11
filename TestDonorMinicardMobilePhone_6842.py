# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import sql_query, get_data
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6842')
class TestDonorCardMobilePhone(BaseTest):

	@allure.step('МД. Мобильный телефон (карточка донора в регистратуре донорского отделения) (автотест)')
	@pytest.mark.parametrize('query, test_data_set_number', get_data('data_test_donor_minicard_mobile_phone.csv'))
	def test_donor_minicard_mobile_phone(self, query, test_data_set_number):
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

		if expected_result == '':
			assert aistium.element_is_on_the_page(locators_list='minicard_mobile_phone',element_name='minicard_mobile_phone') == False
		else:
			assert aistium.get_text(elements=main_page.minicard_mobile_phone) == expected_result

if __name__ == "__main__":
	pytest.main()