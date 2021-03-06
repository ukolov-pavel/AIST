# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from locators import donors_registry_locators as locators
from base import BaseTest, Driver
from additional_functions import sql_query
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6105')
class TestResetSearchFilters(BaseTest):

    @allure.step('1. МД. Регистратура. Кнопки сброса фильтров поиска недоступна без введённых параметров поиска.')
    def test_reset_search_filters_a(self):
        main_page = DonorsModuleRegistryPage()

        main_page.clear_localstorage()

        main_page.open()

        assert main_page.reset_filters_is_not_on_page() == True

    @allure.step('2. МД. Регистратура. Очищение быстрого поиска по кнопке "Снять фильтр" (ластик).')
    def test_reset_search_filters_b(self):
        main_page = DonorsModuleRegistryPage()

        query = "select top (1) PerC.UniqueId Ent from PersonCards PerC where PerC.Gender = '1' and PerC.IsDeleted != '1'"

        donorid = str(sql_query(query)[0][0])

        main_page.clear_localstorage()

        main_page.open()

        aistium.fill(donorid, elements=main_page.quick_search_field)

        main_page.quick_search('press_enter')

        main_page.loading_is_completed()

        main_page.reset_filters_click()

        main_page.loading_is_completed()

        assert main_page.number_of_entities_at_grid() == 0

    @allure.step('3. МД. Регистратура. Очищение полей расширенного поиска по кнопке "Снять фильтр" (ластик).')
    def test_reset_search_filters_c(self):
        main_page = DonorsModuleRegistryPage()

        full_query = sql_query('''
			select top (1) PerC.LastName, PerC.FirstName, PerC.MiddleName, case when PerC.Gender = '1' then 'Мужской' when PerC.Gender = '2' then 'Женский' end Gender,
			PerAd.FiasRegion, PerC.UniqueId, Don.Barcode,
			convert(varchar, dateadd(day, -1, PerC.BirthDate), 104) BirthDateS, convert(varchar, dateadd(day, 1, PerC.BirthDate), 104) BirthDatePo,
			convert(varchar, dateadd(day, -1, ApD.NextDonationDate), 104) NextDonationDateS, convert(varchar, dateadd(day, 1, ApD.NextDonationDate), 104) NextDonationDatePo,
			case
			when IDoc.DocType = 1 then 'Паспорт РФ'
			when IDoc.DocType = 2 then 'Военный билет'
			when IDoc.DocType = 3 then 'Загранпаспорт РФ'
			when IDoc.DocType = 4 then 'Паспорт СССР'
			when IDoc.DocType = 5 then 'Иные документы'
			when IDoc.DocType = 6 then 'Св-во о рождении'
			end DocType, IDoc.Serie, IDoc.Number
			from PersonCards PerC 
			join AppointedDonationTypes ApD on PerC.UniqueId = ApD.DonorId
			join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId
			join Donations Don on PerC.UniqueId = Don.DonorId
			join PersonAddresses PerAd on PerC.RegAddressId = PerAd.UniqueId
			where PerC.IsDeleted != 1 
			and PerC.LastName not like '%[a-zA-Z0-9?!_+=*\/%()}{<>^]%' and PerC.FirstName not like '%[a-zA-Z0-9?!_+=*\/%()}{<>^]%' and PerC.MiddleName not like '%[a-zA-Z0-9?!_+=*\/%()}{<>^]%'
			and PerC.Gender in ('1','2')
			and PerAd.FiasRegion is not null
			and PerAd.FiasArea is null
			and PerAd.FiasCity is not null
			and PerAd.FiasInnerArea is null
			and PerAd.FiasSettlement is null
			and PerAd.FiasStreet is not null
			and PerAd.FiasHouse is not null
			and ApD.NextDonationDate > dateadd(year, -10, getdate()) 
			and ApD.NextDonationDate < dateadd(year, 10, getdate())
			''')

        lastname, firstname, middlename, gender, region, donorid, barcode, birthdate_from, birthdate_to, next_donation_from, next_donation_to, document_type, document_serie, document_number = (
        full_query[0][0], full_query[0][1],
        full_query[0][2], full_query[0][3], full_query[0][4], full_query[0][5], full_query[0][6], full_query[0][7],
        full_query[0][8], full_query[0][9], full_query[0][10], full_query[0][11], full_query[0][12], full_query[0][13])

        main_page.clear_localstorage()

        main_page.open()

        main_page.extended_search_click('open')

        main_page.filling_fio_in_extended_search(lastname, firstname, middlename)

        main_page.filling_gender_in_extended_search(gender)

        main_page.filling_region_in_extended_search(region)

        aistium.fill(donorid, elements=main_page.extended_registry_number)

        aistium.fill(barcode, elements=main_page.extended_donation_barcode)

        aistium.fill(birthdate_from, elements=main_page.extended_birthdate_from)

        aistium.fill(birthdate_to, elements=main_page.extended_birthdate_to)

        aistium.fill(next_donation_from, elements=main_page.extended_preregistration_from)

        aistium.fill(next_donation_to, elements=main_page.extended_preregistration_to)

        main_page.filling_doc_type_in_extended_search(document_type)

        main_page.filling_doc_serie_in_extended_search(document_serie)

        main_page.filling_doc_number_in_extended_search(document_number)

        aistium.click_on(elements=main_page.extended_search_button)

        main_page.loading_is_completed()

        main_page.reset_filters_click()

        main_page.loading_is_completed()

        assert main_page.number_of_entities_at_grid() == 0

    @allure.step('4. МД. Регистратура. Очищение полей расширенного поиска при выполнении быстрого поиска.')
    def test_reset_search_filters_d(self):
        main_page = DonorsModuleRegistryPage()

        full_query = sql_query('''
			select top (1) PerC.LastName, PerC.FirstName, PerC.MiddleName, case when PerC.Gender = '1' then 'Мужской' when PerC.Gender = '2' then 'Женский' end Gender,
			PerAd.FiasRegion, PerC.UniqueId, Don.Barcode,
			convert(varchar, dateadd(day, -1, PerC.BirthDate), 104) BirthDateS, convert(varchar, dateadd(day, 1, PerC.BirthDate), 104) BirthDatePo,
			convert(varchar, dateadd(day, -1, ApD.NextDonationDate), 104) NextDonationDateS, convert(varchar, dateadd(day, 1, ApD.NextDonationDate), 104) NextDonationDatePo,
			case
			when IDoc.DocType = 1 then 'Паспорт РФ'
			when IDoc.DocType = 2 then 'Военный билет'
			when IDoc.DocType = 3 then 'Загранпаспорт РФ'
			when IDoc.DocType = 4 then 'Паспорт СССР'
			when IDoc.DocType = 5 then 'Иные документы'
			when IDoc.DocType = 6 then 'Св-во о рождении'
			end DocType, IDoc.Serie, IDoc.Number
			from PersonCards PerC 
			join AppointedDonationTypes ApD on PerC.UniqueId = ApD.DonorId
			join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId
			join Donations Don on PerC.UniqueId = Don.DonorId
			join PersonAddresses PerAd on PerC.RegAddressId = PerAd.UniqueId
			where PerC.IsDeleted != 1 
			and PerC.LastName not like '%[a-zA-Z0-9?!_+=*\/%()}{<>^]%' and PerC.FirstName not like '%[a-zA-Z0-9?!_+=*\/%()}{<>^]%' and PerC.MiddleName not like '%[a-zA-Z0-9?!_+=*\/%()}{<>^]%'
			and PerC.Gender in ('1','2')
			and PerAd.FiasRegion is not null
			and PerAd.FiasArea is null
			and PerAd.FiasCity is not null
			and PerAd.FiasInnerArea is null
			and PerAd.FiasSettlement is null
			and PerAd.FiasStreet is not null
			and PerAd.FiasHouse is not null
			and ApD.NextDonationDate > dateadd(year, -10, getdate()) 
			and ApD.NextDonationDate < dateadd(year, 10, getdate())
			''')

        donorid_quick_search = str(sql_query("select top (1) PerC.UniqueId Ent from PersonCards PerC where PerC.Gender = '1' and PerC.IsDeleted != '1'"))[0][0]

        lastname, firstname, middlename, gender, region, donorid, barcode, birthdate_from, birthdate_to, next_donation_from, next_donation_to, document_type, document_serie, document_number = (
        full_query[0][0], full_query[0][1],
        full_query[0][2], full_query[0][3], full_query[0][4], full_query[0][5], full_query[0][6], full_query[0][7],
        full_query[0][8], full_query[0][9], full_query[0][10], full_query[0][11], full_query[0][12], full_query[0][13])

        main_page.clear_localstorage()

        main_page.open()

        main_page.extended_search_click('open')

        main_page.filling_fio_in_extended_search(lastname, firstname, middlename)

        main_page.filling_gender_in_extended_search(gender)

        main_page.filling_region_in_extended_search(region)

        aistium.fill(donorid, elements=main_page.extended_registry_number)

        aistium.fill(barcode, elements=main_page.extended_donation_barcode)

        aistium.fill(birthdate_from, elements=main_page.extended_birthdate_from)

        aistium.fill(birthdate_to, elements=main_page.extended_birthdate_to)

        aistium.fill(next_donation_from, elements=main_page.extended_preregistration_from)

        aistium.fill(next_donation_to, elements=main_page.extended_preregistration_to)

        main_page.filling_doc_type_in_extended_search(document_type)

        main_page.filling_doc_serie_in_extended_search(document_serie)

        main_page.filling_doc_number_in_extended_search(document_number)

        aistium.click_on(elements=main_page.extended_search_button)

        main_page.loading_is_completed()

        aistium.fill(donorid_quick_search, elements=main_page.quick_search_field)

        main_page.quick_search('press_enter')

        main_page.loading_is_completed()

        assertions = [main_page.get_lastname_from_extended_search(),
                      main_page.get_firstname_from_extended_search(),
                      main_page.get_middlename_from_extended_search(),
                      main_page.get_region_from_extended_search(),
                      main_page.get_donorid_from_extended_search(),
                      main_page.get_barcode_from_extended_search(),
                      main_page.get_birth_date_from_from_extended_search(),
                      main_page.get_birth_date_to_from_extended_search(),
                      main_page.get_next_donation_from_from_extended_search(),
                      main_page.get_next_donation_to_from_extended_search(),
                      main_page.get_document_serie_from_extended_search(),
                      main_page.get_document_number_from_extended_search()]

        for assertion in assertions:
            assert assertion == ''

        assert main_page.get_gender_from_extended_search() == 'Пол'

        assert main_page.get_document_type_from_extended_search() == ''

    @allure.step('5. МД. Регистратура. Очищение быстрого поиска при выполнении расширенного поиска.')
    def test_reset_search_filters_e(self):
        main_page = DonorsModuleRegistryPage()

        main_page.clear_localstorage()

        main_page.open()

        simple_search_donorid = str(sql_query("select top (1) PerC.UniqueId Ent from PersonCards PerC where PerC.Gender = '1' and PerC.IsDeleted != '1'")[0][0])

        aistium.fill(simple_search_donorid, elements=main_page.quick_search_field)

        main_page.quick_search('press_enter')

        main_page.loading_is_completed()

        extended_search_donorid = str(sql_query("select top (1) PerC.UniqueId Ent from PersonCards PerC where PerC.Gender = '2' and PerC.IsDeleted != '1'")[0][0])

        main_page.extended_search_click('open')

        aistium.fill(extended_search_donorid, elements=main_page.extended_registry_number)

        aistium.click_on(elements=main_page.extended_search_button)

        main_page.loading_is_completed()

        assert aistium.get_value(locators_list=locators, element_name='quick_search_field') == ''

if __name__ == "__main__":
    pytest.main()