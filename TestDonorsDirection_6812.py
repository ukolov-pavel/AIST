# -*- coding: utf-8 -*-
import pytest, allure, selenium, requests, aistium
from base import BaseTest, Driver
from additional_functions import sql_query, get_data
from donors_registry import DonorsModuleRegistryPage
from locators import donors_registry_locators as locators
from system_settings.donor_settings import change_donor_settings
from system_settings.donations_settings import change_donations_settings
from system_settings.product_settings import change_product_settings
from system_settings.sticker_settings import change_sticker_settings


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6812')
class TestDonorsDirection(BaseTest):

	@allure.step('1. МД. Регистратура. Направление донора.')
	@pytest.mark.parametrize('query, test_data_set_number', get_data('data_test_donors_direction_a.csv'))
	def test_donors_direction_a(self, query, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		change_donor_settings(CheckDonorInFicWhileDirection='false', 
			CheckFiasAddressForDonor='false', 
			CheckIncompleteAnalysis= 'false', 
			AlwaysShowEpidAddress='false', 
			NotifyRegistrarForHonorableDonor='false', 
			CheckAntierythrocyteDonationOrExamination='false')

		change_product_settings(AutoDonorAutomaticApprobationProducts='true')

		change_sticker_settings(PrintRunner='false')

		full_query = sql_query(query)

		donorid = str(full_query[0][0])

		main_page.open()

		aistium.fill(donorid, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC left join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and (PerC.UniqueId = '"+donorid+"' or IDoc.Number = '"+donorid+"')) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		main_page.ndp_get_grid_values('№', ind, 'click')

		main_page.loading_is_completed()

		aistium.click_on(elements=main_page.process_state_button)

		main_page.loading_is_completed()

		assert aistium.get_text(elements=main_page.process_state_button) == 'Вернуть'

		assert len(sql_query("select PrReg.Id from DonationProcessRegistry PrReg, ref.SystemSettings SysSet where PrReg.DonorId = '"+donorid+"' and PrReg.OrgId = SysSet.CurrentOrganizationId and PrReg.RegDate = cast(getdate() as date) and PrReg.CurrentState = 1 and PrReg.MobileTeamSessionId is null")[0]) > 0

		payload = {'Login':BaseTest.login, 'Password':BaseTest.password}

		url = BaseTest.stand+'/Auth/LogOn'

		s = requests.Session()

		s.post(url, data=payload)

		body = {'donorId': donorid}

		s.post('http://10.32.200.142/Common/IsExaminationsSaved', data=body)

		body = {'id': donorid, 'confirmed': 'true', 'sessionId': '', 'reason': 'автотест', 'fromQuickRegistryForm': 'false', 'recipientId': '', 'donationTypeId': '', 'noteType': 'Registration'}

		s.post(BaseTest.stand+'/Common/StepBackwardDonationProcess', data=body)

	@allure.step('2. МД. Регистратура. Направление донора.')
	@pytest.mark.parametrize('query, test_data_set_number', get_data('data_test_donors_direction_b.csv'))
	def test_donors_direction_b(self, query, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		change_donor_settings(CheckDonorInFicWhileDirection='false', 
			CheckFiasAddressForDonor='false', 
			CheckIncompleteAnalysis= 'false', 
			AlwaysShowEpidAddress='false', 
			NotifyRegistrarForHonorableDonor='false', 
			CheckAntierythrocyteDonationOrExamination='false')

		change_donations_settings(MaxYearBloodDonationCountMale='3', 
			MaxYearBloodDonationCountFemale='3', 
			MaxYearPlasmaVolumeMale='2',
			MaxYearPlasmaVolumeFemale='2',
			MaxYearPlasmapheresisCount='4',
			MaxYearCytapheresisCount='4')

		change_product_settings(AutoDonorAutomaticApprobationProducts='true')

		change_sticker_settings(PrintRunner='false')

		full_query = sql_query(query)

		donorid = str(full_query[0][0])

		main_page.open()

		aistium.fill(donorid, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC left join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and (PerC.UniqueId = '"+donorid+"' or IDoc.Number = '"+donorid+"')) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		main_page.ndp_get_grid_values('№', ind, 'click')

		main_page.loading_is_completed()

		aistium.click_on(elements=main_page.process_state_button)

		main_page.loading_is_completed()

		assert aistium.get_text(elements=main_page.process_state_button) == 'Вернуть'

		assert len(sql_query("select PrReg.Id from DonationProcessRegistry PrReg, ref.SystemSettings SysSet where PrReg.DonorId = '"+donorid+"' and PrReg.OrgId = SysSet.CurrentOrganizationId and PrReg.RegDate = cast(getdate() as date) and PrReg.CurrentState = 1 and PrReg.MobileTeamSessionId is null")[0]) > 0

		payload = {'Login':BaseTest.login, 'Password':BaseTest.password}

		url = BaseTest.stand+'/Auth/LogOn'

		s = requests.Session()

		s.post(url, data=payload)

		body = {'donorId': donorid}

		s.post('http://10.32.200.142/Common/IsExaminationsSaved', data=body)

		body = {'id': donorid, 'confirmed': 'true', 'sessionId': '', 'reason': 'автотест', 'fromQuickRegistryForm': 'false', 'recipientId': '', 'donationTypeId': '', 'noteType': 'Registration'}

		s.post(BaseTest.stand+'/Common/StepBackwardDonationProcess', data=body)

	@allure.step('3. МД. Регистратура. Направление донора.')
	@pytest.mark.parametrize('query, test_data_set_number', get_data('data_test_donors_direction_c.csv'))
	def test_donors_direction_с(self, query, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		change_donor_settings(CheckAntierythrocyteDonationOrExamination='true',
			CheckDonorInFicWhileDirection='false', 
			CheckFiasAddressForDonor='false', 
			CheckIncompleteAnalysis= 'false', 
			AlwaysShowEpidAddress='false', 
			NotifyRegistrarForHonorableDonor='false')

		change_product_settings(AutoDonorAutomaticApprobationProducts='true')

		change_sticker_settings(PrintRunner='false')

		full_query = sql_query(query)

		donorid = str(full_query[0][0])

		main_page.open()

		aistium.fill(donorid, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC left join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and (PerC.UniqueId = '"+donorid+"' or IDoc.Number = '"+donorid+"')) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		main_page.ndp_get_grid_values('№', ind, 'click')

		main_page.loading_is_completed()

		aistium.click_on(elements=main_page.process_state_button)

		main_page.loading_is_completed()

		assert aistium.get_text(elements=main_page.process_state_button) == 'Вернуть'

		assert len(sql_query("select PrReg.Id from DonationProcessRegistry PrReg, ref.SystemSettings SysSet where PrReg.DonorId = '"+donorid+"' and PrReg.OrgId = SysSet.CurrentOrganizationId and PrReg.RegDate = cast(getdate() as date) and PrReg.CurrentState = 1 and PrReg.MobileTeamSessionId is null")[0]) > 0

		payload = {'Login':BaseTest.login, 'Password':BaseTest.password}

		url = BaseTest.stand+'/Auth/LogOn'

		s = requests.Session()

		s.post(url, data=payload)

		body = {'donorId': donorid}

		s.post('http://10.32.200.142/Common/IsExaminationsSaved', data=body)

		body = {'id': donorid, 'confirmed': 'true', 'sessionId': '', 'reason': 'автотест', 'fromQuickRegistryForm': 'false', 'recipientId': '', 'donationTypeId': '', 'noteType': 'Registration'}

		s.post(BaseTest.stand+'/Common/StepBackwardDonationProcess', data=body)

	@allure.step('4. МД. Регистратура. Направление донора.')
	@pytest.mark.parametrize('query, test_data_set_number', get_data('data_test_donors_direction_d.csv'))
	def test_donors_direction_d(self, query, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		change_donor_settings(CheckDonorInFicWhileDirection='false', 
			CheckFiasAddressForDonor='true', 
			CheckIncompleteAnalysis= 'false', 
			AlwaysShowEpidAddress='false', 
			NotifyRegistrarForHonorableDonor='false', 
			CheckAntierythrocyteDonationOrExamination='false')

		change_product_settings(AutoDonorAutomaticApprobationProducts='true')

		change_sticker_settings(PrintRunner='false')

		full_query = sql_query(query)

		donorid = str(full_query[0][0])

		main_page.open()

		aistium.fill(donorid, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC left join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and (PerC.UniqueId = '"+donorid+"' or IDoc.Number = '"+donorid+"')) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		main_page.ndp_get_grid_values('№', ind, 'click')

		main_page.loading_is_completed()

		aistium.click_on(elements=main_page.process_state_button)

		main_page.loading_is_completed()

		assert aistium.get_text(elements=main_page.process_state_button) == 'Вернуть'

		assert len(sql_query("select PrReg.Id from DonationProcessRegistry PrReg, ref.SystemSettings SysSet where PrReg.DonorId = '"+donorid+"' and PrReg.OrgId = SysSet.CurrentOrganizationId and PrReg.RegDate = cast(getdate() as date) and PrReg.CurrentState = 1 and PrReg.MobileTeamSessionId is null")[0]) > 0

		payload = {'Login':BaseTest.login, 'Password':BaseTest.password}

		url = BaseTest.stand+'/Auth/LogOn'

		s = requests.Session()

		s.post(url, data=payload)

		body = {'donorId': donorid}

		s.post('http://10.32.200.142/Common/IsExaminationsSaved', data=body)

		body = {'id': donorid, 'confirmed': 'true', 'sessionId': '', 'reason': 'автотест', 'fromQuickRegistryForm': 'false', 'recipientId': '', 'donationTypeId': '', 'noteType': 'Registration'}

		s.post(BaseTest.stand+'/Common/StepBackwardDonationProcess', data=body)

	@allure.step('5. МД. Регистратура. Направление донора.')
	@pytest.mark.parametrize('query, test_data_set_number', get_data('data_test_donors_direction_e.csv'))
	def test_donors_direction_e(self, query, test_data_set_number):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		donations_counts = {
		'HonorableDonorSettings[0].DonationsCount': '10',
		'HonorableDonorSettings[0].BloodAndComponentsCount': '5',
		'HonorableDonorSettings[0].PlasmaCount': '5',
		'HonorableDonorSettings[1].DonationsCount': '999',
		'HonorableDonorSettings[1].BloodAndComponentsCount': '999',
		'HonorableDonorSettings[1].PlasmaCount': '0',
		'HonorableDonorSettings[2].DonationsCount': '999',
		'HonorableDonorSettings[2].BloodAndComponentsCount': '999',
		'HonorableDonorSettings[2].PlasmaCount': '0',
		'HonorableDonorSettings[3].DonationsCount': '999',
		'HonorableDonorSettings[3].BloodAndComponentsCount': '999',
		'HonorableDonorSettings[3].PlasmaCount': '0'
		}

		change_donor_settings(**{str(k): v for k, v in donations_counts.items()},
			NotifyRegistrarForHonorableDonor='true',
			CheckDonorInFicWhileDirection='false', 
			CheckFiasAddressForDonor='false', 
			CheckIncompleteAnalysis= 'false', 
			AlwaysShowEpidAddress='false', 
			CheckAntierythrocyteDonationOrExamination='false',
			)

		change_product_settings(AutoDonorAutomaticApprobationProducts='true')

		change_sticker_settings(PrintRunner='false')

		full_query = sql_query(query)

		donorid = str(full_query[0][0])

		main_page.open()

		aistium.fill(donorid, elements=main_page.quick_search_field)

		main_page.quick_search('click')

		main_page.loading_is_completed()

		ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC left join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and (PerC.UniqueId = '"+donorid+"' or IDoc.Number = '"+donorid+"')) Main where Main.UniqueId = '"+donorid+"'")[0][0]

		main_page.ndp_get_grid_values('№', ind, 'click')

		main_page.loading_is_completed()

		aistium.click_on(elements=main_page.process_state_button)

		main_page.loading_is_completed()

		assert aistium.get_text(elements=main_page.process_state_button) == 'Вернуть'

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