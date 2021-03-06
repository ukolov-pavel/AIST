'''
Словарь со списком элементов страниц, отсортированных в алфавитном порядке (для удобства чтения). 
Список элементов идентичен (ключи словарей имеют такие же названия, 
как элементы соответствующих модулей страниц) с теми, которые описаны в модуле страницы - 
туда подтягиваются локаторы и их значения из этих словарей. 
Сделано для того, чтобы в ситуациях, когда элемент динамически генерируется на странице (т.е, изначально, на момент запуска
скрипта, элемент отсутствовал или, если был на странице, но по каждому действию, которое приводит к появлению нужного нам элемента.
элемент с таким же, например, айдишником генерируется новый, а старый элемент не исчезает из DOM, но является уже невидимым.).
Пример использования словаря локаторов можно увидеть в документации к классу **element_is_visible** из модуля **aistium**.
'''

donors_registry_locators = {
		'alert': ['Find', 'id', 'alert-popup'],
		'birthdate_field_ndp': ['Find', 'id', 'BirthDate'],
		'cancel_reason_back_donation_btn': ['Find', 'id', 'CancelReasonBackDonationBtn'],
		'confirm_popup': ['Finds', 'id', 'confirm-popup'],
		'confirm_popup_no_btn': ['Finds', 'id', 'confirm-popup-no'],
		'confirm_popup_yes_btn': ['Finds', 'id', 'confirm-popup-yes'],
		'deferrals_button': ['Find', 'id', 'DeferralsButton'],
		'deferrals_grid': ['Find', 'id', 'deferralGrid'],
		'deferral_from_minicard': ['Find', 'css selector', 'div.deferralinfo-block:nth-child(4)'],
		'deferral_only_active_tick': ['Find', 'id', 'DeferralPage_OnlyActive'],
		'diseases_button': ['Find', 'id', 'DiseasesButton'],
		'diseases_grid': ['Find', 'id', 'diseasesGrid'],
		'diseases_only_active': ['Find', 'id', 'DiseasesPage_OnlyActive'],
		'document_number_field_ndp': ['Find', 'id', 'IdentityDocument_Number'],
		'document_serie_field_ndp': ['Find', 'id', 'IdentityDocument_Serie'],
		'document_type_select_field': ['Find', 'xpath', '//*[@id="step1"]//*[contains(@class, "k-dropdown-wrap k-state-default")]/span[@class="k-input"]'],
		'donation_type_select_row': ['Find', 'xpath', "//div[contains(@class, 'margin-bottom-15 donation')]/span/span/span"],
		'edit_reason_back_donation_window': ['Finds', 'id', 'edit-reason-back-donation-window'],
		'extended_birthdate_from': ['Find', 'id', 'ExtendedBirthDateFrom'],
		'extended_birthdate_to': ['Find', 'id', 'ExtendedBirthDateTo'],
		'extended_donation_barcode': ['Find', 'id', 'ExtendedDonationBarCode'],
		'extended_fias_address_house': ['Find', 'id', 'searchFiasAddress_House'],
		'extended_firstname': ['Find', 'id', 'ExtendedName'],
		'extended_lastname': ['Find', 'id', 'ExtendedSurname'],
		'extended_middlename': ['Find', 'id', 'ExtendedLastName'],
		'extended_preregistration_from': ['Find', 'id', 'ExtendedPreregistrationFrom'],
		'extended_preregistration_to': ['Find', 'id', 'ExtendedPreregistrationTo'],
		'extended_registry_number': ['Find', 'id', 'ExtendedRegistryNumber'],
		'extended_search_button': ['Find', 'id', 'ExtendedSearch'],
		'extended_search_clear_button': ['Find', 'id', 'ExtendedSearchCancel'],
		'extended_search_close': ['Find', 'id', 'ExtendedSearchClose'],
		'extended_search_field': ['Find', 'id', 'ExtendedSearchLink'],
		'extended_search_select_doc_type_field': ['Find', 'xpath', "//div[contains(@class, 'extendedSearchBlock-line')][3]/span/span/span[1]"],
		'extended_search_select_gender_field': ['Find', 'xpath', "//div[contains(@class, 'extendedSearchBlock-line')][1]/div[1]/span/span/span[1]"],
		'fio_minicard': ['Find', 'class name', 'person-card-details-fio'],
		'first_name_field_ndp': ['Find', 'id', 'FirstName'],
		'identity_document_issue_date': ['Find', 'id', 'IdentityDocument_IssueDate'],
		'identity_document_issued_by': ['Find', 'id', 'IdentityDocument_IssuedBy'],
		'is_agree_persional_data_processing': ['Find', 'id', 'IsAgreePersionalDataProcessing'],
		'is_fact_address_equals_reg_address': ['Find', 'id', 'IsFactAddressEqualsRegAddress'],
		'is_message_agree': ['Find', 'id', 'IsMessageAgree'],
		'job_place': ['Find', 'id', 'JobInfo'],
		'minicard_job_place_label': ['Find', 'xpath', '//div[@class="short-registry-block"]/label[contains(@for, "PersonInfo_JobInfo")]'],
		'job_position': ['Find', 'id', 'JobPosition'],
		'last_name_field_ndp': ['Find', 'id', 'LastName'],
		'list_of_directed_button': ['Find', 'xpath', "//div[contains(@class, 'searchPage-title')]/a/input"],
		'local_cabinet_continue': ['Find', 'css selector', 'input.right'],
		'main_grid': ['Find', 'id', 'gridView'],
		'middle_name_field_ndp': ['Find', 'id', 'MiddleName'],
		'minicard_address': ['Find', 'id', 'person-card-address-fact'],
		'minicard_email': ['Find', 'class name', 'contacts-email.contacts-info'],
		'minicard_mobile_phone': ['Find', 'class name', 'contacts-mobile.contacts-info'],
		'minicard_phone': ['Find', 'class name', 'contacts-phone.contacts-info'],
		'minicard_snils': ['Find', 'xpath', '//div[contains(@class, "person-card-details-data-block")]/span[contains(@title, "СНИЛС")]'],
		'ndp_birth_place': ['Find', 'id', 'BirthPlace'],
		'ndp_deferral_clear_button': ['Find', 'id', 'DeferralNewDonorClearButton'],
		'ndp_deferral_field': ['Find', 'xpath', '//input[@name="DeferralTypeIdNewDonor_input"]'],
		'ndp_deferral_type': ['Find', 'id', 'DeferralTypeNameNewDonor'],
		'ndp_donation_type_field': ['Find', 'css selector', 'span.k-combobox:nth-child(2) > span:nth-child(1) > input:nth-child(1)'],
		'ndp_email': ['Find', 'id', 'Email'],
		'ndp_female_gender': ['Find', 'id', 'Gender2'],
		'ndp_first_page_cancel_newdonor': ['Find', 'id', 'cancel-newdonor1'],
		'ndp_job_place_field': ['Find', 'xpath', '//input[contains(@name, "JobInfo_input")]'],
		'ndp_male_gender': ['Find', 'id', 'Gender1'],
		'ndp_mobile_phone': ['Find', 'id', 'PhoneMob'],
		'ndp_phone': ['Find', 'id', 'Phone'],
		'ndp_second_page_cancel_newdonor': ['Find', 'id', 'cancel-newdonor'],
		'newdonor': ['Find', 'id', 'newdonor'],
		'next_step_ndp': ['Find', 'id', 'NextStep'],
		'popup_close_icon': ['Finds', 'class name', 'k-icon.k-i-close'],
		'popup_titlebar': ['Find', 'class name', 'k-window-titlebar.k-header.message-popup-title'],
		'previous_step_ndp': ['Find', 'id', 'PrevStep'],
		'process_state_button': ['Find', 'id', 'donation-process-state-button'],
		'quick_search_button': ['Find', 'id', 'Search'],
		'quick_search_field': ['Find', 'id', 'SimpleSearchText'],
		'reason_back_donation_input': ['Find', 'id', 'reasonBackDonation'],
		'reg_fias_address_building': ['Find', 'id', 'regFiasAddress_Building'],
		'reg_fias_address_city': ['Find', 'id', 'regFiasAddress_City'],
		'reg_fias_address_city_listbox': ['Finds', 'id', 'regFiasAddress_City_listbox'],
		'reg_fias_address_house': ['Find', 'id', 'regFiasAddress_House'],
		'reg_fias_address_office': ['Find', 'id', 'regFiasAddress_Office'],
		'reg_fias_address_region': ['Find', 'id', 'regFiasAddress_Region'],
		'reg_fias_address_region_listbox': ['Finds', 'id', 'regFiasAddress_Region_listbox'],
		'reg_fias_address_street': ['Find', 'id', 'regFiasAddress_Street'],
		'reg_fias_address_structure': ['Find', 'id', 'regFiasAddress_Structure'],
		'reset_filters': ['Find', 'id', 'ResetFilters'],
		'save_new_donor_button': ['Find', 'id', 'save-newdonor'],
		'save_reason_back_donation_btn': ['Find', 'id', 'SaveReasonBackDonationBtn'],
		'snils_field': ['Find', 'id', 'Snils'],
		'social_status_field': ['Find', 'xpath', '//input[contains(@name, "SocialStatus_input")]'],
		'social_status_select_row': ['Find', 'css selector', '#step2 > div:nth-child(16) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1) > span:nth-child(2) > span:nth-child(1)']}

donors_card_title_locators = {
		'personal_content_back_address_and_jobs': ['Finds', 'xpath', '//*[@class="personal-content-back"]//*[@class="clear margin-bottom-10 bold"]']
}