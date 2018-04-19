from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests

class Driver(object):
    __instance = None

    @classmethod
    def get(cls, type='ff'):
        if not cls.__instance:
            cls.__instance = webdriver.Firefox()
        return cls.__instance

class Session(object):
    __instance = None

    @classmethod
    def get(cls):
        if not cls.__instance:
            cls.__instance = requests.Session()
        return cls.__instance

class BaseTest(object):
    '''
    Реализована работа с настройками системы:
    при создании тестов, в которых используются те или иные глобальные настройки, для возврата к исходным
    состояниям настроек, затрагиваемых автотестом, отныне нужно присваивать переменной used_settings
    список классов из back_to_default.py, в соответствии с настройками, которые нужны в тесте.
    '''
    stand = "http://10.32.200.142"
    login = 'autotest'
    password = '77@dm1nA'
    timeout = 15
    used_settings_classes = []
    started_settings = []
    @classmethod
    def setup_class(cls):
        for setting in cls.used_settings_classes:
            cls.started_settings.append(setting.get_settings())
        cls.driver = Driver.get()
        #cls.driver.implicitly_wait(0)
        cls.driver.maximize_window()
        cls.driver.get(cls.stand)
        cls.driver.find_element_by_id('Login').send_keys(cls.login)
        cls.driver.find_element_by_id('Password').send_keys(cls.password)
        cls.driver.find_element_by_class_name('submit').click()
        WebDriverWait(Driver.get(), 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".donor-logo")))
    @classmethod
    def teardown_class(cls):
        Driver.get().close()
        if cls.started_settings:
            for dic in cls.started_settings:
                if dic:
                    cls.used_settings_classes[cls.started_settings.index(dic)]().post_settings(cls.started_settings[cls.started_settings.index(dic)])
            Session.get().close()