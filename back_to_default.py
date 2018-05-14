#>>> pip install bs4

from base import BaseTest, Session
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import codecs
import json


class Settings(object):

	def __init__(self, url, script):
		self.url = url
		self.session = Session.get()
		self.headers = {'Referer': BaseTest.stand+self.url, 'Content-Type': 'application/x-www-form-urlencoded'}
		self.script = script
		payload = {'Login': BaseTest.login, 'Password': BaseTest.password}
		login_url = BaseTest.stand + '/Auth/LogOn'
		self.session.post(url=login_url, data=payload)
		self.cookies = self.session.cookies.get_dict()
		self.headers = {**self.headers, **self.cookies}

	def get_raw_settings(self, mode='model'):
		t = self.session.get(BaseTest.stand+self.url, headers=self.headers)
		soup = BeautifulSoup(t.text, 'html.parser')
		for scr in soup.findAll('script'):
			if scr.get('src') == '/bundles/Setting/' + self.url.split('/')[-1] + '?v=' + self.script:
				str_settings = scr
			else:
				pass
		settings = []
		if mode == 'model':
			for sett in str(str_settings.findNextSibling()).split('\r\n'):
				try:
					sett = sett.strip()
					if sett.startswith('model.'):
						settings.append(sett[6:])
				except:
					pass
			return settings
		else:
			return str_settings

	def get_settings(self):
		dic = {}
		for i in self.get_raw_settings():
			dic[i.split('=')[0][:-1]] = i.split('=')[1][1:-1]
		for i in dic:
			dic[i] = dic[i].strip("'")
		return dic

	def post_settings(self, settings_dic):
		request_body_list = []
		for i in settings_dic:
			request_body_list.append(i + '=' + settings_dic[i])
		self.request_body = '&'.join(request_body_list)
		return self.session.post(BaseTest.stand + self.url, data=self.request_body, headers=self.headers)


class DonorSettings(Settings):

	def __init__(self, script='k3PZb1rGL2OJptx7_Wq4Yu8kZSWVRVievzK9AFvF6b01', url='/Admin/Setting/EditDonor'):
		Settings.__init__(self, url, script)

	def get_settings(self):
		settings = self.get_raw_settings()
		dic = {}
		dic['ViewTabName'] = 'EditDonor'
		dic['NextTabName'] = ''
		for i in settings:
			if i.startswith('HonorableDonorSettings') == True:
				i = i.replace(i[22], '[', 1)
				i = i.replace('__', '].')
				i = i.replace(i.split('=')[0], quote_plus(i.split('=')[0]))
			dic[i.split('=')[0][:-1]] = i.split('=')[1][1:-1]
		for i in dic:
			dic[i] = dic[i].strip("'")
		dic['DonorSubscription'] = quote_plus(
			dic['DonorSubscription'].replace('&quot;', '"').replace('\\', '\r' + '\\').replace('\\n', codecs.decode('\\n', 'unicode_escape')))
		for k, v in dic.items():
			dic[k] = v.strip(' ')
		return dic

	def edit_donor_settings(self, **edited_settings):
		current_settings = self.get_settings()
		updated = {}
		for k, v in edited_settings.items():
			updated[quote_plus(k)] = v
		updated_donor_settings = {**current_settings, **updated}
		return self.post_settings(updated_donor_settings)


class DonationsSettings(Settings):

	def __init__(self, script='Q5M5c4m_DiE8N-vPmMI6ahTLJDkExwefMRrV3gZcX_U1', url='/Admin/Setting/EditDonation'):
		Settings.__init__(self, url, script)

	def get_settings(self):
		settings = self.get_raw_settings()
		str_settings = self.get_raw_settings('numbers')
		str_numbers = str_settings.find_next_sibling().get_text().split('\r\n')[4].strip().strip('DonationTabDiv.Init')[1:-2]
		json_numbers = json.loads(str_numbers)
		days = []
		for y in range(len(json_numbers)):
			for i in json_numbers[y]['Days']:
				if int(i) <= 5:
					days.append(dict(Days=json_numbers[y]['Days'][i]['Count'], Id=json_numbers[y]['Days'][i]['Id']))
		dic = {}
		dic['ViewTabName'] = 'EditDonation'
		dic['NextTabName'] = ''
		for i in settings:
			dic[i.split('=')[0][:-1]] = i.split('=')[1][1:-1]
		for i in dic:
			dic[i] = dic[i].strip("'")
		for i in range(36):
			dic[quote_plus('EditDelays[' + str(i) + '].Id')] = str(days[i]['Id'])
			dic[quote_plus('EditDelays[' + str(i) + '].Days')] = str(days[i]['Days'])
		return dic

	def edit_donations_settings(self, **edited_settings):
		current_settings = self.get_settings()
		updated = {}
		for k, v in edited_settings.items():
			updated[quote_plus(k)] = v
		updated_donations_settings = {**current_settings, **updated}
		return self.post_settings(updated_donations_settings)