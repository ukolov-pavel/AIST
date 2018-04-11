# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from locators import donors_registry_locators as locators
from base import BaseTest, Driver
from additional_functions import get_data
from donors_registry import DonorsModuleRegistryPage
from donors_card_title import DonorsCardTitle
from system_settings.general_settings import change_general_settings


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-16532')
class TestDonorsCreationAllFields(BaseTest):

	@allure.step('Добавление донора с заполнением всех полей, проверка на верное сохранение введённых данных')
	def test_donors_creation_all_fields(self):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		change_general_settings(WorkWithSocialStatus='true')

		main_page.open()

		main_page.newdonor_click()
		
		main_page.ndp_filling_first_page('Петров', 'Константин', 'Семенович', '02.03.1980', '9360', '206519') #mandatory fields only

		main_page.select_gender('male')

		if main_page.get_is_agree_persional_data_processing_value() != 'true':
			aistium.click_on(elements=main_page.is_agree_persional_data_processing)

		if main_page.get_is_message_agree_value() != 'true':
			aistium.click_on(elements=main_page.is_message_agree)

		main_page.filling_identity_document_issue_date('10.03.2000')

		aistium.fill('Учреждение выдачи паспортов', elements=main_page.identity_document_issued_by)

		aistium.fill('14805696690', elements=main_page.snils_field)

		main_page.ndp_filling_birth_place('г. Москва')

		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()
		
		main_page.if_donor_is_in_local_cabinet()

		main_page.ndp_second_page_loaded()

		main_page.ndp_filling_region('Москва г')

		main_page.ndp_filling_street('Перова Поля 3-й проезд')

		aistium.fill('21', elements=main_page.reg_fias_address_house)

		main_page.ndp_filling_building('366')

		main_page.ndp_filling_structure('16')

		main_page.ndp_filling_flat('80')

		main_page.ndp_filling_contacts('9252451340', '4956280991', 'pks-1980@mail.ru')

		aistium.fill('ООО Работа', elements=main_page.ndp_job_place_field)

		aistium.fill('Специалист', elements=main_page.job_position)
			
		aistium.fill('Безработные, в т.ч. домохозяйки', elements=main_page.social_status_field)

		main_page.ndp_filling_deferral('А Прием алкоголя')

		main_page.ndp_filling_donation_type('110 Безв. доноp кpови')
		
		main_page.ndp_save_new_donor('success')

		assert aistium.get_text(elements=main_page.fio_minicard) == 'Петров Константин Семенович'

		assert main_page.ndp_get_grid_values('ФИО', 1) == 'Петров Константин Семенович'

		assert aistium.get_value(locators_list=locators, element_name='quick_search_field') == 'Петров Константин Семенович'

		assert main_page.get_gender_from_minicard() == 'М'
		
		assert main_page.get_birthdate_from_minicard() == '02.03.1980'

		assert main_page.get_document_serie_and_number() == '9360' + ' ' + '206519'

		assert aistium.get_text(elements=main_page.deferral_from_minicard) == 'Прием алкоголя'

		assert main_page.get_donation_type_value_from_minicard() == '110 Безв. доноp кpови'

		assert main_page.get_email_from_minicard() == 'pks-1980@mail.ru'

		assert aistium.get_text(elements=main_page.minicard_mobile_phone) == '+7 925 245 13 40'

		assert aistium.get_text(elements=main_page.minicard_phone) == '+7 4956280991'

		assert main_page.get_accurate_address() == '111141, Москва г, Перова Поля 3-й проезд, д.21, корп.366, стр.16, кв. 80'

		grid_donor_id = main_page.ndp_get_grid_values('№', 'active_cell')

		donors_card_title_page = DonorsCardTitle(grid_donor_id)

		donors_card_title_page.open()

		#assert donors_card_title_page.job_place() == 'ООО Работа' '''https://aj.srvdev.ru/browse/AIST-16521'''

		assert donors_card_title_page.job() == 'Специалист'

		assert donors_card_title_page.social_status() == 'Статус: ' + 'Безработные, в т.ч. домохозяйки'

if __name__ == "__main__":
	pytest.main()