# -*- coding: utf-8 -*-
import pytest, aistium, allure, selenium, requests
from base import BaseTest, Driver
from locators import donors_registry_locators as locators
from additional_functions import sql_query, get_data
from donors_registry import DonorsModuleRegistryPage


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6817')
class TestStepBackwardDonationProcessWarningMessages(BaseTest):

	@allure.step('1. МД. Регистратура. Возврат направленного донора. Проверка текста предупреждающих сообщений')
	@pytest.mark.parametrize('query, test_data_set_number', get_data('data_test_step_backward_donation_process_warning_messages_a.csv'))
	def test_step_backward_donation_process_warning_messages_a(self, query, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		full_query = sql_query(query)

		donorid = str(full_query[0][0])

		expected_message = str(full_query[0][1])

		main_page.open()

		aistium.fill(donorid, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC left join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and (PerC.UniqueId = '"+donorid+"' or IDoc.Number = '"+donorid+"')) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		main_page.get_grid_values('UniqueId', ind, main_page.main_grid, mode='click')

		main_page.loading_is_completed()

		aistium.click_on(elements=main_page.process_state_button)

		main_page.loading_is_completed()

		aistium.click_on(locators_list=locators, element_name='confirm_popup_yes_btn')

		assert expected_message in aistium.get_text(locators_list=locators, element_name='confirm_popup')

	@allure.step('2. МД. Регистратура. Возврат направленного донора. Отмена возврата после предупреждающего сообщения')
	def test_step_backward_donation_process_warning_messages_b(self):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		full_query = sql_query(
			'''select top(1) PerC.UniqueId Ent from ref.SystemSettings SysSet, PersonCards PerC 
			join DonationProcessRegistry PrReg on PerC.UniqueId = PrReg.DonorId join Examinations Ex on PerC.UniqueId = Ex.DonorId 
			where PerC.IsDeleted != 1 and PrReg.OrgId = SysSet.CurrentOrganizationId and PrReg.RegDate = cast(getdate() as date) 
			and PrReg.CurrentState = 1 and PrReg.MobileTeamSessionId is null and cast(Ex.ExamDate as date) = cast(getdate() as date)'''
			)

		donorid = str(full_query[0][0])

		main_page.open()

		aistium.fill(donorid, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC left join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and (PerC.UniqueId = '"+donorid+"' or IDoc.Number = '"+donorid+"')) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		main_page.get_grid_values('UniqueId', ind, main_page.main_grid, mode='click')

		main_page.loading_is_completed()

		aistium.click_on(elements=main_page.process_state_button)

		main_page.loading_is_completed()

		aistium.click_on(locators_list=locators, element_name='confirm_popup_yes_btn')

		main_page.loading_is_completed()

		aistium.click_on(locators_list=locators, element_name='confirm_popup_no_btn')

		assert aistium.element_is_on_the_page(locators_list=locators, element_name='confirm_popup') == False

		assert aistium.get_text(main_page.process_state_button) == 'Вернуть'

		assert len(sql_query("select PrReg.Id from DonationProcessRegistry PrReg, ref.SystemSettings SysSet where PrReg.DonorId = '"+donorid+"' and PrReg.OrgId = SysSet.CurrentOrganizationId and PrReg.RegDate = cast(getdate() as date) and PrReg.CurrentState = 1 and PrReg.MobileTeamSessionId is null")) > 0

	@allure.step('3. МД. Регистратура. Возврат направленного донора. Подтверждение возврата при появлении предупреждающего сообщения')
	def test_step_backward_donation_process_warning_messages_c(self):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		full_query = sql_query(
			'''select top(1) PerC.UniqueId Ent from ref.SystemSettings SysSet, PersonCards PerC 
			join DonationProcessRegistry PrReg on PerC.UniqueId = PrReg.DonorId join Examinations Ex on PerC.UniqueId = Ex.DonorId 
			where PerC.IsDeleted != 1 and PrReg.OrgId = SysSet.CurrentOrganizationId and PrReg.RegDate = cast(getdate() as date) 
			and PrReg.CurrentState = 1 and PrReg.MobileTeamSessionId is null and cast(Ex.ExamDate as date) = cast(getdate() as date)'''
			)

		donorid = str(full_query[0][0])

		main_page.open()

		aistium.fill(donorid, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC left join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and (PerC.UniqueId = '"+donorid+"' or IDoc.Number = '"+donorid+"')) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		main_page.get_grid_values('UniqueId', ind, main_page.main_grid, mode='click')

		main_page.loading_is_completed()

		aistium.click_on(elements=main_page.process_state_button)

		main_page.loading_is_completed()

		aistium.click_on(locators_list=locators, element_name='confirm_popup_yes_btn')

		main_page.loading_is_completed()

		aistium.click_on(locators_list=locators, element_name='confirm_popup_yes_btn')

		assert main_page.element_is_on_page(main_page.edit_reason_back_donation_window) == True

if __name__ == "__main__":
	pytest.main()