# -*- coding: utf-8 -*-
import pytest, allure, selenium, requests, aistium
from base import BaseTest, Driver
from locators import donors_registry_locators as locators
from additional_functions import sql_query, get_data
from donors_registry import DonorsModuleRegistryPage
from system_settings.donor_settings import change_donor_settings
from system_settings.sticker_settings import change_sticker_settings


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6814')
class TestDonorsDirectionWarningMessages(BaseTest):

	@allure.step('1. МД. Регистратура. Направление донора. Проверка текста предупреждающих сообщений')
	@pytest.mark.parametrize('query, test_data_set_number', get_data('data_test_donors_direction_warning_messages_a.csv'))
	def test_donors_direction_warning_messages_a(self, query, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		change_donor_settings(CheckDonorInFicWhileDirection='false', 
			CheckFiasAddressForDonor='true', 
			CheckIncompleteAnalysis= 'true', 
			AlwaysShowEpidAddress='true')

		full_query = sql_query(query)

		donorid = str(full_query[0][0])

		expected_message = str(full_query[0][1])

		main_page.open()

		aistium.fill(donorid, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC left join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and (PerC.UniqueId = '"+donorid+"' or IDoc.Number = '"+donorid+"')) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		main_page.ndp_get_grid_values('№', ind, 'click')

		main_page.loading_is_completed()

		aistium.click_on(elements=main_page.process_state_button)

		main_page.loading_is_completed()

		assert expected_message in aistium.get_text(locators_list=locators, element_name='confirm_popup')

	@allure.step('2. МД. Регистратура. Направление донора. Отмена направления после предупреждающего сообщения')
	def test_donors_direction_warning_messages_b(self):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		change_donor_settings(CheckDonorInFicWhileDirection='false', 
			CheckFiasAddressForDonor='true', 
			CheckIncompleteAnalysis= 'true', 
			AlwaysShowEpidAddress='true')

		full_query = sql_query(
			'''select top(1) PerC.UniqueId Ent, 'Донор отведён (тип отвода: Абсолютный).' 
			OR1 from PersonCards PerC join AppointedDonationTypes AppD on PerC.UniqueId = AppD.DonorId 
			join (select AppD.DonorId, max(AppD.DonationDate) MaxDate from AppointedDonationTypes AppD group by AppD.DonorId) 
			Main on AppD.DonorId = Main.DonorId and AppD.DonationDate = Main.MaxDate 
			join ref.DonationTypeParams DonTP on AppD.DonationTypeId = DonTP.DonationTypeId 
			join ref.DonationTypes DonT on AppD.DonationTypeId = DonT.UniqueId 
			join Deferrals Def on PerC.UniqueId = Def.DonorId and Def.RevokeDate is null 
			join ref.DeferralTypes DefT on Def.DeferralTypeId = DefT.UniqueId and DefT.BaseType = 1 where PerC.IsDeleted != 1 
			and PerC.BirthDateIsUndefined = 0 and PerC.DeathDate is null and PerC.UniqueId not in 
			(select PrReg.DonorId from DonationProcessRegistry PrReg where PrReg.RegDate = cast(getdate() as date) and PrReg.CurrentState != 6) 
			and PerC.UniqueId not in (select Don.DonorId from Donations Don where cast(Don.DonationDate as date) = cast(getdate() as date)) 
			and PerC.UniqueId not in (select Def.DonorId from Deferrals Def join ref.DeferralTypes DefT on Def.DeferralTypeId = DefT.UniqueId 
			where ((DefT.BaseType = 2 and Def.RevokeDate is null) or (DefT.BaseType = 3 
			and (cast(Def.StopDate as date) >= cast(getdate() as date) or Def.StopDate is null)))) and PerC.Gender in (1,2) 
			and PerC.IdentityDocId is not null and ((PerC.RegAddressId is not null and (PerC.RegAddressIsInactive = 0 
			or PerC.RegAddressIsInactive is null)) or (PerC.FactAddressId is not null and (PerC.FactAddressIsInactive = 0 
			or PerC.FactAddressIsInactive is null)) or (PerC.TempAddressId is not null and (PerC.TempAddressIsInactive = 0 
			or PerC.TempAddressIsInactive is null))) and DonTP.IsActive = 1 and DonT.DonationParams not in (4, 5, 6, 7, 12, 15) 
			and (cast(AppD.NextDonationDate as date) <= cast(getdate() as date) or AppD.NextDonationDate is null) and DonT.ChargeType = 0 
			and PerC.UniqueId not in (select Don.DonorId from Donations Don where Don.ResultStatus != 5)'''
			)

		donorid = str(full_query[0][0])

		expected_message = str(full_query[0][1])

		main_page.open()

		aistium.fill(donorid, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC left join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and (PerC.UniqueId = '"+donorid+"' or IDoc.Number = '"+donorid+"')) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		main_page.ndp_get_grid_values('№', ind, 'click')

		main_page.loading_is_completed()

		aistium.click_on(elements=main_page.process_state_button)

		main_page.loading_is_completed()

		aistium.click_on(locators_list=locators, element_name='confirm_popup_no_btn')

		assert aistium.element_is_on_the_page(locators_list=locators, element_name='confirm_popup') == False

		assert len(sql_query("select PrReg.Id from DonationProcessRegistry PrReg, ref.SystemSettings SysSet where PrReg.DonorId = '"+donorid+"' and PrReg.OrgId = SysSet.CurrentOrganizationId and PrReg.RegDate = cast(getdate() as date) and PrReg.CurrentState = 1 and PrReg.MobileTeamSessionId is null")) == 0

	@allure.step('3. МД. Регистратура. Направление донора. Подтверждение направления при появлении предупреждающего сообщения')
	def test_donors_direction_warning_messages_с(self):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		change_donor_settings(CheckDonorInFicWhileDirection='false', 
			CheckFiasAddressForDonor='true', 
			CheckIncompleteAnalysis= 'true', 
			AlwaysShowEpidAddress='true')

		change_sticker_settings(PrintRunner='false')

		full_query = sql_query(
			'''select top(1) PerC.UniqueId Ent, 'Донор отведён (тип отвода: Абсолютный).' 
			OR1 from PersonCards PerC join AppointedDonationTypes AppD on PerC.UniqueId = AppD.DonorId 
			join (select AppD.DonorId, max(AppD.DonationDate) MaxDate from AppointedDonationTypes AppD group by AppD.DonorId) 
			Main on AppD.DonorId = Main.DonorId and AppD.DonationDate = Main.MaxDate 
			join ref.DonationTypeParams DonTP on AppD.DonationTypeId = DonTP.DonationTypeId 
			join ref.DonationTypes DonT on AppD.DonationTypeId = DonT.UniqueId 
			join Deferrals Def on PerC.UniqueId = Def.DonorId and Def.RevokeDate is null 
			join ref.DeferralTypes DefT on Def.DeferralTypeId = DefT.UniqueId and DefT.BaseType = 1 where PerC.IsDeleted != 1 
			and PerC.BirthDateIsUndefined = 0 and PerC.DeathDate is null and PerC.UniqueId not in 
			(select PrReg.DonorId from DonationProcessRegistry PrReg where PrReg.RegDate = cast(getdate() as date) and PrReg.CurrentState != 6) 
			and PerC.UniqueId not in (select Don.DonorId from Donations Don where cast(Don.DonationDate as date) = cast(getdate() as date)) 
			and PerC.UniqueId not in (select Def.DonorId from Deferrals Def join ref.DeferralTypes DefT on Def.DeferralTypeId = DefT.UniqueId 
			where ((DefT.BaseType = 2 and Def.RevokeDate is null) or (DefT.BaseType = 3 
			and (cast(Def.StopDate as date) >= cast(getdate() as date) or Def.StopDate is null)))) and PerC.Gender in (1,2) 
			and PerC.IdentityDocId is not null and ((PerC.RegAddressId is not null and (PerC.RegAddressIsInactive = 0 
			or PerC.RegAddressIsInactive is null)) or (PerC.FactAddressId is not null and (PerC.FactAddressIsInactive = 0 
			or PerC.FactAddressIsInactive is null)) or (PerC.TempAddressId is not null and (PerC.TempAddressIsInactive = 0 
			or PerC.TempAddressIsInactive is null))) and DonTP.IsActive = 1 and DonT.DonationParams not in (4, 5, 6, 7, 12, 15) 
			and (cast(AppD.NextDonationDate as date) <= cast(getdate() as date) or AppD.NextDonationDate is null) and DonT.ChargeType = 0 
			and PerC.UniqueId not in (select Don.DonorId from Donations Don where Don.ResultStatus != 5)'''
			)

		donorid = str(full_query[0][0])

		expected_message = str(full_query[0][1])

		main_page.open()

		aistium.fill(donorid, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC left join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and (PerC.UniqueId = '"+donorid+"' or IDoc.Number = '"+donorid+"')) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		main_page.ndp_get_grid_values('№', ind, 'click')

		main_page.loading_is_completed()

		aistium.click_on(elements=main_page.process_state_button)

		main_page.loading_is_completed()

		aistium.click_on(locators_list=locators, element_name='confirm_popup_yes_btn')

		main_page.loading_is_completed()

		assert aistium.get_text(main_page.process_state_button) == 'Вернуть'

		assert len(sql_query("select PrReg.Id from DonationProcessRegistry PrReg, ref.SystemSettings SysSet where PrReg.DonorId = '"+donorid+"' and PrReg.OrgId = SysSet.CurrentOrganizationId and PrReg.RegDate = cast(getdate() as date) and PrReg.CurrentState = 1 and PrReg.MobileTeamSessionId is null")[0]) > 0

		payload = {'Login':BaseTest.login, 'Password':BaseTest.password}

		url = BaseTest.stand+'/Auth/LogOn'

		s = requests.Session()

		s.post(url, data=payload)

		body = {'donorId': donorid}

		s.post('http://10.32.200.142/Common/IsExaminationsSaved', data=body)

		body = {'id': donorid, 'confirmed': 'true', 'sessionId': '', 'reason': 'автотест', 'fromQuickRegistryForm': 'false', 'recipientId': '', 'donationTypeId': '', 'noteType': 'Registration'}

		s.post(BaseTest.stand+'/Common/StepBackwardDonationProcess', data=body)

if __name__ == "__main__":
	pytest.main()