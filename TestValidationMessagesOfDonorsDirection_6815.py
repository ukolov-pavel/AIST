# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from locators import donors_registry_locators as locators
from base import BaseTest, Driver
from additional_functions import sql_query, get_data
from donors_registry import DonorsModuleRegistryPage
from system_settings.product_settings import change_product_settings
from system_settings.donor_settings import change_donor_settings

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6815')
class TestValidationMessagesOfDonorsDirection(BaseTest):

	@allure.step('1. МД. Регистратура. Проверка текста запрещающих сообщений при направлении донора.')
	@pytest.mark.parametrize('query, test_data_set_number', get_data('data_test_validation_messages_of_donors_direction.csv'))
	def test_validation_messages_of_donors_direction(self, query, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		change_product_settings(AutoDonorAutomaticApprobation='false')

		change_donor_settings(CheckAntierythrocyteDonationOrExamination='true')

		full_query = sql_query(query)

		donorid = str(full_query[0][0])

		expected_message = full_query[0][1]

		main_page.clear_localstorage()

		main_page.open()

		aistium.fill(donorid, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC left join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and (PerC.UniqueId = '"+donorid+"' or IDoc.Number = '"+donorid+"')) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		main_page.ndp_get_grid_values('№', ind, 'click')

		main_page.loading_is_completed()

		aistium.click_on(elements=main_page.process_state_button)

		main_page.loading_is_completed()

		assert main_page.get_alert_text(mode='none').split('\n')[0] == 'Направление запрещено.'

		assert (expected_message in main_page.get_alert_text(mode='none').split('\n')[1:]) == True

if __name__ == "__main__":
	pytest.main()