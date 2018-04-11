# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import sql_query, get_data
from donors_registry import DonorsModuleRegistryPage
from system_settings.donor_settings import change_donor_settings

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6074')
class TestNdpCheckingDonorByFicFullname(BaseTest):

	@allure.step('1. Проверка нового донора по ФИЦ, отображение поля ФИО в гриде')
	@pytest.mark.parametrize('query, row_index', get_data('data_test_ndp_checking_donor_by_fic_fullname_a.csv'))
	def test_ndp_checking_donor_by_fic_fullname_a(self, query, row_index):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		change_donor_settings(UseFicDonorSearch='true')
			
		main_page.open()
			
		query = sql_query(query, stand="DRIVER={SQL Server};SERVER=10.36.200.79;DATABASE=aistdb_fic;UID=sa;PWD=Mos111222")

		document_serie = query[0][0]

		document_number = query[0][1]

		expected = query[0][2]
	
		main_page.newdonor_click()
					
		main_page.ndp_filling_first_page("Сидоров", "Кирилл", '', "01.06.1980", document_serie, document_number)
				
		main_page.select_gender('male')
			
		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()
					
		main_page.if_donor_is_in_local_cabinet()
			
		main_page.ndp_results_by_fic_is_on_the_page()

		assert main_page.ndp_results_by_fic_get_grid_values('ФИО', int(row_index)) == expected

	@allure.step('2. Проверка нового донора по ФИЦ, отображение поля ФИО в гриде')
	def test_ndp_checking_donor_by_fic_fullname_b(self):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		change_donor_settings(UseFicDonorSearch='true')
			
		main_page.open()
			
		query = sql_query('''select top (1) PerC.IdentityDocSerie, PerC.IdentityDocNumber, PerC.LastName + ' ' + PerC.FirstName + ' ' + PerC.MiddleName OR1
			from aistdb_fic.dbo.PersonCards PerC
			where len(PerC.LastName) > 0
			and len(PerC.FirstName) > 0
			and len(PerC.MiddleName) > 0
			and len(PerC.IdentityDocSerie) > 0
			and len(PerC.IdentityDocNumber) > 0''', 
			stand="DRIVER={SQL Server};SERVER=10.36.200.79;DATABASE=aistdb_fic;UID=sa;PWD=Mos111222")

		document_serie = query[0][0]

		document_number = query[0][1]

		expected = query[0][2]
	
		main_page.newdonor_click()
					
		main_page.ndp_filling_first_page("Сидоров", "Кирилл", '', "01.06.1980", document_serie, document_number)
				
		main_page.select_gender('male')
			
		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()
					
		main_page.if_donor_is_in_local_cabinet()
			
		main_page.ndp_results_by_fic_is_on_the_page()

		main_page.ndp_results_by_fic_get_grid_values('ФИО', 0, mode='click')

		Driver.get().switch_to.window(Driver.get().window_handles[1])

		assert main_page.query_to_fic_get_fullname() == expected

if __name__ == "__main__":
	pytest.main()