# -*- coding: utf-8 -*-
import pytest, allure, selenium, requests, aistium
from base import BaseTest, Driver
from locators import donors_registry_locators as locators
from additional_functions import sql_query, get_data
from donors_registry import DonorsModuleRegistryPage
from system_settings.donor_settings import change_donor_settings
from system_settings.sticker_settings import change_sticker_settings


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6813')
class TestDonorsDirectionInformationMessages(BaseTest):

    @allure.step('1. МД. Кнопка Направить (информационные сообщения) (карточка донора в регистратуре донорского отделения)')
    @pytest.mark.parametrize('query, test_data_set_number', get_data('data_test_donors_direction_information_messages.csv'))
    def test_donors_direction_information_messages(self, query, test_data_set_number):
        main_page = DonorsModuleRegistryPage()

        main_page.clear_localstorage()

        full_query = sql_query(query)

        donor_id = str(full_query[0][0])

        expected_message = str(full_query[0][1])

        str_index = str(full_query[0][2])

        donations_count = str(full_query[0][3])

        blood_and_components_count = str(full_query[0][4])

        plasma_count = str(full_query[0][4])

        donations_counts = {
        'HonorableDonorSettings[0].DonationsCount': '999',
        'HonorableDonorSettings[0].BloodAndComponentsCount': '999',
        'HonorableDonorSettings[0].PlasmaCount': '999',
        'HonorableDonorSettings[1].DonationsCount': '999',
        'HonorableDonorSettings[1].BloodAndComponentsCount': '999',
        'HonorableDonorSettings[1].PlasmaCount': '999',
        'HonorableDonorSettings[2].DonationsCount': '999',
        'HonorableDonorSettings[2].BloodAndComponentsCount': '999',
        'HonorableDonorSettings[2].PlasmaCount': '999',
        'HonorableDonorSettings[3].DonationsCount': '999',
        'HonorableDonorSettings[3].BloodAndComponentsCount': '999',
        'HonorableDonorSettings[3].PlasmaCount': '999'
        }

        donations_counts['HonorableDonorSettings['+str_index+'].DonationsCount'] = donations_count

        donations_counts['HonorableDonorSettings['+str_index+'].BloodAndComponentsCount'] = blood_and_components_count

        donations_counts['HonorableDonorSettings['+str_index+'].PlasmaCount'] = plasma_count

        change_donor_settings(**{str(k): v for k, v in donations_counts.items()},
            DonorsModuleRegistryPage='false',
            CheckFiasAddressForDonor='false',
            CheckIncompleteAnalysis='false',
            NotifyRegistrarForHonorableDonor='true')

        change_sticker_settings(PrintRunner='false')

        main_page.open()

        aistium.fill(donor_id, elements = main_page.quick_search_field)

        main_page.quick_search('click')

        main_page.loading_is_completed()

        ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC left join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and (PerC.UniqueId = '"+donor_id+"' or IDoc.Number = '"+donor_id+"')) Main where Main.UniqueId = '"+donor_id+"'")[0][0]

        main_page.get_grid_values('UniqueId', ind, main_page.main_grid, 'click')

        main_page.loading_is_completed()

        aistium.click_on(elements=main_page.process_state_button)

        main_page.loading_is_completed()

        if aistium.get_background_color(locators_list=locators, element_name='popup_titlebar') == '#E19F50':
            aistium.click_on(locators_list=locators, element_name='confirm-popup-yes')
        else: 
            pass

        assert main_page.get_alert_text() == expected_message

        assert aistium.get_text(elements=main_page.process_state_button) == 'Вернуть'

if __name__ == "__main__":
    pytest.main()





