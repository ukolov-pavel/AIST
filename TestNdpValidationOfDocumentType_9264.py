# -*- coding: utf-8 -*-
import pytest, allure, selenium
from base import BaseTest, Driver
from additional_functions import get_data
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-9264')
class TestNdpValidationOfDocumentType(BaseTest):

    @allure.step('1. Проверка значения по умолчанию')
    @pytest.mark.parametrize('expected_result, test_data_set_number', get_data('data_test_ndp_validation_of_document_type_default.csv'))
    def test_ndp_validation_of_document_type_default(self, expected_result, test_data_set_number):
        main_page = DonorsModuleRegistryPage()

        main_page.open()

        main_page.newdonor_click()

        assert main_page.ndp_get_document_type_value() == expected_result

    @allure.step('2. Проверка значений в списке для выбора')
    def test_ndp_validation_of_document_type_list(self):
        main_page = DonorsModuleRegistryPage()

        main_page.open()

        main_page.newdonor_click()

        assert main_page.ndp_get_document_type_listbox() == ['Паспорт РФ', 'Военный билет', 'Загранпаспорт РФ', 'Паспорт СССР', 'Иные документы', 'Св-во о рождении']

if __name__ == "__main__":
    pytest.main()