#>>> pip install bs4

import requests
from base import BaseTest
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import codecs

payload = {'Login':BaseTest.login, 'Password':BaseTest.password}

url = BaseTest.stand+'/Auth/LogOn'

s = requests.Session()

s.post(url, data=payload)

constant_headers = {'Referer': BaseTest.stand+'/Admin/Setting/EditDonor', 'Content-Type': 'application/x-www-form-urlencoded'}

cookies = s.cookies.get_dict()

headers = {**constant_headers, **cookies}

t = s.get(BaseTest.stand+'/Admin/Setting/EditDonor', headers=headers)

soup = BeautifulSoup(t.text, 'html.parser')

for script in soup.findAll('script'):
	if script.get('src') == '/bundles/Setting/EditDonor?v=k3PZb1rGL2OJptx7_Wq4Yu8kZSWVRVievzK9AFvF6b01':
		edit_donor = script
	else:
		pass

settings = []

for sett in str(edit_donor.findNextSibling()).split('\r\n'):
	try:
		if sett[16:22] == 'model.':
			settings.append(sett[22:])
	except:
		pass

dic = {}

for i in settings:
	if i.startswith('HonorableDonorSettings') == True:
		i = i.replace(i[22], '[', 1)
		i = i.replace('__', '].')
		i = i.replace(i.split('=')[0], quote_plus(i.split('=')[0]))
	dic[i.split('=')[0][:-1]] = i.split('=')[1][1:-1]

for i in dic:
	dic[i] = dic[i].strip("'")

dic['DonorSubscription'] = quote_plus(dic['DonorSubscription'].replace('&quot;', '"').replace('\\', '\r'+'\\').replace('\\n', codecs.decode('\\n', 'unicode_escape')))

dic['ViewTabName'] = 'EditDonor'

dic['NextTabName'] = ''

for k, v in dic.items():
	dic[k] = v.strip(' ')


class TurnBackToPreviousSettings(object):
	def __init__(self, url, session, headers, script):
		self.url = url
		self.session = session
		self.headers = headers
		self.script = script
	def get_settings(self):
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
				if sett[16:22] == 'model.':
					settings.append(sett[22:])
			except:
				pass
		return settings