# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import sql_query
from system_settings.donor_settings import change_donor_settings
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6073')
class TestNdpCheckingDonorByFic(BaseTest):

	@allure.step('1. Отображение региона карты, если передано значение длиной 5 знаков')
	def test_ndp_checking_donor_by_fic_a(self):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		change_donor_settings(UseFicDonorSearch='true')
			
		main_page.open()
			
		query = sql_query(
			'''select top (1) PerC.IdentityDocSerie, PerC.IdentityDocNumber, '0'+substring(ltrim(PerC.RegNodeId), 1, 1) as OR1 from aistdb_fic.dbo.PersonCards PerC where len(PerC.RegNodeId) = 5 
			and PerC.RegNodeId not like '0%'
			and len(PerC.LastName) > 0
			and len(PerC.FirstName) > 0
			and len(PerC.MiddleName) > 0
			and len(PerC.IdentityDocType) > 0
			and len(PerC.IdentityDocSerie) > 0''',
			stand='DRIVER={SQL Server};SERVER=10.36.200.79;DATABASE=aistdb_fic;UID=sa;PWD=Mos111222'
			)

		document_serie = query[0][0]

		document_number = query[0][1]

		expected = query[0][2]
	
		main_page.newdonor_click()
					
		main_page.ndp_filling_first_page("Сидоров", "Кирилл", '', "01.06.1980", document_serie, document_number)
				
		main_page.select_gender('male')
		
		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()
					
		main_page.if_donor_is_in_local_cabinet()
			
		main_page. #*#*#*#*#*#*#*#**#*#*#*#*#*#*#**#*#*#*#**#*#*#*#*#*#*#*#*#*#**#*#*#*#*#*#*#*#*#*

	@allure.step('2. Отображение региона карты, если передано значение длиной, не равной 5 знакам')
	def test_ndp_checking_donor_by_fic_b(self):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		change_donor_settings(UseFicDonorSearch='true')
			
		main_page.open()

		query = sql_query(
			'''select top (1) PerC.IdentityDocSerie, PerC.IdentityDocNumber, substring(ltrim(PerC.RegNodeId), 1, 2) as OR1 
			from aistdb_fic.dbo.PersonCards PerC
			where len(PerC.RegNodeId) != 5
			and len(PerC.LastName) > 0
			and len(PerC.FirstName) > 0
			and len(PerC.MiddleName) > 0
			and len(PerC.IdentityDocType) > 0
			and len(PerC.IdentityDocSerie) > 0''',
			stand='DRIVER={SQL Server};SERVER=10.36.200.79;DATABASE=aistdb_fic;UID=sa;PWD=Mos111222'
			)

		document_serie = query[0][0]

		document_number = query[0][1]

		expected = query[0][2]
	
		main_page.newdonor_click()
					
		main_page.ndp_filling_first_page("Сидоров", "Кирилл", '', "01.06.1980", document_serie, document_number)
				
		main_page.select_gender('male')			
		
		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()
					
		main_page.if_donor_is_in_local_cabinet()
			
		main_page.