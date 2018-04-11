import requests
from base import BaseTest
from urllib.parse import quote_plus

def change_general_settings(**settings):

	payload = {'Login':BaseTest.login, 'Password':BaseTest.password}

	url = BaseTest.stand+'/Auth/LogOn'

	s = requests.Session()

	s.post(url, data=payload)

	constant_headers = {'Referer': BaseTest.stand+'/Admin/Setting/EditGeneral', 'Content-Type': 'application/x-www-form-urlencoded'}

	cookies = s.cookies.get_dict()

	headers = {**constant_headers, **cookies}
	
	general_settings = {'ViewTabName': 'EditGeneral', 
	'NextTabName': '', 
	'CurrentOrganizationId': '774800', 
	'CurrentOrganizationName': quote_plus('ФГБУЗ Центр крови ФМБА России'), 
	'ContractorInfo': quote_plus('Амирхаян Арам 8 (925) 011-05-19'), 
	'ConversionDate': '',
	'NomenclatureDate': '09.03.2018',
	'DefaultAddressFiasRegionId': '', 
	'DefaultAddressFiasRegion': '', 
	'DefaultAddressFiasAreaId': '', 
	'DefaultAddressFiasArea': '', 
	'DefaultAddressFiasCityId': '', 
	'DefaultAddressFiasCity': '', 
	'DefaultAddressFiasInnerAreaId': '', 
	'DefaultAddressFiasInnerArea': '', 
	'DefaultAddressFiasSettlementId': '', 
	'DefaultAddressFiasSettlement': '', 
	'AllowPartialFiasAddress': 'false', 
	'UseCurrentCalendarYearRadioButton': 'on', 
	'UseCurrentCalendarYear': 'False', 
	'UseBloodGroupEuropeanFormat': 'true', 
	'UseRhesusLowerFormat': 'false', 
	'UsePhenotypeShortFormat': 'false', 
	'ValueAddedTax': '0', 
	'CheckBloodParametersForRecipientAndProduct': 'false', 
	'WorkWithPreRegistration': 'false', 
	'IasSpkGuid': '8E034A62-1D92-4F9C-AC2A-4579CFFE429D', 
	'BlockPasswordSave': 'false', 
	'EnableExternalTestPub': 'false', 
	'KeepReportPrintOptionsWindowOpen': 'true', 
	'CountItemsInElectronicQueue': '3', 
	'SendInvoicesManual': 'false', 
	'WorkWithRecepientInDonor': 'true', 
	'WorkWithRecepientInExpedition': 'true', 
	'WorkWithRequestsInExpedition': 'true', 
	'WorkWithPurposes': 'true', 
	'WorkWithSocialStatus': 'true', 
	'WorkWithCommodities': 'true', 
	'WorkWithHLA': 'true', 
	'HlaErrorCount': '', 
	'WorkWithRecipientsInLaboratory': 'false'}

	updated_general_settings = {**general_settings, **settings}

	request_body_list = []

	for i in updated_general_settings:
		request_body_list.append(i+'='+updated_general_settings[i])

	request_body = '&'.join(request_body_list)

	s.post(BaseTest.stand+'/Admin/Setting/EditGeneral', data=request_body, headers=headers)