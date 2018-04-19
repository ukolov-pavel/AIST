#>>> pip install bs4

import requests
from base import BaseTest, Session
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import codecs


class GetCurrentSettings(object):

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

	def get_raw_settings(self):
		t = self.session.get(BaseTest.stand+self.url, headers=self.headers)
		soup = BeautifulSoup(t.text, 'html.parser')
		for scr in soup.findAll('script'):
			if scr.get('src') == '/bundles/Setting/' + self.url.split('/')[-1] + '?v=' + self.script:
				str_settings = scr
			else:
				pass
		settings = []
		for sett in str(str_settings.findNextSibling()).split('\r\n'):
			try:
				sett = sett.strip()
				if sett.startswith('model.'):
					settings.append(sett[6:])
			except:
				pass
		return settings

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


class TurnBackDonorSettings(GetCurrentSettings):

	def __init__(self, script='k3PZb1rGL2OJptx7_Wq4Yu8kZSWVRVievzK9AFvF6b01', url='/Admin/Setting/EditDonor'):
		GetCurrentSettings.__init__(self, url, script)

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
