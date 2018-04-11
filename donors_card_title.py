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
from locators import donors_card_title_locators as L

class AbstractBasePage(BasePage):

	def __init__(self, url):
		BasePage.__init__(self, Driver.get(), url)

	def get_title(self):
		return Driver.get().title

	def get_url(self):
		return Driver.get().current_url

class DonorsCardTitle(AbstractBasePage):

	personal_content_back_address_and_jobs = Finds(by=L['personal_content_back_address_and_jobs'][1], value=L['personal_content_back_address_and_jobs'][2])

	def __init__(self, donor_id):
		AbstractBasePage.__init__(self, BaseTest.stand+'/Donor/Registration/Edit/'+donor_id+'?showDeleted=False')

	def loading_is_completed(cls):
		time.sleep(2)
		while 1:
			try:
				WebDriverWait(Driver.get(), 2).until(EC.visibility_of_any_elements_located((By.CLASS_NAME, 'k-loading-image')))
				continue
			except:
				time.sleep(1)
				break

	def job_place(cls):
		return Driver.get().find_elements(by=L['personal_content_back_address_and_jobs'][1], value=L['personal_content_back_address_and_jobs'][2])[1].text

	def job(cls):
		return Driver.get().find_elements(by=L['personal_content_back_address_and_jobs'][1], value=L['personal_content_back_address_and_jobs'][2])[2].text

	def social_status(cls):
		return Driver.get().find_elements(by=L['personal_content_back_address_and_jobs'][1],
		value=L['personal_content_back_address_and_jobs'][2])[3].text

	def issued_by(cls):
		return Driver.get().find_element_by_css_selector('span.bold').text