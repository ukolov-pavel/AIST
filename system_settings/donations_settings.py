import requests
from base import BaseTest

def change_donations_settings(**settings):

	payload = {'Login':BaseTest.login, 'Password':BaseTest.password}

	url = BaseTest.stand+'/Auth/LogOn'

	s = requests.Session()

	s.post(url, data=payload)

	constant_headers = {'Referer': BaseTest.stand+'/Admin/Setting/EditDonation', 'Content-Type': 'application/x-www-form-urlencoded'}

	cookies = s.cookies.get_dict()

	headers = {**constant_headers, **cookies}
	
	donations_settings = {
	'ViewTabName': 'EditDonation', 
	'NextTabName': '', 
	'MaxYearBloodDonationCountMale': '3', 
	'MaxYearBloodDonationCountFemale': '3', 
	'MaxYearPlasmaVolumeMale': '2', 
	'MaxYearPlasmaVolumeFemale': '1', 
	'MaxYearPlasmapheresisCount': '1', 
	'MaxYearCytapheresisCount': '1', 
	'AlbuminCheckDonationInterval': '0', 
	'HbCoreCheckDonationInterval': '30', 
	'ConsiderBranchesKellPhenotypeResults': 'false', 
	'OrgFillsPhenotypeCw': 'false', 
	'ExcludeAntibodyMessage': 'false', 
	'AsynchronousProcessingOfResearchesResults': 'false', 
	'AvailabilityBrigadeNecessarily': 'false', 
	'ShortageComplicationGuid': '', 
	'ShowComplicationsInPersonCard': 'false', 
	'EditDelays%5B0%5D.Id': '1', 
	'EditDelays%5B0%5D.Days': '1', 
	'EditDelays%5B1%5D.Id': '2', 
	'EditDelays%5B1%5D.Days': '0', 
	'EditDelays%5B2%5D.Id': '3', 
	'EditDelays%5B2%5D.Days': '0', 
	'EditDelays%5B3%5D.Id': '4', 
	'EditDelays%5B3%5D.Days': '0', 
	'EditDelays%5B4%5D.Id': '5', 
	'EditDelays%5B4%5D.Days': '0', 
	'EditDelays%5B5%5D.Id': '6', 
	'EditDelays%5B5%5D.Days': '0', 
	'EditDelays%5B6%5D.Id': '9', 
	'EditDelays%5B6%5D.Days': '1', 
	'EditDelays%5B7%5D.Id': '10', 
	'EditDelays%5B7%5D.Days': '60', 
	'EditDelays%5B8%5D.Id': '11', 
	'EditDelays%5B8%5D.Days': '30', 
	'EditDelays%5B9%5D.Id': '12', 
	'EditDelays%5B9%5D.Days': '30', 
	'EditDelays%5B10%5D.Id': '13', 
	'EditDelays%5B10%5D.Days': '30', 
	'EditDelays%5B11%5D.Id': '14', 
	'EditDelays%5B11%5D.Days': '30', 
	'EditDelays%5B12%5D.Id': '21', 
	'EditDelays%5B12%5D.Days': '1', 
	'EditDelays%5B13%5D.Id': '22', 
	'EditDelays%5B13%5D.Days': '14', 
	'EditDelays%5B14%5D.Id': '23', 
	'EditDelays%5B14%5D.Days': '14', 
	'EditDelays%5B15%5D.Id': '24', 
	'EditDelays%5B15%5D.Days': '14', 
	'EditDelays%5B16%5D.Id': '25', 
	'EditDelays%5B16%5D.Days': '14', 
	'EditDelays%5B17%5D.Id': '26', 
	'EditDelays%5B17%5D.Days': '14', 
	'EditDelays%5B18%5D.Id': '29', 
	'EditDelays%5B18%5D.Days': '1', 
	'EditDelays%5B19%5D.Id': '30', 
	'EditDelays%5B19%5D.Days': '14', 
	'EditDelays%5B20%5D.Id': '31', 
	'EditDelays%5B20%5D.Days': '14', 
	'EditDelays%5B21%5D.Id': '32', 
	'EditDelays%5B21%5D.Days': '14', 
	'EditDelays%5B22%5D.Id': '33', 
	'EditDelays%5B22%5D.Days': '14', 
	'EditDelays%5B23%5D.Id': '34', 
	'EditDelays%5B23%5D.Days': '14', 
	'EditDelays%5B24%5D.Id': '37', 
	'EditDelays%5B24%5D.Days': '1', 
	'EditDelays%5B25%5D.Id': '38', 
	'EditDelays%5B25%5D.Days': '30', 
	'EditDelays%5B26%5D.Id': '39', 
	'EditDelays%5B26%5D.Days': '14', 
	'EditDelays%5B27%5D.Id': '40', 
	'EditDelays%5B27%5D.Days': '14', 
	'EditDelays%5B28%5D.Id': '41', 
	'EditDelays%5B28%5D.Days': '14', 
	'EditDelays%5B29%5D.Id': '42', 
	'EditDelays%5B29%5D.Days': '14', 
	'EditDelays%5B30%5D.Id': '45', 
	'EditDelays%5B30%5D.Days': '1', 
	'EditDelays%5B31%5D.Id': '46', 
	'EditDelays%5B31%5D.Days': '30', 
	'EditDelays%5B32%5D.Id': '47', 
	'EditDelays%5B32%5D.Days': '14', 
	'EditDelays%5B33%5D.Id': '48', 
	'EditDelays%5B33%5D.Days': '14', 
	'EditDelays%5B34%5D.Id': '49', 
	'EditDelays%5B34%5D.Days': '14', 
	'EditDelays%5B35%5D.Id': '50', 
	'EditDelays%5B35%5D.Days': '14'
	}

	updated_donations_settings = {**donations_settings, **settings}

	request_body_list = []

	for i in updated_donations_settings:
		request_body_list.append(i+'='+updated_donations_settings[i])

	request_body = '&'.join(request_body_list)

	s.post(BaseTest.stand+'/Admin/Setting/EditDonation', data=request_body, headers=headers)