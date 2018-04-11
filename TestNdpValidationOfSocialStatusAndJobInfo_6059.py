# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import get_data, sql_query
from donors_registry import DonorsModuleRegistryPage
from system_settings.general_settings import change_general_settings


@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6003')
class TestNdpValidationOfSocialStatusAndJobInfo(BaseTest):

    @allure.step('1. Проверка значений для выбора в поле "Социальный статус донора", в том числе упорядочивание значений; проверка выбора значения из списка')
    def test_ndp_validation_of_social_status_and_job_info_a(self):
        main_page = DonorsModuleRegistryPage()

        main_page.clear_localstorage()

        change_general_settings(WorkWithSocialStatus='true')

        main_page.open()

        query = sql_query("select SocSt.Name from ref.SocialStatuses SocSt where SocSt.IsActive = 1 order by SocSt.Name asc")

        social_statuses_db = []

        main_page.newdonor_click()

        main_page.ndp_filling_first_page("Сидоров", "Дмитрий", '', "31.05.1980", "8909", "650229")

        main_page.select_gender('male')

        aistium.click_on(elements=main_page.next_step_ndp)

        main_page.loading_is_completed()

        main_page.if_donor_is_in_local_cabinet()

        main_page.ndp_filling_region("Москва г")

        main_page.ndp_filling_street("Перовская ул")

        aistium.fill("2", elements=main_page.reg_fias_address_house)

        aistium.click_on(elements=main_page.social_status_select_row)

        for s in query:
            social_statuses_db.append(s[0])

        assert main_page.ndp_social_statuses_list_on_form() == social_statuses_db

        main_page.ndp_choose_social_status_from_list('Рабочие')

        main_page.ndp_social_status_focusout()

        assert main_page.ndp_get_job_information()[2] == 'Рабочие'

        main_page.ndp_save_new_donor('success')

        assert aistium.get_text(elements=main_page.fio_minicard) == "Сидоров " + "Дмитрий"

    @allure.step('2. Ввод значения в поле "Социальный статус донора"" вручную при условии, что оно есть в списке для выбора')
    @pytest.mark.parametrize('expected_color_back, expected_color_text, expected_type, test_data_set_number', get_data('data_test_ndp_validation_of_donation_type_second_case.csv'))
    def test_ndp_validation_of_social_status_and_job_info_b(self, expected_color_back, expected_color_text, expected_type, test_data_set_number):
        main_page = DonorsModuleRegistryPage()

        main_page.clear_localstorage()

        change_general_settings(WorkWithSocialStatus='true')

        main_page.open()

        main_page.newdonor_click()

        main_page.ndp_filling_first_page("Сидоров", "Никита", '', "02.06.1980", "8911", "650232")

        main_page.select_gender('male')

        aistium.click_on(elements=main_page.next_step_ndp)

        main_page.loading_is_completed()

        main_page.if_donor_is_in_local_cabinet()

        main_page.ndp_filling_region("Москва г")

        main_page.ndp_filling_street("Перовская ул")

        aistium.fill('5', elements=main_page.reg_fias_address_house)

        main_page.ndp_typing_social_status('врачи')

        main_page.ndp_social_status_focusout()

        assert main_page.ndp_get_job_information()[2] == 'Врачи'

        main_page.ndp_save_new_donor('success')

        assert aistium.get_text(elements=main_page.fio_minicard) == "Сидоров " + "Никита"

    @allure.step('3. Проверка значений для выбора в поле Социальный статус донора при частичном вводе значения; последующий выбор значения из списка')
    def test_ndp_validation_of_social_status_and_job_info_c(self):
        main_page = DonorsModuleRegistryPage()

        main_page.clear_localstorage()

        change_general_settings(WorkWithSocialStatus='true')

        query = sql_query("select SocSt.Name from ref.SocialStatuses SocSt where SocSt.IsActive = 1 and SocSt.Name like '%персонал%'")

        social_statuses_db = []

        for s in query:
            social_statuses_db.append(s[0])

        main_page.open()

        main_page.newdonor_click()

        main_page.ndp_filling_first_page("Сидоров", "Станислав", '', "03.06.1980", "8912", "650233")

        main_page.select_gender('male')

        aistium.click_on(elements=main_page.next_step_ndp)

        main_page.loading_is_completed()

        main_page.if_donor_is_in_local_cabinet()

        main_page.ndp_filling_region("Москва г")

        main_page.ndp_filling_street("Перовская ул")

        aistium.fill('6', elements=main_page.reg_fias_address_house)

        main_page.ndp_typing_social_status('персонал')

        assert main_page.ndp_social_statuses_list_on_form() == social_statuses_db

        main_page.ndp_choose_social_status_from_list("Средний медицинский персонал")

        main_page.ndp_social_status_focusout()

        assert main_page.ndp_get_job_information()[2] == 'Средний медицинский персонал'

        main_page.ndp_save_new_donor('success')

        assert aistium.get_text(elements=main_page.fio_minicard) == "Сидоров " + "Станислав"

    @allure.step('4. Проверка значений для выбора в поле Социальный статус донора при вводе одного символа для поиска; проверка изменения значения в поле Социальный статус')
    def test_ndp_validation_of_social_status_and_job_info_d(self):
        main_page = DonorsModuleRegistryPage()

        main_page.clear_localstorage()

        change_general_settings(WorkWithSocialStatus='true')

        query = sql_query("select SocSt.Name from ref.SocialStatuses SocSt where SocSt.IsActive = 1 and SocSt.Name like '%ц%'")

        social_statuses_db = []

        for s in query:
            social_statuses_db.append(s[0])

        main_page.open()

        main_page.newdonor_click()

        main_page.ndp_filling_first_page("Сидоров", "Афанасий", '', "04.06.1980", "8913", "650234")

        main_page.select_gender('male')

        aistium.click_on(elements=main_page.next_step_ndp)

        main_page.loading_is_completed()

        main_page.if_donor_is_in_local_cabinet()

        main_page.ndp_filling_region("Москва г")

        main_page.ndp_filling_street("Перовская ул")

        aistium.fill('7', elements=main_page.reg_fias_address_house)

        aistium.click_on(elements=main_page.social_status_select_row)

        main_page.ndp_choose_social_status_from_list("Рабочие")

        main_page.ndp_social_status_clear()

        main_page.ndp_typing_social_status('ц')

        assert main_page.ndp_social_statuses_list_on_form() == social_statuses_db

        main_page.ndp_choose_social_status_from_list("Младший медицинский персонал")

        main_page.ndp_social_status_focusout()

        assert main_page.ndp_get_job_information()[2] == 'Младший медицинский персонал'

        main_page.ndp_save_new_donor('success')

        assert aistium.get_text(elements=main_page.fio_minicard) == "Сидоров " + "Афанасий"

    @allure.step('5. ')
    @pytest.mark.parametrize('social_status, test_data_set_number', get_data('data_test_ndp_validation_of_social_status_and_job_info_e.csv'))
    def test_ndp_validation_of_social_status_and_job_info_e(self, social_status, test_data_set_number):
        main_page = DonorsModuleRegistryPage()

        main_page.clear_localstorage()

        change_general_settings(WorkWithSocialStatus='true')

        query = sql_query("select SocSt.Name from ref.SocialStatuses SocSt where SocSt.IsActive = 1 and SocSt.Name like '%ц%'")

        social_statuses_db = []

        for s in query:
            social_statuses_db.append(s[0])

        main_page.open()

        main_page.newdonor_click()

        main_page.ndp_filling_first_page("Сидоров", "Кирилл", '', "01.06.1980", "8910", "650231")

        main_page.select_gender('male')

        aistium.click_on(elements=main_page.next_step_ndp)

        main_page.loading_is_completed()

        main_page.if_donor_is_in_local_cabinet()

        main_page.ndp_filling_region("Москва г")

        main_page.ndp_filling_street("Перовская ул")

        aistium.fill('4', elements=main_page.reg_fias_address_house)

        main_page.ndp_typing_social_status(social_status)

        assert main_page.ndp_social_status_listbox_is_empty()

        main_page.ndp_social_status_focusout()

        assert main_page.ndp_get_job_information()[2] == ''

        main_page.ndp_save_new_donor('success')

        assert aistium.get_text(elements=main_page.fio_minicard) == "Сидоров " + "Кирилл"

if __name__ == "__main__":
    pytest.main()