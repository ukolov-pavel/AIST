from base import BaseTest, Session
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import codecs
import json


class Settings(object):
	'''Базовый класс для работы с глобальными настройками системы.

	Поддерживаются следующие функциональности:
	1) get_raw_settings: получение "сырых" настроек;
	2) get_settings: получение текущего состояния определённого класса настроек (какие настройки применены СЕЙЧАС);
	3) post_settings: отправление определённых настроек на сервер (применение настроек);
	4) edit_settings: редактирование текущих настроек и их последующее отправление на сервер.
	Нюансы применения некоторых методов описаны отдельно в их документации.

	Уколов П.
	'''

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
		'''
		Метод парсит html нужной страницы, извлекая из неё нужную информацию.
		Возвращает необработанные, "сырые" значения.
		'''
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
		elif mode == 'script':
			return str_settings
		else:
			return soup

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

	def edit_settings(self, **edited_settings):
		'''Меняет текущие настройки и отправляет их.
		Пример использования:
		>>> DonationsSettings().edit_settings(MaxYearBloodDonationCountMale='5')
		либо, если ключ содержит символы вроде точки и т.д.:
		>>> donations_counts = {'EditDelays[0].Days': '2', 'EditDelays[1].Days': '33'}
		>>> DonationsSettings().edit_settings(**{str(k): v for k, v in donations_counts.items()})
		'''

		current_settings = self.get_settings()
		updated = {}
		for k, v in edited_settings.items():
			updated[quote_plus(k)] = v
		updated_settings = {**current_settings, **updated}
		return self.post_settings(updated_settings)


class DonationsSettings(Settings):
	'''
	Класс для работы с ГН --> Донация
	'''

	def __init__(self, script='Q5M5c4m_DiE8N-vPmMI6ahTLJDkExwefMRrV3gZcX_U1', url='/Admin/Setting/EditDonation'):
		Settings.__init__(self, url, script)

	def get_settings(self):
		settings = self.get_raw_settings()
		str_settings = self.get_raw_settings('script')
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


class DonorSettings(Settings):
	'''
	Класс для работы с ГН --> Донор
	'''

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


class GeneralSettings(Settings):
	'''
	Класс для работы с ГН --> Общие настройки
	'''

	def __init__(self, script='Fiwo7VU1dKICygplXugVwqlH68hZEEfzozuZDqRhYx01', url='/Admin/Setting/EditGeneral'):
		Settings.__init__(self, url, script)

	def get_settings(self):
		dic = super().get_settings()
		dic['ViewTabName'] = 'EditGeneral'
		dic['NextTabName'] = ''
		dic['CurrentOrganizationName'] = quote_plus('ФГБУЗ Центр крови ФМБА России')
		dic['ContractorInfo'] = quote_plus(dic['ContractorInfo'])
		dic['WorkWithRecipientsInLaboratory'] = 'False'
		return dic


class ProductSettings(Settings):
	'''
	Класс для работы с ГН --> Продукция
	'''

	def __init__(self, script='7Uk85H-JIFrzUzUj0f6mVHMlb4uN4E4TFJWyEy_u3VI1', url='/Admin/Setting/EditProduct'):
		Settings.__init__(self, url, script)

	def get_settings(self):
		dic = super().get_settings()
		dic['ViewTabName'] = 'EditProduct'
		dic['NextTabName'] = ''
		return dic

class StickerSettings(Settings):
	'''
	Класс для работы с ГН --> Печатные формы
	'''

	def __init__(self, script='h9XKzduIFgWurWIWiiVJW0mwbgoJ-ff3hBK9jrBm1Yo1', url='/Admin/Setting/EditSticker'):
		Settings.__init__(self, url, script)

	def get_settings(self):
		def x2():
			num = 1
			while num <= 32768:
				yield num
				num = num * 2

		x2_generator = x2()
		dic = super().get_settings()
		dic['ViewTabName'] = 'EditSticker'
		dic['NextTabName'] = ''
		keys_to_delete = ['StickerWidth', 'StickerHeight', 'StampWidth', 'StampHeight', 'CellStampWidth', 'CellStampHeight',
		'RefusionStampWidth', 'RefusionStampHeight']
		for i in keys_to_delete:
			del (dic[i])
		dic['StickerText'] = quote_plus(dic['StickerText'].replace('\\n', '\r\n'))
		html = self.get_raw_settings(mode='other')
		keys_to_append = ['OverwriteSourceStickerText', 'NotShowLastDonationTest', 'PrintOnlyLatestetectedAntibodies']
		for i in keys_to_append:
			input = html.find('input', attrs={'id': i})
			if input.get('checked') == None:
				dic[i] = 'false'
			else:
				dic[i] = 'true'
		for i in html.findAll('table'):
			if i.get('id') == 'gridModeList':
				mode_list = i
		modes = mode_list.findChild('tbody').findAll('input', attrs={'type': 'checkbox'})
		modes_dict = {}
		ind = ''
		for i in modes:
			mode_index = i.get('name').split('.')[0]
			mode_index = mode_index[mode_index.find("[") + 1:mode_index.find("]")]
			if ind != mode_index:
				modes_dict[quote_plus('modes[' + mode_index + '].ModeId')] = str(x2_generator.__next__())
			else:
				pass
			if str(i.get('checked')) == 'None':
				modes_dict[quote_plus(i.get('name'))] = 'false'
			else:
				modes_dict[quote_plus(i.get('name'))] = 'true'
			ind = mode_index
		dic = {**dic, **modes_dict}
		return dic