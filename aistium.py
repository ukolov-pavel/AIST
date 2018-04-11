from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from additional_functions import convert_to_hex
from base import Driver, BaseTest
import time, locators

class element_is_visible(object):
	'''Принимает либо элемент и список элементов, либо локаторы (при этом нужно указать список из элементов и их локаторов: 
	например, 
	>>> from locators import donors_registry_locators as L
	>>> element_is_visible(locators_list=locators, element_name='confirm_popup')
	Если на вход подаётся список элементов, то возвращается первый видимый элемент из этого списка.'''

	def __init__(self, elements=None, locators_list=None, element_name=None):
		self.elements = elements
		self.locators_list = locators_list
		self.element_name = element_name
	def __call__(self, ignored):
		if self.elements != None:
			if type(self.elements) == list:
				self.elems = [element for element in self.elements if EC._element_if_visible(element)]
				if len(self.elems) > 0:
					self.elem = self.elems[0]
					return self.elem
			else:
				self.elem = EC._element_if_visible(self.elements)
				return self.elem
		elif self.locators_list != None and self.element_name != None:
			for key, val in self.locators_list.items():
				if key == self.element_name:
					if val[0] == 'Finds':
						self.elems = [element for element in Driver.get().find_elements(val[1], val[2]) if EC._element_if_visible(element)]
						if len(self.elems) > 0:
							self.elem = self.elems[0]
							return self.elem
					elif val[0] == 'Find':
						self.elem = EC._element_if_visible(Driver.get().find_element(val[1], val[2]))
						return self.elem
				else: pass

def waiting_for_element_is_visible(elements=None, locators_list=None, element_name=None, time_out=BaseTest.timeout):
	try:
		if elements != None:
			return WebDriverWait(Driver.get(), time_out).until(lambda x: element_is_visible(elements=elements).__call__(ignored=None))
		elif locators_list != None and element_name != None:
			return WebDriverWait(Driver.get(), time_out).until(lambda x: element_is_visible(locators_list=locators_list, element_name=element_name).__call__(ignored=None))
	except:
		raise NoSuchElementException('AIST-element is not visible')

'''def element_is_generated(locators_list, locator):
	try:
		return WebDriverWait(Driver.get(), BaseTest.timeout).until(EC.visibility_of_any_elements_located((locators_list[locator][1], locators_list[locator][2])))[0]
	except:
		return False'''

def element_is_on_the_page(locators_list, element_name):
	'''Принимает только список локаторов и имя элемента. Сам элемент не принимает.'''
	try:
		waiting_for_element_is_visible(locators_list=locators_list, element_name=element_name, time_out=5)
		return True
	except:
		return False

def switch_to_target_tab(ind):
	Driver.get().switch_to.window(Driver.get().window_handles[ind])

def get_text(elements=None, locators_list=None, element_name=None):
	if elements:
		return waiting_for_element_is_visible(elements=elements).text
	elif locators_list and element_name:
		return waiting_for_element_is_visible(locators_list=locators_list, element_name=element_name).text

def get_value(elements=None, locators_list=None, element_name=None):
	if elements:
		return waiting_for_element_is_visible(elements=elements).get_attribute('value')
	elif locators_list and element_name:
		return waiting_for_element_is_visible(locators_list=locators_list, element_name=element_name).get_attribute('value')

def get_background_color(elements=None, locators_list=None, element_name=None):
	if elements:
		return convert_to_hex(waiting_for_element_is_visible(elements=elements).value_of_css_property('background-color'))
	elif locators_list and element_name:
		return convert_to_hex(waiting_for_element_is_visible(locators_list=locators_list, element_name=element_name).value_of_css_property('background-color'))

def click_on(elements=None, locators_list=None, element_name=None):
	time.sleep(2)
	if elements:
		element = waiting_for_element_is_visible(elements=elements)
		if element.is_enabled() == True:
			element.click()
		else:
			raise ElementClickInterceptedException('AIST-element is not clickable')
	elif locators_list and element_name:
		element = waiting_for_element_is_visible(locators_list=locators_list, element_name=element_name)
		if element.is_enabled() == True:
			element.click()
		else:
			raise ElementClickInterceptedException('AIST-element is not clickable')

def fill(value, elements=None, locators_list=None, element_name=None):
	if elements:
		element = waiting_for_element_is_visible(elements=elements)
		if element.is_enabled() == True:
			element.send_keys(value)
		else:
			raise ElementClickInterceptedException('AIST-element is not enabled')
	elif locators_list and element_name:
		element = waiting_for_element_is_visible(locators_list=locators_list, element_name=element_name)
		if element.is_enabled() == True:
			element.send_keys(value)
		else:
			raise ElementClickInterceptedException('AIST-element is not enabled')

def element_is_enabled(elements):#доработка
	time.sleep(1)
	if type(elements) == list:
		list_of_enabled_elements = []
		for elem in elements:
			if elem.is_enabled() == True and elem.is_displayed() == True:
				list_of_enabled_elements.append(elem)
		if len(list_of_enabled_elements) > 0:
			return True
		else:
			return False
	else:
		if elements.is_enabled() == True and elements.is_displayed() == True:
			return True
		else:
			return False