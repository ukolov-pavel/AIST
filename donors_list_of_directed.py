from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from webium import BasePage, Find, Finds
from base import Driver, BaseTest
from dateutil.relativedelta import relativedelta
import datetime
import time

class AbstractBasePage(BasePage):

	def __init__(self, url):
		BasePage.__init__(self, Driver.get(), url)

	def get_title(self):
		return Driver.get().title

class DonorsListOfDirected(AbstractBasePage):

	def __init__(self):
		AbstractBasePage.__init__(self, BaseTest.stand+'/Donor/Registration/Directed?clearGridState=1')

	def get_directed_date_value(cls):
		return Driver.get().find_element_by_id('directedDate').text