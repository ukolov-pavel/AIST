# -*- coding: utf-8 -*-
import pytest, allure, selenium, aistium
from base import BaseTest, Driver
from additional_functions import sql_query
from donors_registry import DonorsModuleRegistryPage

@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
@allure.testcase('https://aj.srvdev.ru/browse/AIST-6104')
class TestSimpleSearchByDonorNumberMessages(BaseTest):

    @allure.step('Поиск донора по номеру (запрещающие сообщения) (быстрый поиск в регистратуре донорского отделения)')
    def test_simple(self):
        main_page = DonorsModuleRegistryPage()

        Sel1 = 1

        Sel2 = 1

        I = 1

        while (Sel1 > 0 or Sel2 > 0):
            donor_number = str(sql_query("select ls.Nm from (select row_number() over (order by PerC.UniqueId desc) as rank, replace(str(PerC.UniqueId), ' ','') + replace(str(" + str(I) + "), ' ','') Nm from PersonCards PerC where PerC.IsDeleted != 1) ls where ls.rank = " + str(I))[0][0])
            Sel1 = len(sql_query("select top (1) replace(IdDoc.Number, ' ','') Ent from IdentityDocs IdDoc where replace(IdDoc.Number, ' ','') = '" + donor_number + "'"))
            Sel2 = len(sql_query("select top (1) replace(str(PerC.UniqueId), ' ','') Ent from PersonCards PerC where replace(str(PerC.UniqueId), ' ','') = '" + donor_number + "'"))
            I = I + 1

        main_page.clear_localstorage()

        main_page.open()

        aistium.fill(donor_number, elements=main_page.quick_search_field)

        main_page.quick_search('click')

        main_page.loading_is_completed()

        assert main_page.get_snils_alert_text() == "Донор не найден."

if __name__ == "__main__":
    pytest.main()