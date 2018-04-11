from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from webium import BasePage, Find, Finds
from base import Driver, BaseTest
from dateutil.relativedelta import relativedelta
import datetime, time, aistium
from locators import donors_registry_locators as L
from additional_functions import date_calculation, convert_to_hex
from selenium.common.exceptions import ElementNotInteractableException

class AbstractBasePage(BasePage):

	def __init__(self, url):
		BasePage.__init__(self, Driver.get(), url)

	def get_title(self):
		return Driver.get().title

class DonorsModuleRegistryPage(AbstractBasePage, WebElement):

	alert = Find(by=L['alert'][1], value=L['alert'][2])
	birthdate_field_ndp = Find(by=L['birthdate_field_ndp'][1], value=L['birthdate_field_ndp'][2])
	cancel_reason_back_donation_btn = Find(by=L['cancel_reason_back_donation_btn'][1], value=L['cancel_reason_back_donation_btn'][2])
	confirm_popup = Finds(by=L['confirm_popup'][1], value=L['confirm_popup'][2])
	confirm_popup_no_btn = Finds(by=L['confirm_popup_no_btn'][1], value=L['confirm_popup_no_btn'][2])
	confirm_popup_yes_btn = Finds(by=L['confirm_popup_yes_btn'][1], value=L['confirm_popup_yes_btn'][2])
	deferrals_button = Find(by=L['deferrals_button'][1], value=L['deferrals_button'][2])
	deferrals_grid = Find(by=L['deferrals_grid'][1], value=L['deferrals_grid'][2])
	deferral_from_minicard = Find(by=L['deferral_from_minicard'][1], value=L['deferral_from_minicard'][2])
	deferral_only_active_tick = Find(by=L['deferral_only_active_tick'][1], value=L['deferral_only_active_tick'][2])
	diseases_button = Find(by=L['diseases_button'][1], value=L['diseases_button'][2])
	diseases_grid = Find(by=L['diseases_grid'][1], value=L['diseases_grid'][2])
	diseases_only_active = Find(by=L['diseases_only_active'][1], value=L['diseases_only_active'][2])
	document_number_field_ndp = Find(by=L['document_number_field_ndp'][1], value=L['document_number_field_ndp'][2])
	document_serie_field_ndp = Find(by=L['document_serie_field_ndp'][1], value=L['document_serie_field_ndp'][2])
	document_type_select_field = Find(by=L['document_type_select_field'][1], value=L['document_type_select_field'][2])
	donation_type_select_row = Find(by=L['donation_type_select_row'][1], value=L['donation_type_select_row'][2])
	edit_reason_back_donation_window = Finds(by=L['edit_reason_back_donation_window'][1], value=L['edit_reason_back_donation_window'][2])
	extended_lastname = Find(by=L['extended_lastname'][1], value=L['extended_lastname'][2])
	extended_search_field = Find(by=L['extended_search_field'][1], value=L['extended_search_field'][2])
	extended_search_select_gender_field = Find(by=L['extended_search_select_gender_field'][1], value=L['extended_search_select_gender_field'][2])
	extended_search_select_doc_type_field = Find(by=L['extended_search_select_doc_type_field'][1], value=L['extended_search_select_doc_type_field'][2])
	extended_search_button = Find(by=L['extended_search_button'][1], value=L['extended_search_button'][2])
	extended_search_clear_button = Find(by=L['extended_search_clear_button'][1], value=L['extended_search_clear_button'][2])
	extended_search_close = Find(by=L['extended_search_close'][1], value=L['extended_search_close'][2])
	extended_firstname = Find(by=L['extended_firstname'][1], value=L['extended_firstname'][2])
	extended_middlename = Find(by=L['extended_middlename'][1], value=L['extended_middlename'][2])
	extended_registry_number = Find(by=L['extended_registry_number'][1], value=L['extended_registry_number'][2])
	extended_donation_barcode = Find(by=L['extended_donation_barcode'][1], value=L['extended_donation_barcode'][2])
	extended_birthdate_from = Find(by=L['extended_birthdate_from'][1], value=L['extended_birthdate_from'][2])
	extended_birthdate_to = Find(by=L['extended_birthdate_to'][1], value=L['extended_birthdate_to'][2])
	extended_preregistration_from = Find(by=L['extended_preregistration_from'][1], value=L['extended_preregistration_from'][2])
	extended_preregistration_to = Find(by=L['extended_preregistration_to'][1], value=L['extended_preregistration_to'][2])
	fio_minicard = Find(by=L['fio_minicard'][1], value=L['fio_minicard'][2])
	first_name_field_ndp = Find(by=L['first_name_field_ndp'][1], value=L['first_name_field_ndp'][2])
	identity_document_issue_date = Find(by=L['identity_document_issue_date'][1], value=L['identity_document_issue_date'][2])
	identity_document_issued_by = Find(by=L['identity_document_issued_by'][1], value=L['identity_document_issued_by'][2])
	is_agree_persional_data_processing = Find(by=L['is_agree_persional_data_processing'][1], value=L['is_agree_persional_data_processing'][2])
	is_fact_address_equals_reg_address = Find(by=L['is_fact_address_equals_reg_address'][1], value=L['is_fact_address_equals_reg_address'][2])
	is_message_agree = Find(by=L['is_message_agree'][1], value=L['is_message_agree'][2])
	job_place = Find(by=L['job_place'][1], value=L['job_place'][2])
	job_position = Find(by=L['job_position'][1], value=L['job_position'][2])
	last_name_field_ndp = Find(by=L['last_name_field_ndp'][1], value=L['last_name_field_ndp'][2])#здесь и далее: ndp - new_donor_popup
	list_of_directed_button = Find(by=L['list_of_directed_button'][1], value=L['list_of_directed_button'][2])
	local_cabinet_continue = Find(by=L['local_cabinet_continue'][1], value=L['local_cabinet_continue'][2])
	main_grid = Find(by=L['main_grid'][1], value=L['main_grid'][2])
	middle_name_field_ndp = Find(by=L['middle_name_field_ndp'][1], value=L['middle_name_field_ndp'][2])
	minicard_address = Find(by=L['minicard_address'][1], value=L['minicard_address'][2])
	minicard_email = Find(by=L['minicard_email'][1], value=L['minicard_email'][2])
	minicard_job_place_label = Find(by=L['minicard_job_place_label'][1], value=L['minicard_job_place_label'][2])
	minicard_mobile_phone = Find(by=L['minicard_mobile_phone'][1], value=L['minicard_mobile_phone'][2])
	minicard_phone = Find(by=L['minicard_phone'][1], value=L['minicard_phone'][2])
	minicard_snils = Find(by=L['minicard_snils'][1], value=L['minicard_snils'][2])
	ndp_male_gender = Find(by=L['ndp_male_gender'][1], value=L['ndp_male_gender'][2])
	ndp_female_gender = Find(by=L['ndp_female_gender'][1], value=L['ndp_female_gender'][2])
	ndp_birth_place = Find(by=L['ndp_birth_place'][1], value=L['ndp_birth_place'][2])
	ndp_donation_type_field = Find(by=L['ndp_donation_type_field'][1], value=L['ndp_donation_type_field'][2])
	ndp_mobile_phone = Find(by=L['ndp_mobile_phone'][1], value=L['ndp_mobile_phone'][2])
	ndp_phone = Find(by=L['ndp_phone'][1], value=L['ndp_phone'][2])
	ndp_email = Find(by=L['ndp_email'][1], value=L['ndp_email'][2])
	ndp_deferral_field = Find(by=L['ndp_deferral_field'][1], value=L['ndp_deferral_field'][2])
	ndp_deferral_clear_button = Find(by=L['ndp_deferral_clear_button'][1], value=L['ndp_deferral_clear_button'][2])
	ndp_deferral_type = Find(by=L['ndp_deferral_type'][1], value=L['ndp_deferral_type'][2])
	ndp_job_place_field = Find(by=L['ndp_job_place_field'][1], value=L['ndp_job_place_field'][2])
	ndp_first_page_cancel_newdonor = Find(by=L['ndp_first_page_cancel_newdonor'][1], value=L['ndp_first_page_cancel_newdonor'][2])
	ndp_second_page_cancel_newdonor = Find(by=L['ndp_second_page_cancel_newdonor'][1], value=L['ndp_second_page_cancel_newdonor'][2])
	next_step_ndp = Find(by=L['next_step_ndp'][1], value=L['next_step_ndp'][2])
	newdonor = Find(by=L['newdonor'][1], value=L['newdonor'][2])
	popup_close_icon = Finds(by=L['popup_close_icon'][1], value=L['popup_close_icon'][2])
	popup_titlebar = Find(by=L['popup_titlebar'][1], value=L['popup_titlebar'][2])
	previous_step_ndp = Find(by=L['previous_step_ndp'][1], value=L['previous_step_ndp'][2])
	process_state_button = Find(by=L['process_state_button'][1], value=L['process_state_button'][2])
	quick_search_button = Find(by=L['quick_search_button'][1], value=L['quick_search_button'][2])
	quick_search_field = Find(by=L['quick_search_field'][1], value=L['quick_search_field'][2])
	reason_back_donation_input = Find(by=L['reason_back_donation_input'][1], value=L['reason_back_donation_input'][2])
	reg_fias_address_region = Find(by=L['reg_fias_address_region'][1], value=L['reg_fias_address_region'][2])
	reg_fias_address_region_listbox = Finds(by=L['reg_fias_address_region_listbox'][1], value=L['reg_fias_address_region_listbox'][2])
	reg_fias_address_city = Find(by=L['reg_fias_address_city'][1], value=L['reg_fias_address_city'][2])
	reg_fias_address_city_listbox = Finds(by=L['reg_fias_address_city_listbox'][1], value=L['reg_fias_address_city_listbox'][2])
	reg_fias_address_building = Find(by=L['reg_fias_address_building'][1], value=L['reg_fias_address_building'][2])
	reg_fias_address_structure = Find(by=L['reg_fias_address_structure'][1], value=L['reg_fias_address_structure'][2])
	reg_fias_address_street = Find(by=L['reg_fias_address_street'][1], value=L['reg_fias_address_street'][2])
	reg_fias_address_house = Find(by=L['reg_fias_address_house'][1], value=L['reg_fias_address_house'][2])
	reg_fias_address_office = Find(by=L['reg_fias_address_office'][1], value=L['reg_fias_address_office'][2])
	reset_filters = Find(by=L['reset_filters'][1], value=L['reset_filters'][2])
	save_new_donor_button = Find(by=L['save_new_donor_button'][1], value=L['save_new_donor_button'][2])
	save_reason_back_donation_btn = Find(by=L['save_reason_back_donation_btn'][1], value=L['save_reason_back_donation_btn'][2])
	snils_field = Find(by=L['snils_field'][1], value=L['snils_field'][2])
	social_status_field = Find(by=L['social_status_field'][1], value=L['social_status_field'][2])
	social_status_select_row = Find(by=L['social_status_select_row'][1], value=L['social_status_select_row'][2])

	def __init__(self):
		AbstractBasePage.__init__(self, BaseTest.stand+'/donor')

	def hover_top_menu(cls, menu_index, element_index):
		ActionChains(Driver.get()).move_to_element(Driver.get().find_element_by_css_selector('#top-menu > li:nth-child(' + menu_index + ')')).perform()
		while 1:
			try:
				WebDriverWait(Driver.get(), 2).until(lambda driver: driver.find_element_by_class_name('k-group.k-menu-group.k-popup.k-reset.k-state-border-up').is_displayed())
				break
			except:
				continue
		time.sleep(1)
		Driver.get().find_element_by_class_name('k-group.k-menu-group.k-popup.k-reset.k-state-border-up').find_elements_by_tag_name('li')[element_index].click()

	def quick_search(cls, mode):
		if mode == 'click':
			aistium.click_on(elements=cls.quick_search_button)
		else:
			aistium.fill(Keys.ENTER, elements=cls.quick_search_field)
	
	def loading_is_completed(cls):
		time.sleep(3)
		Driver.get().implicitly_wait(0)
		while 1:
			try:
				WebDriverWait(Driver.get(), 1).until(EC.visibility_of_any_elements_located((By.CLASS_NAME, 'k-loading-image')))
				continue
			except:
				time.sleep(1)
				break

	def get_grid_values(cls, column, row, grid, mode='get_value'):
		columns = grid.find_elements_by_tag_name('th')
		for i in columns:
			if i.get_attribute('data-field') == column:
				ind = columns.index(i)
		try:
			ind
		except:
			raise Exception('Column with the name *' + column + '* does not exist')
		tbody = grid.find_element_by_xpath("./div[contains(@class, 'k-grid-content')]//table/tbody")
		if row != 'active_cell':
			row = tbody.find_elements_by_tag_name('tr')[row-1]
		else:
			row = tbody.find_element_by_class_name('k-state-selected')
		Driver.get().switch_to.default_content()
		Driver.get().execute_script("arguments[0].scrollIntoView();", row)
		value = row.find_elements_by_tag_name('td')[ind]
		Driver.get().execute_script("arguments[0].scrollIntoView();", value)
		if mode == 'get_value':
			return value.text
		elif mode == 'click':
			value.click()
		elif mode == 'background-color':
			return value.find_element_by_css_selector('div').value_of_css_property('background-color')
		elif mode == 'color':
			return value.find_element_by_css_selector('div').value_of_css_property('color')

	def is_grid_row_selected(cls, row_ind):
		row = Driver.get().find_element_by_xpath("//div[contains(@class, 'k-virtual-scrollable-wrap')]/table/tbody").find_elements_by_tag_name('tr')[row_ind-1]
		return row.value_of_css_property('background-color') == 'rgb(25, 132, 200)' and row.get_attribute('class') == 'k-state-selected'

	def link_to_donor_card(cls):
		return Driver.get().find_element_by_class_name('person-card-details-fio').get_attribute('href')

	def number_of_entities_at_grid(cls, grid):
		tbody = grid.find_element_by_xpath("./div[contains(@class, 'k-grid-content')]//table/tbody")
		rows = tbody.find_elements_by_tag_name('tr')
		return len(rows)

	def number_of_entities_at_grid_including_hidden(cls):
		return int(Driver.get().find_element_by_class_name('titleHeader.pageTitle').text.replace('Регистратура донорского отделения (', '')[:-1])

	def list_of_directed_button_click(cls):
		while True:
			WebDriverWait(Driver.get(), 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'searchPage-title')]/a/input")))
			cls.list_of_directed_button.click()
			try:
				WebDriverWait(Driver.get(), 10).until(lambda driver: driver.find_element_by_xpath("//div[contains(@class, 'searchPage-title')]/a").get_attribute('href') == 'http://10.32.200.142/Donor')
				break
			except:
				continue

	def extended_search_click(cls, mode):
		if mode == 'open':
			while True:
				WebDriverWait(Driver.get(), 10).until(EC.element_to_be_clickable((By.ID, 'ExtendedSearchLink')))
				cls.extended_search_field.click()
				try:
					WebDriverWait(Driver.get(), 10).until(EC.element_to_be_clickable((By.ID, 'ExtendedName')))
					break
				except:
					continue
		elif mode == 'close':
			while True:
				WebDriverWait(Driver.get(), 10).until(EC.element_to_be_clickable((By.ID, 'ExtendedSearchLink')))
				cls.extended_search_field.click()
				try:
					WebDriverWait(Driver.get(), 10).until(lambda driver: driver.find_element_by_id('ExtendedName').is_displayed() == False)
					break
				except:
					continue

	def is_extended_search_closed(cls):
		return WebDriverWait(Driver.get(), 10).until(lambda driver: driver.find_element_by_id('extendedSearchBlock').is_displayed() == False)

	def is_extended_search_button_disable(cls):
		return Driver.get().find_element_by_id('ExtendedSearch').get_attribute('disabled')

	def filling_fio_in_extended_search(cls, lastname, firstname, middlename=''):
		if lastname:
			aistium.fill(lastname, cls.extended_lastname)
		if firstname:
			aistium.fill(firstname, cls.extended_firstname)
		if middlename:
			aistium.fill(middlename, cls.extended_middlename) #id не соответствует семантике

	def filling_region_in_extended_search(cls, region):
		WebDriverWait(Driver.get(), 10).until(EC.element_to_be_clickable((By.ID, 'searchFiasAddress_Region')))
		Driver.get().find_element_by_id('searchFiasAddress_Region').send_keys(region)
		while 1:
			try:
				WebDriverWait(Driver.get(), 2).until(EC.visibility_of_any_elements_located((By.CLASS_NAME, 'k-icon.k-loading')))
				continue
			except:
				reg_fias_address_region_listbox = WebDriverWait(Driver.get(), 5).until(EC.visibility_of_any_elements_located((By.ID, 'searchFiasAddress_Region_listbox')))
				reg_fias_address_region_listbox[0].click()
				break

	def ndp_filling_city_in_extended_search(cls, city):
		WebDriverWait(Driver.get(), 10).until(EC.element_to_be_clickable((By.ID, 'searchFiasAddress_City')))
		Driver.get().find_element_by_id('searchFiasAddress_City').send_keys(city)
		while 1:
			try:
				WebDriverWait(Driver.get(), 2).until(EC.visibility_of_any_elements_located((By.CLASS_NAME, 'k-icon.k-loading')))
				continue
			except:
				reg_fias_address_city_listbox = WebDriverWait(Driver.get(), 5).until(EC.visibility_of_any_elements_located((By.ID, 'searchFiasAddress_City_listbox')))
				reg_fias_address_city_listbox[0].click()
				break
		
	def ndp_filling_street_in_extended_search(cls, street):
		WebDriverWait(Driver.get(), 10).until(EC.element_to_be_clickable((By.ID, 'searchFiasAddress_Street'))).send_keys(street)
		time.sleep(2)
		while 1:
			try:
				WebDriverWait(Driver.get(), 2).until(EC.visibility_of_any_elements_located((By.CLASS_NAME, 'k-icon.k-loading')))
				continue
			except:
				reg_fias_address_street_listbox = WebDriverWait(Driver.get(), 5).until(EC.visibility_of_any_elements_located((By.ID, 'searchFiasAddress_Street_listbox')))
				reg_fias_address_street_listbox[0].click()
				break

	def ndp_filling_house_in_extended_search(cls, house):
		time.sleep(1)
		WebDriverWait(Driver.get(), 10).until(EC.element_to_be_clickable((By.ID, 'searchFiasAddress_House'))).send_keys(house)

	def filling_gender_in_extended_search(cls, gender):
		time.sleep(2)
		WebDriverWait(Driver.get(), 7).until(EC.visibility_of(cls.extended_search_select_gender_field))
		cls.extended_search_select_gender_field.click()
		time.sleep(2)
		genders_listbox = WebDriverWait(Driver.get(), 7).until(EC.visibility_of_any_elements_located((By.XPATH, '//*[@id="ExtendedGender_listbox"]/li')))
		for gen in genders_listbox:
			if gender == gen.text:
				gen.click()

	def filling_doc_type_in_extended_search(cls, doc_type):
		time.sleep(2)
		WebDriverWait(Driver.get(), 7).until(EC.visibility_of(Driver.get().find_element_by_xpath("//div[contains(@class, 'extendedSearchBlock-line')][3]/span/span/span[1]")))
		cls.extended_search_select_doc_type_field.click()
		doc_type_listbox = WebDriverWait(Driver.get(), 7).until(EC.visibility_of_any_elements_located((By.XPATH, '//*[@id="ExtendedDocumentType_listbox"]/li')))
		for dt in doc_type_listbox:
			if doc_type == dt.text:
				try:
					dt.click()
				except ElementNotInteractableException:
					pass

	def filling_doc_serie_in_extended_search(cls, doc_serie):
		time.sleep(1)
		Driver.get().execute_script("arguments[0].value='"+doc_serie+"';", Driver.get().find_element_by_id('ExtendedIdentityDocSeries'))

	def filling_doc_number_in_extended_search(cls, doc_number):
		time.sleep(1)
		Driver.get().execute_script("arguments[0].value='"+doc_number+"';", Driver.get().find_element_by_id('ExtendedIdentityDocNumber'))

	def get_lastname_from_extended_search(cls):
		Driver.get().execute_script("arguments[0].blur();", Driver.get().find_element_by_id('ExtendedSurname'))
		return Driver.get().find_element_by_id('ExtendedSurname').get_attribute('value')

	def get_firstname_from_extended_search(cls):
		Driver.get().execute_script("arguments[0].blur();", Driver.get().find_element_by_id('ExtendedName'))
		return Driver.get().find_element_by_id('ExtendedName').get_attribute('value')

	def get_middlename_from_extended_search(cls):
		Driver.get().execute_script("arguments[0].blur();", Driver.get().find_element_by_id('ExtendedLastName'))
		return Driver.get().find_element_by_id('ExtendedLastName').get_attribute('value')

	def get_gender_from_extended_search(cls):
		return Driver.get().execute_script("return jQuery(arguments[0]).text();", Driver.get().find_element_by_xpath("//div[contains(@class, 'extendedSearchBlock-line')][1]/div[1]/span/span/span[1]"))

	def get_region_from_extended_search(cls):
		Driver.get().execute_script("arguments[0].blur();", Driver.get().find_element_by_id('regFiasAddress_Region'))
		return Driver.get().find_element_by_id('regFiasAddress_Region').get_attribute('value')

	def get_donorid_from_extended_search(cls):
		Driver.get().execute_script("arguments[0].blur();", Driver.get().find_element_by_id('ExtendedRegistryNumber'))
		return Driver.get().find_element_by_id('ExtendedRegistryNumber').get_attribute('value')

	def get_barcode_from_extended_search(cls):
		Driver.get().execute_script("arguments[0].blur();", Driver.get().find_element_by_id('ExtendedDonationBarCode'))
		return Driver.get().find_element_by_id('ExtendedDonationBarCode').get_attribute('value')

	def get_birth_date_from_from_extended_search(cls):
		Driver.get().execute_script("arguments[0].blur();", Driver.get().find_element_by_id('ExtendedBirthDateFrom'))
		return Driver.get().find_element_by_id('ExtendedBirthDateFrom').get_attribute('value')

	def get_birth_date_to_from_extended_search(cls):
		Driver.get().execute_script("arguments[0].blur();", Driver.get().find_element_by_id('ExtendedBirthDateTo'))
		return Driver.get().find_element_by_id('ExtendedBirthDateTo').get_attribute('value')

	def get_next_donation_from_from_extended_search(cls):
		Driver.get().execute_script("arguments[0].blur();", Driver.get().find_element_by_id('ExtendedPreregistrationFrom'))
		return Driver.get().find_element_by_id('ExtendedPreregistrationFrom').get_attribute('value')

	def get_next_donation_to_from_extended_search(cls):
		Driver.get().execute_script("arguments[0].blur();", Driver.get().find_element_by_id('ExtendedPreregistrationTo'))
		return Driver.get().find_element_by_id('ExtendedPreregistrationTo').get_attribute('value')

	def get_document_serie_from_extended_search(cls):
		Driver.get().execute_script("arguments[0].blur();", Driver.get().find_element_by_id('ExtendedIdentityDocSeries'))
		return Driver.get().find_element_by_id('ExtendedIdentityDocSeries').get_attribute('value')

	def get_document_number_from_extended_search(cls):
		Driver.get().execute_script("arguments[0].blur();", Driver.get().find_element_by_id('ExtendedIdentityDocNumber'))
		return Driver.get().find_element_by_id('ExtendedIdentityDocNumber').get_attribute('value')

	def get_document_type_from_extended_search(cls):
		return str(Driver.get().execute_script("return jQuery(arguments[0]).text();", Driver.get().find_element_by_xpath("//div[contains(@class, 'extendedSearchBlock-line')][3]/span/span/span[1]")))

	def clear_localstorage(cls):
		Driver.get().get('javascript:localStorage.clear();')

	def reset_filters_click(cls):
		while True:
			WebDriverWait(Driver.get(), 10).until(EC.element_to_be_clickable((By.ID, 'ResetFilters'))).click()
			try:
				WebDriverWait(Driver.get(), 10).until(lambda driver: driver.find_element_by_id('ResetFilters').is_displayed() == False)
				break
			except:
				continue
			time.sleep(2)
		
	def reset_filters_is_not_on_page(cls):
		return WebDriverWait(Driver.get(), 10).until(lambda driver: driver.find_element_by_id('ResetFilters').is_displayed() == False)

	def newdonor_click(cls):
		while True:
			WebDriverWait(Driver.get(), 10).until(EC.element_to_be_clickable((By.ID, 'newdonor')))
			Driver.get().find_element_by_id('newdonor').click()
			try:
				WebDriverWait(Driver.get(), 10).until(EC.visibility_of_any_elements_located((By.ID, 'newdonor-window_wnd_title')))
				break
			except:
				continue
			time.sleep(2)

	def is_ndp_closed(cls):
		if WebDriverWait(Driver.get(), 10).until(lambda driver: driver.find_element_by_id('newdonor-window_wnd_title').is_displayed() == False):
			return True
		else:
			return False

	def ndp_filling_first_page(cls, lastname, firstname, middlename, birthdate, document_serie, document_number): #mandatory fields only (and middlename)
		WebDriverWait(Driver.get(), 10).until(EC.element_to_be_clickable((By.ID, 'LastName')))
		time.sleep(2)
		cls.last_name_field_ndp.send_keys(lastname)
		cls.first_name_field_ndp.send_keys(firstname)
		cls.middle_name_field_ndp.send_keys(middlename)
		if 'today' in birthdate:
			if len(birthdate.split(' ')) > 1:
				cls.birthdate_field_ndp.send_keys(date_calculation(birthdate))
			elif len(birthdate.split(' ')) == 1:
				d = datetime.date.today()
				cls.birthdate_field_ndp.send_keys(d.strftime('%d.%m.%Y'))
		else:
			cls.birthdate_field_ndp.send_keys(birthdate)
		Driver.get().execute_script("arguments[0].value='" + document_serie + "';", Driver.get().find_element(L['document_serie_field_ndp'][1], L['document_serie_field_ndp'][2]))
		Driver.get().execute_script("arguments[0].value='" + document_number + "';", Driver.get().find_element(L['document_number_field_ndp'][1], L['document_number_field_ndp'][2]))

	def ndp_first_page_clear(cls):
		WebDriverWait(Driver.get(), 10).until(EC.element_to_be_clickable((By.ID, 'LastName')))
		cls.document_number_field_ndp.clear()
		cls.last_name_field_ndp.clear()
		cls.first_name_field_ndp.clear()
		cls.middle_name_field_ndp.clear()
		cls.birthdate_field_ndp.clear()
		cls.document_serie_field_ndp.clear()
		cls.identity_document_issue_date.clear()
		cls.identity_document_issued_by.clear()
		cls.snils_field.clear()
		cls.ndp_birth_place.clear()

	def ndp_first_page_check_values_of_mandatory_fields(cls, expected_lastname, expected_firstname, expected_birthdate, expected_document_serie, expected_document_number):
		WebDriverWait(Driver.get(), 10).until(EC.element_to_be_clickable((By.ID, 'LastName')))
		assert Driver.get().find_element_by_id('LastName').get_attribute('value') == expected_lastname
		assert Driver.get().find_element_by_id('FirstName').get_attribute('value') == expected_firstname
		assert Driver.get().find_element_by_id('BirthDate').get_attribute('value') == expected_birthdate
		assert Driver.get().find_element_by_id('IdentityDocument_Serie').get_attribute('value') == expected_document_serie
		assert Driver.get().find_element_by_id('IdentityDocument_Number').get_attribute('value') == expected_document_number
		time.sleep(2)

	def is_birthdate_field_focused(cls):
		return WebDriverWait(Driver.get(), 10).until(lambda driver: 'focused' in driver.find_element_by_xpath('//*[@class="margin-bottom-20"][4]/span[2]/span[1]').get_attribute('class'))

	def ndp_filling_birth_place(cls, birthplace):
		cls.ndp_birth_place.send_keys(birthplace)

	def ndp_select_document_type(cls, document_type):
		time.sleep(2)
		WebDriverWait(Driver.get(), 7).until(EC.visibility_of(cls.document_type_select_field))
		cls.document_type_select_field.click()
		document_type_listbox = WebDriverWait(Driver.get(), 7).until(EC.visibility_of_any_elements_located((By.XPATH, '//*[@id="IdentityDocType_listbox"]/li')))
		for dt in document_type_listbox:
			if document_type == dt.text:
				dt.click()

	def ndp_get_document_type_value(cls):
		time.sleep(2)
		WebDriverWait(Driver.get(), 7).until(EC.visibility_of(cls.document_type_select_field))
		return Driver.get().find_element_by_css_selector('span.k-dropdown:nth-child(1) > span:nth-child(1) > span:nth-child(1)').text

	def ndp_get_document_type_listbox(cls):
		time.sleep(2)
		WebDriverWait(Driver.get(), 7).until(EC.visibility_of(cls.document_type_select_field))
		document_type_listbox = []
		cls.document_type_select_field.click()
		for i in WebDriverWait(Driver.get(), 7).until(EC.visibility_of_any_elements_located((By.XPATH, '//*[@id="IdentityDocType_listbox"]/li'))):
			document_type_listbox.append(i.text)
		return document_type_listbox

	def filling_identity_document_issue_date(cls, date):
		if 'today' in date:
			if len(date.split('+')) > 1:
				d = datetime.date.today() + relativedelta(days=+int(date.split('+')[1]))
				cls.identity_document_issue_date.send_keys(d.strftime('%d.%m.%Y'))
			elif len(date.split('+')) == 1:
				d = datetime.date.today()
				cls.identity_document_issue_date.send_keys(d.strftime('%d.%m.%Y'))
		else:
			cls.identity_document_issue_date.send_keys(date)

	def identity_document_issued_date_focusout(cls):
		Driver.get().execute_script("$('"+L['identity_document_issue_date'][2]+"').focusout();")

	def identity_document_issued_by_clear(cls):
		cls.identity_document_issued_by.clear()
		time.sleep(1)

	def ndp_filling_snils(cls, snils):
		cls.snils_field.send_keys(snils)

	def expected_identity_document_issue_date(cls, date):
		if 'today' in date:
			if len(date.split('+')) > 1:
				d = datetime.date.today() + relativedelta(days=+int(date.split('+')[1]))
				return d.strftime('%d.%m.%Y')
			elif len(date.split('+')) == 1:
				d = datetime.date.today()
				return d.strftime('%d.%m.%Y')
		else:
			return date

	def get_validation_message_text(cls):
		WebDriverWait(Driver.get(), 7).until(EC.presence_of_element_located((By.CLASS_NAME, 'validation-summary-errors.k-block.k-error-colored')))
		return Driver.get().find_element_by_class_name('validation-summary-errors.k-block.k-error-colored').find_elements_by_tag_name('li')[0].text

	def get_alert_text(cls, mode='rep'):
		WebDriverWait(Driver.get(), 7).until(lambda driver: driver.find_element_by_id('alert-popup').is_displayed())
		if mode == 'rep':
			return cls.alert.text.replace('\n', " ")
		else:
			return cls.alert.text

	def select_gender(cls, donors_gender):
		time.sleep(1)
		if donors_gender == 'female':
			cls.ndp_female_gender.click()
		elif donors_gender == 'male':
			cls.ndp_male_gender.click()
		else:
			pass

	def check_saved_gender(cls, expected_result):
		if expected_result == 'Мужской':
			assert Driver.get().find_element_by_id('Gender1').get_attribute("checked") == "true"
			return 'Мужской'
		elif expected_result == 'Женский':
			assert Driver.get().find_element_by_id('Gender2').get_attribute("checked") == "true"
			return 'Женский'

	def check_is_agree_persional_data_processing(cls, expected_result):
		if expected_result == 'true':
			assert Driver.get().find_element_by_id('IsAgreePersionalDataProcessing').get_attribute("checked") == "true"
		elif expected_result == 'false':
			Driver.get().find_element_by_id('IsAgreePersionalDataProcessing').get_attribute("checked") == None

	def check_is_message_agree(cls, expected_result):
		if expected_result == 'true':
			assert Driver.get().find_element_by_id('IsMessageAgree').get_attribute("checked") == "true"
		elif expected_result == 'false':
			Driver.get().find_element_by_id('IsMessageAgree').get_attribute("checked") == None

	def get_is_agree_persional_data_processing_value(cls):
		return Driver.get().find_element_by_id('IsAgreePersionalDataProcessing').get_attribute("checked")

	def get_is_message_agree_value(cls):
		return Driver.get().find_element_by_id('IsMessageAgree').get_attribute("checked")

	def if_donor_is_in_local_cabinet(cls):
		while True:
			try:
				WebDriverWait(Driver.get(), 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.right')))
				while Driver.get().find_element_by_css_selector('input.right').get_attribute('value') != 'Добавить нового':
					Driver.get().find_element_by_css_selector('input.right').click()
			except:
				WebDriverWait(Driver.get(), 7).until(EC.element_to_be_clickable((By.ID, 'regFiasAddress_Region')))
				break

	def ndp_results_by_fic_is_on_the_page(cls):
		WebDriverWait(Driver.get(), 10).until(lambda driver: driver.find_element_by_id('newdonor-window_wnd_title').text == 'РЕЗУЛЬТАТЫ ПОИСКА В ФИЦ')

	def ndp_results_by_fic_get_grid_values(cls, column, row, mode='get_value'):
		columns = Driver.get().find_element_by_id('similar-donors').find_elements_by_tag_name('th')
		for i in columns:
			if i.text == column:
				ind = columns.index(i)
		row = Driver.get().find_element_by_xpath('//*[@id="similar-donors"]/div[2]/table').find_elements_by_tag_name('tr')[row]
		Driver.get().execute_script("arguments[0].scrollIntoView();", row)
		value = row.find_elements_by_tag_name('td')[ind]
		Driver.get().execute_script("arguments[0].scrollIntoView();", value)
		if mode == 'get_value':
			return value.text
		elif mode == 'click':
			value.click()

	def query_to_fic_get_fullname(cls):
		WebDriverWait(Driver.get(), 15).until(lambda driver: driver.title == 'Запрос в ЕИБД')
		return Driver.get().find_element_by_css_selector('span.margin-right-10').text.split(',')[0]

	def ndp_second_page_loaded(cls):
		WebDriverWait(Driver.get(), 15).until(EC.element_to_be_clickable((By.ID, 'regFiasAddress_Region')))
		WebDriverWait(Driver.get(), 10).until(EC.element_to_be_clickable((By.ID, 'save-newdonor')))
		time.sleep(1)

	def ndp_fias_address_clear(cls):
		cls.reg_fias_address_region.clear()
		time.sleep(2)
		cls.reg_fias_address_region.send_keys(Keys.ENTER)

	def ndp_filling_contacts(cls, mobile_phone, phone, email):
		cls.ndp_mobile_phone.send_keys(mobile_phone)
		cls.ndp_phone.send_keys(phone)
		cls.ndp_email.send_keys(email)

	def ndp_phone_clear(cls):
		cls.ndp_phone.clear()

	def ndp_contacts_clear(cls):
		cls.ndp_mobile_phone.clear()
		cls.ndp_phone.clear()
		cls.ndp_email.clear()

	def ndp_filling_region(cls, region):
		WebDriverWait(Driver.get(), 10).until(EC.element_to_be_clickable((By.ID, 'regFiasAddress_Region')))
		Driver.get().find_element_by_id('regFiasAddress_Region').send_keys(region)
		while 1:
			try:
				WebDriverWait(Driver.get(), 2).until(EC.visibility_of_any_elements_located((By.CLASS_NAME, 'k-icon.k-loading')))
				continue
			except:
				reg_fias_address_region_listbox = WebDriverWait(Driver.get(), 5).until(EC.visibility_of_any_elements_located((By.ID, 'regFiasAddress_Region_listbox')))
				reg_fias_address_region_listbox[0].click()
				break

	def ndp_filling_city(cls, city):
		WebDriverWait(Driver.get(), 10).until(EC.element_to_be_clickable((By.ID, 'regFiasAddress_City')))
		Driver.get().find_element_by_id('regFiasAddress_City').send_keys(city)
		while 1:
			try:
				WebDriverWait(Driver.get(), 2).until(EC.visibility_of_any_elements_located((By.CLASS_NAME, 'k-icon.k-loading')))
				continue
			except:
				reg_fias_address_city_listbox = WebDriverWait(Driver.get(), 5).until(EC.visibility_of_any_elements_located((By.ID, 'regFiasAddress_City_listbox')))
				reg_fias_address_city_listbox[0].click()
				break
		
	def ndp_filling_street(cls, street):
		Driver.get().find_element_by_id('regFiasAddress_Street').send_keys(street)
		time.sleep(2)
		while 1:
			try:
				WebDriverWait(Driver.get(), 2).until(EC.visibility_of_any_elements_located((By.CLASS_NAME, 'k-icon.k-loading')))
				continue
			except:
				reg_fias_address_street_listbox = WebDriverWait(Driver.get(), 5).until(EC.visibility_of_any_elements_located((By.ID, 'regFiasAddress_Street_listbox')))
				reg_fias_address_street_listbox[0].click()
				break

	def ndp_filling_house(cls, house):
		cls.reg_fias_address_house.send_keys(house, Keys.ENTER)
		time.sleep(1)

	def ndp_filling_building(cls, building):
		cls.reg_fias_address_building.send_keys(building)

	def ndp_filling_structure(cls, structure):
		cls.reg_fias_address_structure.send_keys(structure)

	def ndp_filling_flat(cls, flat):
		cls.reg_fias_address_office.send_keys(flat)

	def ndp_job_or_study_place_clear(cls):
		Driver.get().find_elements_by_class_name('k-input.JobInfo')[0].clear()
		cls.job_position.clear()
		Driver.get().find_elements_by_class_name('k-input.JobInfo')[1].clear()

	def ndp_social_statuses_list_on_form(cls):
		statuses_gui = []
		for i in WebDriverWait(Driver.get(), 10).until(EC.visibility_of_any_elements_located((By.XPATH, '//*[@id="SocialStatus_listbox"]/li'))):
			statuses_gui.append(Driver.get().execute_script("return jQuery(arguments[0]).text();", i))
		return statuses_gui

	def ndp_filling_social_status(cls, social_status):
		WebDriverWait(Driver.get(), 7).until(lambda driver: driver.find_elements_by_class_name('k-input.JobInfo')[1].is_displayed() == True)
		Driver.get().find_elements_by_class_name('k-input.JobInfo')[1].send_keys(social_status)
		ndp_social_status_listbox =  WebDriverWait(Driver.get(), 10).until(EC.visibility_of_any_elements_located((By.XPATH, '//*[@id="SocialStatus_listbox"]/li')))
		for i in ndp_social_status_listbox:
				if social_status.lower() == i.text.lower():
					Driver.get().execute_script("arguments[0].scrollIntoView();", i)
					try:
						i.click()
					except:
						continue

	def ndp_typing_social_status(cls, social_status):
		WebDriverWait(Driver.get(), 7).until(lambda driver: driver.find_elements_by_class_name('k-input.JobInfo')[1].is_displayed() == True)
		Driver.get().find_elements_by_class_name('k-input.JobInfo')[1].send_keys(social_status)

	def ndp_social_status_clear(cls):
		WebDriverWait(Driver.get(), 7).until(lambda driver: driver.find_elements_by_class_name('k-input.JobInfo')[1].is_displayed() == True)
		Driver.get().find_elements_by_class_name('k-input.JobInfo')[1].clear()
	
	def ndp_choose_social_status_from_list(cls, expected):
		ndp_social_status_listbox =  WebDriverWait(Driver.get(), 10).until(EC.visibility_of_any_elements_located((By.XPATH, '//*[@id="SocialStatus_listbox"]/li')))
		for i in ndp_social_status_listbox:
			if expected.lower() == i.text.lower():
				Driver.get().execute_script("arguments[0].scrollIntoView();", i)
				try:
					i.click()
				except:
					continue

	def ndp_social_status_listbox_is_empty(cls):
		time.sleep(3)
		return WebDriverWait(Driver.get(), 5).until(lambda driver: driver.find_element_by_xpath('//*[@id="SocialStatus_listbox"]').is_displayed() == False)

	def ndp_social_status_focusout(cls):
		Driver.get().execute_script('$("#step2 > div:nth-child(16) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1) > input:nth-child(1)").focusout();')

	def is_deferral_type_field_disabled(cls):
		return Driver.get().find_element(L['ndp_deferral_type'][1], L['ndp_deferral_type'][2]).get_attribute('disabled'), Driver.get().find_element(L[ndp_deferral_type][1], L[ndp_deferral_type][2]).get_attribute('readonly')

	def ndp_filling_deferral(cls, deferral_name, mode='correct_input'):
		WebDriverWait(Driver.get(), 10).until(EC.visibility_of(cls.ndp_deferral_field))
		if mode == 'correct_input':
			cls.ndp_deferral_field.send_keys(deferral_name)
			ndp_deferral_listbox_first_li = WebDriverWait(Driver.get(), 3).until(EC.visibility_of_any_elements_located((By.XPATH, '//*[@id="DeferralTypeIdNewDonor_listbox"]/li[1]')))
			for i in ndp_deferral_listbox_first_li:
				if deferral_name.lower() == i.text.lower():
					try:
						i.click()
					except:
						continue
			WebDriverWait(Driver.get(), 10).until(lambda driver: driver.find_element_by_id('DeferralTypeNameNewDonor').value_of_css_property('background-color') != 'rgb(255, 255, 255)')
		elif mode == 'incorrect_input':
			cls.ndp_deferral_field.send_keys(deferral_name)
		else:
			cls.ndp_deferral_field.send_keys(deferral_name)
			WebDriverWait(Driver.get(), 3).until(EC.visibility_of_any_elements_located((By.XPATH, '//*[@id="DeferralTypeIdNewDonor_listbox"]')))

	def ndp_deferrals_press_enter(cls):
		WebDriverWait(Driver.get(), 10).until(EC.visibility_of(cls.ndp_deferral_field))
		cls.ndp_deferral_field.send_keys(Keys.ENTER)

	def ndp_deferrals_listbox(cls):
		return Driver.get().find_elements_by_id('DeferralTypeIdNewDonor_listbox')[2].find_elements_by_tag_name('li')

	def is_deferral_listbox_empty(cls):
		time.sleep(2)
		WebDriverWait(Driver.get(), 3).until_not(EC.visibility_of_any_elements_located((By.XPATH, '//*[@id="DeferralTypeIdNewDonor_listbox"]')))

	def ndp_deferral_list_on_form(cls):
		deferrals_gui = []
		for defer in WebDriverWait(Driver.get(), 5).until(EC.visibility_of_any_elements_located((By.XPATH, '//*[@id="DeferralTypeIdNewDonor_listbox"]/li'))):
			deferrals_gui.append(Driver.get().execute_script("return jQuery(arguments[0]).text();", defer))
		return deferrals_gui

	def ndp_get_deferral_type_color(cls):
		return Driver.get().find_element(L['ndp_deferral_type'][1], L['ndp_deferral_type'][2]).value_of_css_property('background-color')

	def ndp_filling_donation_type(cls, donation_type, mode='equals'):
		WebDriverWait(Driver.get(), 7).until(lambda driver: cls.ndp_donation_type_field.is_displayed() == True)
		cls.ndp_donation_type_field.send_keys(donation_type)
		if mode == 'equals':
			ndp_donation_type_listbox =  WebDriverWait(Driver.get(), 10).until(EC.visibility_of_any_elements_located((By.XPATH, '//*[@id="NextDonationType_listbox"]')))[0].find_elements_by_tag_name('li')
			for i in ndp_donation_type_listbox:
					if donation_type.lower() == i.text.lower():
						Driver.get().execute_script("arguments[0].scrollIntoView();", i)
						try:
							i.click()
						except:
							continue
		elif mode == 'first_li':
			ndp_donation_type_listbox =  WebDriverWait(Driver.get(), 10).until(EC.visibility_of_any_elements_located((By.XPATH, '//*[@id="NextDonationType_listbox"]')))[0].find_elements_by_tag_name('li')
			ndp_donation_type_listbox[0].click()
		elif mode == 'does_not_exists':
			time.sleep(2)
			return WebDriverWait(Driver.get(), 5).until(lambda driver: driver.find_element_by_xpath('//*[@id="NextDonationType_listbox"]').is_displayed() == False)


	def ndp_donation_types_list_on_form(cls):
		types_gui = []
		for i in WebDriverWait(Driver.get(), 10).until(EC.visibility_of_any_elements_located((By.XPATH, '//*[@id="NextDonationType_listbox"]/li'))):
			types_gui.append(Driver.get().execute_script("return jQuery(arguments[0]).text();", i))
		return types_gui

	def ndp_donation_type_clear(cls):
		WebDriverWait(Driver.get(), 7).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.k-combobox:nth-child(2) > span:nth-child(1) > input:nth-child(1)'))).clear()

	def ndp_donation_type_focus_out(cls):
		Driver.get().execute_script("$('span.k-combobox:nth-child(2) > span:nth-child(1) > input:nth-child(1)').focusout();")

	def ndp_get_donation_type(cls):
		return Driver.get().find_element_by_css_selector('span.k-combobox:nth-child(2) > span:nth-child(1) > input:nth-child(1)').get_attribute('value')

	def ndp_get_donation_type_color(cls):
		time.sleep(1)
		return Driver.get().find_element_by_css_selector('span.k-combobox:nth-child(2) > span:nth-child(1) > input:nth-child(1)').value_of_css_property('background-color')

	def ndp_get_donation_type_text_color(cls):
		time.sleep(1)
		return Driver.get().find_element_by_css_selector('span.k-combobox:nth-child(2) > span:nth-child(1) > input:nth-child(1)').value_of_css_property('color')

	def ndp_second_page_check_values_of_mandatory_fields(cls): #mandatory fields only
		return Driver.get().find_element(L['reg_fias_address_region'][1], L['reg_fias_address_region'][2]).get_attribute('value'), \
			   Driver.get().find_element(L['reg_fias_address_city'][1], L['reg_fias_address_city'][2]).get_attribute('value'), \
			   Driver.get().find_element(L['reg_fias_address_street'][1], L['reg_fias_address_street'][2]).get_attribute('value'), \
			   Driver.get().find_element(L['reg_fias_address_house'][1], L['reg_fias_address_house'][2]).get_attribute('value')

	def ndp_get_contacts_values(cls):
		return Driver.get().find_element(L['ndp_mobile_phone'][1], L['ndp_mobile_phone'][2]).get_attribute('value'), \
			   Driver.get().find_element(L['ndp_phone'][1], L['ndp_phone'][2]), \
			   Driver.get().find_element(L['ndp_email'][1], L['ndp_email'][2]).get_attribute('value')

	def ndp_get_job_information(cls):
		return Driver.get().find_elements_by_class_name('k-input.JobInfo')[0].get_attribute('value'), Driver.get().find_element_by_id('JobPosition').get_attribute('value'), Driver.get().find_elements_by_class_name('k-input.JobInfo')[1].get_attribute('value')

	def ndp_save_new_donor(cls, mode):
		if mode == 'success':
			WebDriverWait(Driver.get(), 15).until(EC.presence_of_element_located((By.ID, 'IsFactAddressEqualsRegAddress')))
			time.sleep(2)
			cls.save_new_donor_button.click()
			WebDriverWait(Driver.get(), 10).until(EC.visibility_of_any_elements_located((By.CLASS_NAME, 'comment-title-block')))
		if mode == 'check':
			time.sleep(2)
			cls.save_new_donor_button.click()

	def mc_donor_has_not_deferral(cls): #здесь и далее: mc - mini-card
		WebDriverWait(Driver.get(), 10).until_not(lambda driver: driver.find_element_by_class_name('deferralinfo-block.margin-bottom-10').is_displayed())

	def get_email_from_minicard(cls):
		try:
			WebDriverWait(Driver.get(), 10).until(lambda driver: driver.find_element_by_class_name('contacts-email.contacts-info').is_displayed())
			return Driver.get().find_element_by_class_name('contacts-email.contacts-info').text
		except:
			pass

	def get_donation_type_value_from_minicard(cls):
		return Driver.get().find_element_by_class_name('person-card-details-donation-label').find_elements_by_tag_name('span')[1].text

	def get_address_from_minicard(cls):
		split_minicard_address = cls.minicard_address.text.split(', ')
		try:
			int(split_minicard_address[0])
			del(split_minicard_address[0])
		except:
			pass
		return split_minicard_address

	def get_accurate_address(cls):
		try:
			WebDriverWait(Driver.get(), 10).until(lambda driver: driver.find_element_by_id('person-card-address-fact').is_displayed())
			return Driver.get().find_element_by_id('person-card-address-fact').text
		except:
			pass

	def get_gender_from_minicard(cls):
		return Driver.get().find_element_by_class_name('person-card-details-data-block ').find_elements_by_tag_name('span')[1].text

	def is_element_positioned(cls, elem_id):
		return Driver.get().execute_script("return document.activeElement.getAttribute('id');") == elem_id

	def is_simple_search_text_selected(cls):
		return Driver.get().execute_script('return arguments[0].value.substring(arguments[0].selectionStart, arguments[0].selectionEnd);', Driver.get().find_element_by_id('SimpleSearchText'))

	def get_birthdate_from_minicard(cls):
		return Driver.get().find_element_by_class_name('person-card-details-data-block ').find_elements_by_tag_name('span')[0].text

	def get_document_serie_and_number(cls):
		return Driver.get().find_element_by_class_name('person-card-details-document-block').find_element_by_tag_name('span').text

	def ndp_place_list_on_form(cls):
		places_gui = []
		for place in WebDriverWait(Driver.get(), 7).until(EC.visibility_of_any_elements_located((By.XPATH, '//*[@id="JobInfo_listbox"]/li'))):
			places_gui.append(Driver.get().execute_script("return jQuery(arguments[0]).text();", place))
		return places_gui

	def get_genders_listbox_from_extended_search(cls):
		WebDriverWait(Driver.get(), 7).until(EC.visibility_of(cls.extended_search_select_gender_field))
		genders_listbox = []
		cls.extended_search_select_gender_field.click()
		for i in WebDriverWait(Driver.get(), 7).until(EC.visibility_of_any_elements_located((By.XPATH, '//*[@id="ExtendedGender_listbox"]/li'))):
			genders_listbox.append(i.text)
		return genders_listbox

	def get_document_types_listbox_from_extended_search(cls):
		WebDriverWait(Driver.get(), 7).until(EC.visibility_of(cls.extended_search_select_doc_type_field))
		document_types_listbox = []
		cls.extended_search_select_doc_type_field.click()
		for i in WebDriverWait(Driver.get(), 7).until(EC.visibility_of_any_elements_located((By.XPATH, '//*[@id="ExtendedDocumentType_listbox"]/li'))):
			document_types_listbox.append(i.text)
		return document_types_listbox

	def get_donor_minicard_fio_color(cls):
		return convert_to_hex(Driver.get().find_element(L['fio_minicard'][1], value=L['fio_minicard'][2]).value_of_css_property('color'))

	def minicard_get_job_place(cls):#*********2.43 version only
		return Driver.get().execute_script('return arguments[0].nextSibling.nodeValue.trim()', Driver.get().find_element(by=L['minicard_job_place_label'][1], value=L['minicard_job_place_label'][2]))

	def get_diseases_only_active_value(cls):
		if Driver.get().find_element(L['diseases_only_active'][1], value=L['diseases_only_active'][2]).get_attribute("checked") == 'true':
			return 'true'
		else:
			return 'false'