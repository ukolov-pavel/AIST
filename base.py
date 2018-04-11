from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest
import selenium
from selenium.webdriver import Firefox

class Driver(object):
    __instance = None

    @classmethod
    def get(cls, type='ff'):
        if not cls.__instance:
            cls.__instance = webdriver.Firefox()
        return cls.__instance

class BaseTest(object):
    stand = "http://10.32.200.142"
    login = 'admin'
    password = '77@dm1n'
    timeout = 15
    @classmethod
    def setup_class(cls):
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