import requests
from base import BaseTest
from urllib.parse import quote_plus

def change_product_settings(**settings):

	payload = {'Login':BaseTest.login, 'Password':BaseTest.password}

	url = BaseTest.stand+'/Auth/LogOn'

	s = requests.Session()

	s.post(url, data=payload)

	constant_headers = {'Referer': BaseTest.stand+'/Admin/Setting/EditProduct', 'Content-Type': 'application/x-www-form-urlencoded'}

	cookies = s.cookies.get_dict()

	headers = {**constant_headers, **cookies}
	
	product_settings = {'ViewTabName': 'EditProduct', 
	'NextTabName': '', 
	'ProductBaseTypesBalanceByFiltrat': quote_plus('[]'), 
	'FiltrateProductTypeId': '901', 
	'FiltrateIsCompleted': 'true', 
	'FiltrateProductDefectTypeId': '', 
	'UtilizationDepartmentId': '120000008', 
	'ExpirationDateDefectTypeId': '12', 
	'BakDefectTypeId': '', 
	'LipidDefectTypeId': '8', 
	'AgglutinationDefectTypeIds': '', 
	'HemolysisDefectTypeId': '', 
	'IsOutIfDonorHasNotApprobed': 'false', 
	'CheckEpidcontrolForOuter': 'false', 
	'CheckEpidControlInProduction': 'false', 
	'CheckCategoryForOuter': 'false', 
	'SendMultipleTubesApprove': 'false', 
	'CheckNumberOfProductsToNumberOfContainers': 'false', 
	'AutoDonorAutomaticApprobationProducts': 'false', 
	'AutoDonorAutomaticQuarantineProducts': 'false', 
	'AllowIncorrectBloodGroup': 'false', 
	'DefaultServiceForLockedId': '', 
	'AutomaticAddToInvoice': 'false', 
	'ExpeditionInvoiceReturnPeriod': '5',
	'CheckTwoBarcodesInExpedition': 'false', 
	'AllowFractionationOtherOrganizations': 'true', 
	'LabSelectionProducts': '4', 
	'LabSelectionDepartments': '19', 
	'ChildDoseVolumeFrom': '', 
	'ChildDoseVolumeTo': '', 
	'FirstNumberBarcode': '150237', 
	'SearchProductsByPartialBarcode': 'false'}

	updated_product_settings = {**product_settings, **settings}

	request_body_list = []

	for i in updated_product_settings:
		request_body_list.append(i+'='+updated_product_settings[i])

	request_body = '&'.join(request_body_list)

	s.post(BaseTest.stand+'/Admin/Setting/EditProduct', data=request_body, headers=headers)