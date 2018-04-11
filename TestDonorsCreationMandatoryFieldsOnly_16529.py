# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from locators import donors_registry_locators as locators
from base import BaseTest, Driver
from additional_functions import get_data
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-16529')
class TestDonorsCreationMandatoryFieldsOnly(BaseTest):

	@allure.step('Добавление донора с заполнением только обязательных полей')
	@pytest.mark.parametrize('lastname, firstname, birthdate, gender, document_serie, document_number, address', get_data('data_test_donors_creation_mandatory_fields_only.csv'))
	def test_donors_creation_mandatory_fields_only(self, lastname, firstname, birthdate, gender, document_serie, document_number, address):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()
		
		region = address.split(':')[0]
		city = address.split(':')[1]
		street = address.split(':')[2]
		house = address.split(':')[3]

		full_address = [region, city, street, 'д.'+house]
		for item in full_address:
			if item == '':
				del(full_address[full_address.index(item)])

		full_name = lastname + ' ' + firstname

		main_page.newdonor_click()
		
		main_page.ndp_filling_first_page(lastname, firstname, '', birthdate, document_serie, document_number)
		if gender == 'Женский':
			main_page.select_gender('female')
			saved_gender = 'Ж'
		elif gender == 'Мужской':
			main_page.select_gender('male')
			saved_gender = 'М'

		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()
		
		main_page.if_donor_is_in_local_cabinet()

		main_page.ndp_filling_region(region)

		if city != '':
			main_page.ndp_filling_city(city)

		main_page.ndp_filling_street(street)

		aistium.fill(house, elements=main_page.reg_fias_address_house)
		
		main_page.ndp_save_new_donor('success')

		assert aistium.get_text(elements=main_page.fio_minicard) == full_name

		#assert main_page.ndp_get_grid_values('ФИО', 1) == full_name

		assert aistium.get_value(locators_list=locators, element_name='quick_search_field') == full_name + ' '

		assert main_page.get_gender_from_minicard() == saved_gender

		assert main_page.get_address_from_minicard() == full_address
		
		assert main_page.get_birthdate_from_minicard() == birthdate

		assert main_page.get_document_serie_and_number() == document_serie + ' ' + document_number

if __name__ == "__main__":
	pytest.main()