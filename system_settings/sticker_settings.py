import requests
from base import BaseTest
from urllib.parse import quote_plus

def change_sticker_settings(**settings):

	payload = {'Login':BaseTest.login, 'Password':BaseTest.password}

	url = BaseTest.stand+'/Auth/LogOn'

	s = requests.Session()

	s.post(url, data=payload)

	constant_headers = {'Referer': BaseTest.stand+'/Admin/Setting/EditSticker', 'Content-Type': 'application/x-www-form-urlencoded'}

	cookies = s.cookies.get_dict()

	headers = {**constant_headers, **cookies}
	
	sticker_settings = {'ViewTabName': 'EditSticker', 
	'NextTabName': '', 
	'IsTraditionalSticker': 'True', 
	'StickerGost': '', 
	'StickerText': quote_plus('Тесты на ВИЧ,\r\nгепатиты В и С,\r\nсифилис отрицательны'), 
	'OverwriteSourceStickerText': 'false', 
	'ShowCustomText': 'false', 
	'PrintNumber': 'true', 
	'PrintEmployeeInfo': 'false', 
	'modes%5B0%5D.ModeId': '1', 
	'modes%5B0%5D.PrintName': 'false', 
	'modes%5B0%5D.PrintDate': 'false', 
	'modes%5B0%5D.PrintTime': 'false', 
	'modes%5B1%5D.ModeId': '2', 
	'modes%5B1%5D.PrintName': 'false',
	'modes%5B1%5D.PrintDate': 'false',
	'modes%5B1%5D.PrintTime': 'false', 
	'modes%5B2%5D.ModeId': '4', 
	'modes%5B2%5D.PrintName': 'false', 
	'modes%5B2%5D.PrintDate': 'false', 
	'modes%5B2%5D.PrintTime': 'false', 
	'modes%5B3%5D.ModeId': '8', 
	'modes%5B3%5D.PrintName': 'false', 
	'modes%5B3%5D.PrintDate': 'false', 
	'modes%5B3%5D.PrintTime': 'false', 
	'modes%5B4%5D.ModeId': '16', 
	'modes%5B4%5D.PrintName': 'false', 
	'modes%5B4%5D.PrintDate': 'false', 
	'modes%5B4%5D.PrintTime': 'false', 
	'modes%5B5%5D.ModeId': '32', 
	'modes%5B5%5D.PrintName': 'false', 
	'modes%5B5%5D.PrintDate': 'false', 
	'modes%5B5%5D.PrintTime': 'false', 
	'modes%5B6%5D.ModeId': '32768', 
	'modes%5B6%5D.PrintName': 'false', 
	'modes%5B6%5D.PrintDate': 'false', 
	'modes%5B6%5D.PrintTime': 'false', 
	'modes%5B7%5D.ModeId': '64', 
	'modes%5B7%5D.PrintName': 'false', 
	'modes%5B7%5D.PrintDate': 'false', 
	'modes%5B7%5D.PrintTime': 'false', 
	'modes%5B8%5D.ModeId': '128', 
	'modes%5B8%5D.PrintName': 'false', 
	'modes%5B8%5D.PrintDate': 'false', 
	'modes%5B8%5D.PrintTime': 'false', 
	'modes%5B9%5D.ModeId': '256', 
	'modes%5B9%5D.PrintName': 'false', 
	'modes%5B9%5D.PrintDate': 'false', 
	'modes%5B9%5D.PrintTime': 'false', 
	'modes%5B9%5D.PrintValue': 'false', 
	'modes%5B10%5D.ModeId': '512', 
	'modes%5B10%5D.PrintName': 'false', 
	'modes%5B10%5D.PrintDate': 'false', 
	'modes%5B10%5D.PrintTime': 'false', 
	'modes%5B11%5D.ModeId': '1024', 
	'modes%5B11%5D.PrintName': 'false', 
	'modes%5B11%5D.PrintDate': 'false', 
	'modes%5B11%5D.PrintTime': 'false', 
	'modes%5B12%5D.ModeId': '2048', 
	'modes%5B12%5D.PrintName': 'false', 
	'modes%5B12%5D.PrintDate': 'false', 
	'modes%5B12%5D.PrintTime': 'false', 
	'modes%5B13%5D.ModeId': '4096', 
	'modes%5B13%5D.PrintName': 'false', 
	'modes%5B13%5D.PrintDate': 'false', 
	'modes%5B13%5D.PrintTime': 'false', 
	'modes%5B14%5D.ModeId': '8192', 
	'modes%5B14%5D.PrintName': 'false', 
	'modes%5B14%5D.PrintDate': 'false', 
	'modes%5B14%5D.PrintTime': 'false', 
	'modes%5B15%5D.ModeId': '16384', 
	'modes%5B15%5D.PrintName': 'false', 
	'modes%5B15%5D.PrintDate': 'false', 
	'modes%5B15%5D.PrintTime': 'false', 
	'ShowPreview': 'true', 
	'PrintBloodGroupWithSubgroups': 'false', 
	'PrintDonorGender': 'true', 
	'PrintDWeak': 'false', 
	'ScaleSticker': 'false', 
	'StickerExpirationEoPeriodAsBefore': 'False', 
	'StickerProducedDateTitle': 'False', 
	'PrintSeparatorDefault': 'false', 
	'ScaleStamp': 'false', 
	'ScaleCellStamp': 'false', 
	'ScaleRefusionStamp': 'false', 
	'PrintWithMedicalDirection': 'false', 
	'PrintDonationType': 'true', 
	'PrintRunner': 'false', 
	'PrintRunnerFromDeparture': 'false', 
	'ShowRegistrationCommentsInRunner': 'false', 
	'ShowImmunohematologyCommentsInRunner': 'false', 
	'ShowDepartureCommentsInRunner': 'false', 
	'PrintRunnerWithCoupon': 'false', 
	'PrintRunnerWithStatus': 'false', 
	'PrintRunnerWithPhoto': 'false', 
	'NotShowLastDonationTest': 'false', 
	'PrintOnlyLatestetectedAntibodies': 'false'}

	updated_sticker_settings = {**sticker_settings, **settings}

	request_body_list = []

	for i in updated_sticker_settings:
		request_body_list.append(i+'='+updated_sticker_settings[i])

	request_body = '&'.join(request_body_list)

	s.post(BaseTest.stand+'/Admin/Setting/EditSticker', data=request_body, headers=headers)