# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import sql_query, get_data
from system_settings.donor_settings import change_donor_settings
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6073')
class TestNdpCheckingDonorByFicRC(BaseTest):

	@allure.step('Проверка нового донора по ФИЦ, отображение поля РК в гриде')
	@pytest.mark.parametrize('query, st, row_index', get_data('data_test_ndp_checking_donor_by_fic_rc_a.csv'))
	def test_ndp_checking_donor_by_fic_rc_a(self, query, st, row_index):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		change_donor_settings(UseFicDonorSearch='true')
			
		main_page.open()
			
		query = sql_query(query, stand=st)

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

		assert main_page.ndp_results_by_fic_get_grid_values('РК', int(row_index)) == expected

if __name__ == "__main__":
	pytest.main()