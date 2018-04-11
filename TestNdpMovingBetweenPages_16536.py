# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from locators import donors_registry_locators as locators
from base import BaseTest, Driver
from additional_functions import get_data, sql_query
from donors_registry import DonorsModuleRegistryPage
from donors_card_title import DonorsCardTitle
from system_settings.general_settings import change_general_settings

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-16536')
class TestNdpMovingBetweenPages(BaseTest):

	@allure.step('1. Перемещение между страницами формы добавления донора при заполнении только обязательных полей; один возврат; без изменения значений. ')
	def test_ndp_moving_between_pages_first_step(self):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		main_page.open()

		main_page.newdonor_click()
		
		main_page.ndp_filling_first_page('Сидоров', 'Кирилл', '', '01.06.1980', '8910', '650231')

		main_page.select_gender('male')

		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()
		
		main_page.if_donor_is_in_local_cabinet()

		main_page.ndp_second_page_loaded()

		main_page.ndp_filling_region('Москва г')

		main_page.ndp_filling_street('Перовская ул')

		aistium.fill('46', elements=main_page.reg_fias_address_house)

		aistium.click_on(elements=main_page.previous_step_ndp)

		main_page.ndp_first_page_check_values_of_mandatory_fields('Сидоров', 'Кирилл', '01.06.1980', '8910', '650231')

		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()

		main_page.if_donor_is_in_local_cabinet()

		main_page.ndp_second_page_loaded()

		main_page.ndp_second_page_check_values_of_mandatory_fields() == ('Москва г', '', 'Перовская ул', '46')
		
		main_page.ndp_save_new_donor('success')

		main_page.loading_is_completed()

		assert aistium.get_text(elements=main_page.fio_minicard) == 'Сидоров Кирилл'

		assert main_page.get_gender_from_minicard() == 'М'
		
		assert main_page.get_birthdate_from_minicard() == '01.06.1980'

		assert main_page.get_document_serie_and_number() == '8910' + ' ' + '650231'

		assert main_page.get_accurate_address() == 'Москва г, Перовская ул, д.46' 

	@allure.step('2. Перемещение между страницами формы добавления донора при заполнении всех полей; два возврата; с изменением значений.')
	def test_ndp_moving_between_pages_second_step(self):
		main_page = DonorsModuleRegistryPage()

		main_page.clear_localstorage()

		change_general_settings(WorkWithSocialStatus='true')

		main_page.newdonor_click()
		
		main_page.ndp_filling_first_page('Сидоров', 'Иван', 'Петрович', '15.06.1980', '8933', '650245')

		main_page.select_gender('male')

		main_page.filling_identity_document_issue_date('20.11.2000')

		aistium.fill('А', elements=main_page.identity_document_issued_by)

		aistium.fill('19133561060', elements=main_page.snils_field)

		main_page.ndp_filling_birth_place('Б')

		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()
		
		main_page.if_donor_is_in_local_cabinet()

		main_page.ndp_second_page_loaded()

		main_page.ndp_filling_region('Москва г')

		main_page.ndp_filling_street('Перовская ул')

		aistium.fill('52', elements=main_page.reg_fias_address_house)

		main_page.ndp_filling_contacts('123456789', '123456789', 'gh@mail.ru')

		aistium.fill('Работа', elements=main_page.ndp_job_place_field)

		aistium.fill('К', elements=main_page.job_position)

		aistium.fill('Рабочие', main_page.social_status_field)

		main_page.ndp_filling_deferral(str(sql_query("select top(1) DefT.Code+' '+DefT.Name Otvod from ref.DeferralTypes DefT join ref.DeferralTypeParams DefTP on DefT.UniqueId = DefTP.DeferralTypeId where DefTP.IsActive = 1 and DefT.BaseType = 1"))[3:-5])

		main_page.ndp_filling_donation_type(str(sql_query("select top(1) DonT.Code+' '+DonT.Name  from ref.DonationTypes DonT join ref.DonationTypeParams DonTP on DonT.UniqueId = DonTP.DonationTypeId where DonTP.IsActive = 1 and DonT.DonationParams not like '%4%' and DonT.ComponentType = 1"))[3:-5])

		aistium.click_on(elements=main_page.previous_step_ndp)

		main_page.ndp_first_page_clear()

		main_page.ndp_select_document_type('Загранпаспорт РФ')

		main_page.select_gender('female')

		main_page.ndp_filling_first_page('Сидорова', 'Иванка', 'Петровна', '15.08.1980', '89', '6502455')

		main_page.filling_identity_document_issue_date('20.11.2002')

		aistium.fill('Б', elements=main_page.identity_document_issued_by)

		aistium.fill('24559224384', elements=main_page.snils_field)

		main_page.ndp_filling_birth_place('3')

		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()
		
		main_page.if_donor_is_in_local_cabinet()

		main_page.ndp_second_page_loaded()

		main_page.ndp_fias_address_clear()

		main_page.ndp_contacts_clear()

		main_page.ndp_job_or_study_place_clear()

		aistium.click_on(elements=main_page.ndp_deferral_clear_button)

		main_page.ndp_donation_type_clear()

		main_page.ndp_filling_region('Москва г')

		main_page.ndp_filling_street('Кленовый б-р')

		aistium.fill('28', elements=main_page.reg_fias_address_house)

		main_page.ndp_filling_contacts('123456785', '123456783', 'gh@mail.com')

		main_page.filling_job_or_study_place('Работа 2', 'К', 'Служащие')

		main_page.ndp_filling_deferral(str(sql_query("select top(1) DefT.Code+' '+DefT.Name Otvod from ref.DeferralTypes DefT join ref.DeferralTypeParams DefTP on DefT.UniqueId = DefTP.DeferralTypeId where DefTP.IsActive = 1 and DefT.BaseType = 2"))[3:-5])

		main_page.ndp_filling_donation_type(str(sql_query("select top(1) DonT.Code+' '+DonT.Name from ref.DonationTypes DonT join ref.DonationTypeParams DonTP on DonT.UniqueId = DonTP.DonationTypeId where DonTP.IsActive = 1 and DonT.DonationParams not like '%4%' and DonT.ComponentType = 2"))[3:-5])

		aistium.click_on(elements=main_page.previous_step_ndp)

		main_page.ndp_first_page_check_values_of_mandatory_fields('Сидорова', 'Иванка', '15.08.1980', '89', '6502455')

		aistium.get_value(locators_list=locators, element_name='middle_name_field_ndp') == 'Петровна'

		aistium.get_value(locators_list=locators, element_name='identity_document_issue_date') == '20.11.2002'

		aistium.get_value(locators_list=locators, element_name='identity_document_issued_by') == 'Б'

		aistium.get_value(locators_list=locators, element_name='ndp_birth_place') == '3'

		aistium.get_value(locators_list=locators, element_name='snils_field') == '24559224384'

		main_page.identity_document_issued_by_clear()

		aistium.fill('Бв', elements=main_page.identity_document_issued_by)

		aistium.click_on(elements=main_page.next_step_ndp)

		main_page.loading_is_completed()

		main_page.if_donor_is_in_local_cabinet()

		main_page.ndp_second_page_loaded()

		main_page.ndp_get_contacts_values() == ('123456785', '123456783', 'gh@mail.com')

		main_page.ndp_second_page_check_values_of_mandatory_fields() == ('Москва г', '', 'Кленовый б-р', '28')

		main_page.ndp_get_job_information() == ('Работа 2', 'К', 'Служащие')

		assert aistium.get_value(locators_list=locators, element_name='ndp_deferral_field') == str(sql_query("select top(1) DefT.Code+' '+DefT.Name Otvod from ref.DeferralTypes DefT join ref.DeferralTypeParams DefTP on DefT.UniqueId = DefTP.DeferralTypeId where DefTP.IsActive = 1 and DefT.BaseType = 2"))[3:-5]

		main_page.ndp_get_donation_type() == str(sql_query("select top(1) DonT.Code+' '+DonT.Name from ref.DonationTypes DonT join ref.DonationTypeParams DonTP on DonT.UniqueId = DonTP.DonationTypeId where DonTP.IsActive = 1 and DonT.DonationParams not like '%4%' and DonT.ComponentType = 2"))[3:-5]

		main_page.ndp_phone_clear()

		main_page.ndp_filling_contacts('', '123456788', '')

		main_page.ndp_save_new_donor('success')

		assert aistium.get_text(elements=main_page.fio_minicard) == 'Сидорова Иванка Петровна'

		assert aistium.get_text(elements=main_page.minicard_phone) == '123456788'

		grid_donor_id = main_page.ndp_get_grid_values('№', 'active_cell')

		donors_card_title_page = DonorsCardTitle(grid_donor_id)

		donors_card_title_page.open()

		donors_card_title_page.issued_by() == 'Бв 20.11.2002'

if __name__ == "__main__":
	pytest.main()