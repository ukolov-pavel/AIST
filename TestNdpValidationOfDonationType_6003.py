# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import get_data, sql_query, convert_to_hex
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6003')
class TestNdpValidationOfDonationType(BaseTest):

    @allure.step('1. Проверка значений для выбора в поле Тип донации, в том числе упорядочивание значений; ввод значения в поле Тип донации вручную, при условии, что оно есть в списке для выбора')
    def test_ndp_validation_of_donation_type_first_case(self):
        main_page = DonorsModuleRegistryPage()

        main_page.clear_localstorage()

        main_page.open()

        query = sql_query("select DonT.Code+' '+DonT.Name from ref.DonationTypes DonT join ref.DonationTypeParams DonTP on DonT.UniqueId = DonTP.DonationTypeId where DonTP.IsActive = 1 and DonT.DonationParams not like '%4%' order by DonT.Code")

        donation_types_db = []

        main_page.newdonor_click()

        main_page.ndp_filling_first_page("Сидоров", "Павел", '', "11.06.1980", "8920", "650241")

        main_page.select_gender('male')

        aistium.click_on(elements=main_page.next_step_ndp)

        main_page.loading_is_completed()

        main_page.if_donor_is_in_local_cabinet()

        main_page.ndp_filling_region("Москва г")

        main_page.ndp_filling_street("Перовская ул")

        aistium.fill('14', elements=main_page.reg_fias_address_house)

        aistium.click_on(elements=main_page.donation_type_select_row)

        for t in query:
            donation_types_db.append(t[0])

        assert main_page.ndp_donation_types_list_on_form() == donation_types_db

        main_page.ndp_filling_donation_type('001 на лабораторные исследования')

        assert main_page.ndp_get_donation_type() == '001 На лабораторные исследования'

        main_page.ndp_save_new_donor('success')

        assert aistium.get_text(elements=main_page.fio_minicard) == "Сидоров " + "Павел"

    @allure.step('2. Соответствие цвета заливки поля типу донации')
    @pytest.mark.parametrize('expected_color_back, expected_color_text, expected_type, test_data_set_number', get_data('data_test_ndp_validation_of_donation_type_second_case.csv'))
    def test_ndp_validation_of_donation_type_second_case(self, expected_color_back, expected_color_text, expected_type, test_data_set_number):
        main_page = DonorsModuleRegistryPage()

        main_page.clear_localstorage()

        main_page.open()

        query = "select top(1) DonT.Code+' '+DonT.Name from ref.DonationTypes DonT join ref.DonationTypeParams DonTP on DonT.UniqueId = DonTP.DonationTypeId where DonTP.IsActive = 1 and DonT.DonationParams not like '%4%' and DonT.ComponentType="

        main_page.newdonor_click()

        main_page.ndp_filling_first_page("Сидоров", "Кирилл", '', "01.06.1980", "3608", "360471")

        main_page.select_gender('male')

        aistium.click_on(elements=main_page.next_step_ndp)

        main_page.loading_is_completed()

        main_page.if_donor_is_in_local_cabinet()

        main_page.ndp_filling_donation_type(sql_query(query + expected_type)[0][0])

        assert convert_to_hex(main_page.ndp_get_donation_type_color()).lower() == expected_color_back

        assert convert_to_hex(main_page.ndp_get_donation_type_text_color()).lower() == expected_color_text

    @allure.step('3. Добавление и последующее удаление типа донации на форме создания донора. Проверка правильности сохранения данных')
    def test_ndp_validation_of_donation_type_third_case(self):
        main_page = DonorsModuleRegistryPage()

        main_page.clear_localstorage()

        main_page.open()

        query = "select top(1) DonT.Code+' '+DonT.Name from ref.DonationTypes DonT join ref.DonationTypeParams DonTP on DonT.UniqueId = DonTP.DonationTypeId where DonTP.IsActive = 1 and DonT.DonationParams not like '%4%'"

        main_page.newdonor_click()

        main_page.ndp_filling_first_page("Сидоров", "Вадим", '', "19.06.1980", "8928", "650249")

        main_page.select_gender('male')

        aistium.click_on(elements=main_page.next_step_ndp)

        main_page.loading_is_completed()

        main_page.if_donor_is_in_local_cabinet()

        main_page.ndp_filling_region("Москва г")

        main_page.ndp_filling_street("Перовская ул")

        aistium.fill('22', elements=main_page.reg_fias_address_house)

        main_page.ndp_filling_donation_type(sql_query(query)[0][0])

        main_page.ndp_donation_type_clear()

        main_page.ndp_donation_type_focus_out()

        assert main_page.ndp_get_donation_type() == ''

        main_page.ndp_save_new_donor('success')

        assert main_page.get_donation_type_value_from_minicard() == 'ДОНАЦИЯ НЕ УКАЗАНА'

    @allure.step('4. Добавление и последующее изменение типа донации на форме создания донора. Проверка правильности сохранения данных')
    def test_ndp_validation_of_donation_type_fourth_case(self):
        main_page = DonorsModuleRegistryPage()

        main_page.clear_localstorage()

        main_page.open()

        query = "select top(1) DonT.Code+' '+DonT.Name  from ref.DonationTypes DonT join ref.DonationTypeParams DonTP on DonT.UniqueId = DonTP.DonationTypeId where DonTP.IsActive = 1 and DonT.DonationParams not like '%4%'"

        main_page.newdonor_click()

        main_page.ndp_filling_first_page("Сидоров", "Алексей", '', "20.06.1980", "8929", "650250")

        main_page.select_gender('male')

        aistium.click_on(elements=main_page.next_step_ndp)

        main_page.loading_is_completed()

        main_page.if_donor_is_in_local_cabinet()

        main_page.ndp_filling_region("Москва г")

        main_page.ndp_filling_street("Перовская ул")

        aistium.fill('23', elements=main_page.reg_fias_address_house)

        main_page.ndp_filling_donation_type(sql_query(query)[0][0])

        assert main_page.ndp_get_donation_type() == sql_query(query)[0][0]

        main_page.ndp_donation_type_clear()

        main_page.ndp_donation_type_focus_out()

        main_page.ndp_filling_donation_type("э", mode='first_li')

        current_donation_type = main_page.ndp_get_donation_type()

        main_page.ndp_save_new_donor('success')

        assert main_page.get_donation_type_value_from_minicard() == current_donation_type

    @allure.step('5. Ввод значений в поле "Тип донации" без его выбора, расфокусировка поля и его последующее очищение.')
    @pytest.mark.parametrize('donation_type, test_data_set_number', get_data('data_test_ndp_validation_of_donation_type_fifth_case.csv'))
    def test_ndp_validation_of_donation_type_fifth_case(self, donation_type, test_data_set_number):
        main_page = DonorsModuleRegistryPage()

        main_page.clear_localstorage()

        main_page.open()

        main_page.newdonor_click()

        main_page.ndp_filling_first_page("Сидоров", "Кирилл", '', "01.06.1980", "3608", "360471")

        main_page.select_gender('male')

        aistium.click_on(elements=main_page.next_step_ndp)

        main_page.loading_is_completed()

        main_page.if_donor_is_in_local_cabinet()

        assert main_page.ndp_filling_donation_type(donation_type, mode='does_not_exists') == True

        main_page.ndp_donation_type_focus_out()

        assert main_page.ndp_get_donation_type() == ''

        main_page.ndp_save_new_donor('success')

if __name__ == "__main__":
    pytest.main()