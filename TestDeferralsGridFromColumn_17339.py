# -*- coding: utf-8 -*-
import pytest, allure, selenium, requests, aistium
from base import BaseTest, Driver
from locators import donors_registry_locators as locators
from additional_functions import sql_query, get_data
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-17339')
class TestDeferralsGridFromColumn_17339(BaseTest):
    @allure.step('1. МД. Поле От (дата начала действия отвода) в гриде, Отводы донора (карточка донора в регистратуре донорского отделения)')
    @pytest.mark.parametrize('query, test_data_set_number', get_data('data_test_deferrals_grid_from_column.csv')) #локально добавила файл
    def test_deferrals_grid_from_column(self, query, test_data_set_number):

        main_page = DonorsModuleRegistryPage()

        main_page.clear_localstorage()

        full_query = sql_query(query)

        donor_id = str(full_query[0][0])

        expected_result = str(full_query[0][1])

        main_page.open()

        aistium.fill(donor_id, elements=main_page.quick_search_field)

        main_page.quick_search('click')

        main_page.loading_is_completed()

        ind = sql_query("select Main.Nmb from (select row_number() over (order by PerC.BirthDate desc) Nmb, PerC.UniqueId from PersonCards PerC left join IdentityDocs IDoc on PerC.IdentityDocId = IDoc.UniqueId where PerC.IsDeleted != 1 and (PerC.UniqueId = '"+donor_id+"' or IDoc.Number = '"+donor_id+"')) Main where Main.UniqueId = '"+donor_id+"'")[0][0]

        main_page.get_grid_values('Fio', ind, main_page.main_grid, mode='click')

        main_page.loading_is_completed()

        aistium.click_on(elements=main_page.deferrals_button)

        main_page.loading_is_completed()

        aistium.click_on(elements=main_page.deferral_only_active_tick)

        main_page.get_grid_values('StartDate', 1, main_page.deferrals_grid, mode='click')

        assert main_page.get_grid_values('StartDate', 1, main_page.deferrals_grid, mode='get_value') == expected_result










