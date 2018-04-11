import requests
from base import BaseTest
from urllib.parse import quote_plus

def change_donor_settings(**settings):

	payload = {'Login':BaseTest.login, 'Password':BaseTest.password}

	url = BaseTest.stand+'/Auth/LogOn'

	s = requests.Session()

	s.post(url, data=payload)

	constant_headers = {'Referer': BaseTest.stand+'/Admin/Setting/EditDonor', 'Content-Type': 'application/x-www-form-urlencoded'}

	cookies = s.cookies.get_dict()

	headers = {**constant_headers, **cookies}

	donor_settings = {'ViewTabName': 'EditDonor',
					  'NextTabName': '',
					  'DonorSubscription': quote_plus('Я прочитал(а) и правильно ответил(а) на все вопросы "Анкеты донора", а также получил(а) ответы на все заданные мной вопросы. Если я нахожусь в группе риска по распространению вирусов гепатита В, С, ВИЧ и других болезней, я согласен(на) не сдавать кровь (плазму) для других людей. Я понимаю, что моя кровь (плазма) будет проверена на ВИЧ и другие вирусы.  Я информирован(а), что во время процедуры взятия крови (плазмы) возможны незначительные реакции организма (кратковременное снижение АД, гематома в области венепункции) не являющиеся следствием ошибки персонала. Я осведомлен(а) о том, что за сокрытие сведений о наличии у меня ВИЧ-инфекции или венерического заболевания я подлежу уголовной ответственности в соответствии со ст. 121 и 122 УК РФ. Я согласен(на): 1) на внесение моих персональных данных, включая данные о состоянии здоровья, в единую базу данных по осуществлению мероприятий, связанных с обеспечением безопасности донорской крови и её компонентов, развитием, организацией и (или) пропагандой донорства крови и её компонентов; 2) на получение информационных уведомлений, связанных с развитием, организацией и (или) пропагандой донорства крови и её компонентов, а также поздравительных уведомлений на указанный мной:\r\n - адрес электронной почты;\r\n - номер контактного телефона.\r\n\r\nПодпись донора ______________   Подпись мед. работника ______________'),
					  'UseFicDonorSearch': 'true',
					  'CheckDonorInFicWhileDirection': 'false',
					  'CheckDonorInFicWhileExaminationDone': 'false',
					  'UseAllDonorDocumentsForFicSearch': 'false',
					  'CheckFiasAddressForDonor': 'false',
					  'CheckIncompleteAnalysis': 'false',
					  'CheckEpidControlLessYear': 'true',
					  'AlwaysShowEpidAddress': 'false',
					  'ShowVisitsWithoutExaminations': 'false',
					  'ShowJobInfo': 'false',
					  'CheckAntierythrocyteDonationOrExamination': 'false',
					  'NotSetIsMessageAgreeFlagByDefault': 'false',
					  'ShowAllContainersWithPlasmaByQuarantine': 'false',
					  'ShowRegDateFromPersonCard': 'false',
					  'CertExpirationUrinalysis': '365',
					  'CertExpirationGynecologist': '365',
					  'CertExpirationSanEpid': '180',
					  'CertExpirationTherapist': '180',
					  'CertExpirationFluorography': '365',
					  'CertExpirationElectrocardiogram': '365',
					  'DonorMinAge': '18',
					  'DonorMaxAge': '96',
					  'NotifyRegistrarForHonorableDonor': 'false',
					  quote_plus('HonorableDonorSettings[0].DonationsCount'): '0',
					  quote_plus('HonorableDonorSettings[0].BloodAndComponentsCount'): '0',
					  quote_plus('HonorableDonorSettings[0].PlasmaCount'): '0',
					  quote_plus('HonorableDonorSettings[1].DonationsCount'): '0',
					  quote_plus('HonorableDonorSettings[1].BloodAndComponentsCount'): '0',
					  quote_plus('HonorableDonorSettings[1].PlasmaCount'): '0',
					  quote_plus('HonorableDonorSettings[2].DonationsCount'): '0',
					  quote_plus('HonorableDonorSettings[2].BloodAndComponentsCount'): '0',
					  quote_plus('HonorableDonorSettings[2].PlasmaCount'): '0',
					  quote_plus('HonorableDonorSettings[3].DonationsCount'): '0',
					  quote_plus('HonorableDonorSettings[3].BloodAndComponentsCount'): '0',
					  quote_plus('HonorableDonorSettings[3].PlasmaCount'): '0'}

	updated = {}

	for k, v in settings.items():
		updated[quote_plus(k)] = v

	updated_donor_settings = {**donor_settings, **updated}

	request_body_list = []

	for i in updated_donor_settings:
		request_body_list.append(i+'='+updated_donor_settings[i])

	request_body = '&'.join(request_body_list)

	s.post(BaseTest.stand+'/Admin/Setting/EditDonor', data=request_body, headers=headers)