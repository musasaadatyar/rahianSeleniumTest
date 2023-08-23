# locator in login page
national_cod_login_id_locator = 'LoginInput_UserNameOrEmailAddress'
password_login_id_locator = 'LoginInput_Password'
remember_login_id_locator = 'LoginInput_RememberMe'
enter_user_button_login_xpath_locator = '//button[@value="Login"]'
cancel_user_button_login_xpath_locator = '//button[@value="Cancel"]'
submit_button_xpath_login_locator = '//a[contains(text(),"ثبت نام")]'
conform_phone_link_login_locator = '/Account/VerifyPhoneNumber?returnUrl=%2Fconnect%2Fauthorize%3Fresponse_type%3Dcode%26client_id%3DRahian_Server_App%26state%3DcVNXNGY0WFh1TW55d0p2c0tCMHRwMi1HRE1MRnV6TkM1MVN0cXVxaG9NVTlT%26redirect_uri%3Dhttp%253A%252F%252F81.28.59.221%253A4200%26scope%3Dopenid%2520offline_access%2520Rahian%26code_challenge%3DjtLVh0CYbaHGy-gmUwXqVrhqthG7gmBjcrTJWX5eWVk%26code_challenge_method%3DS256%26nonce%3DcVNXNGY0WFh1TW55d0p2c0tCMHRwMi1HRE1MRnV6TkM1MVN0cXVxaG9NVTlT%26culture%3Den-US%26ui-culture%3Den-US'

# locator in submit page
national_cod_submit_id_locator = 'Input_NatinalCode'
phone_number_submit_id_locator = 'IphoneNumber'
birthday_submit_id_locator = 'Input_Birthday'
password_submit_id_locator = 'password'
confirm_password_submit_id_locator = 'Input_ConfirmPassword'
button_submit_id_locator = 'submit'
input_users_button_link = '/Account/Login?returnUrl=%2Fconnect%2Fauthorize%3Fresponse_type%3Dcode%26client_id%3DRahian_Server_App%26state%3DYjVRbXUxYkF3R0J1RzBXT0h5LnJ4aFdJck44TDViflU3NUh6amZMVVpHellu%26redirect_uri%3Dhttp%253A%252F%252F81.28.59.221%253A4200%26scope%3Dopenid%2520offline_access%2520Rahian%26code_challenge%3Dd3aVgaffvoGdbJ_3yc_5f0UENdolDTFm5Bxr9MK4t6Q%26code_challenge_method%3DS256%26nonce%3DYjVRbXUxYkF3R0J1RzBXT0h5LnJ4aFdJck44TDViflU3NUh6amZMVVpHellu%26culture%3Den-US%26ui-culture%3Den-US'

# locator in page check_status_phone_number
close_btn_pup_up_xpath = '//button[@aria-label="Close"]'
button_check_phone_number_xpath_locator = '//button[contains(text(),  "بررسی ")]'
confirm_phone_number_Link_text_locator = '/Account/VerifyPhoneNumber?returnUrl=%2Fconnect%2Fauthorize%3Fresponse_type%3Dcode%26client_id%3DRahian_App%26state%3DSUJmZWcuZU0yQ2kwZG9BTUlPNmlnZTJ6c1d5VmF-c0VKSVBEZU5DQ0k0SXdj%26redirect_uri%3Dhttp%253A%252F%252Flocalhost%253A4200%26scope%3Dopenid%2520offline_access%2520Rahian%26code_challenge%3DUanYkX2J3fMyrJXkQd-cB-meFZOhjh3-9kSWpp4tzuE%26code_challenge_method%3DS256%26nonce%3DSUJmZWcuZU0yQ2kwZG9BTUlPNmlnZTJ6c1d5VmF-c0VKSVBEZU5DQ0k0SXdj%26culture%3Den-US%26ui-culture%3Den-US'

# locator in page submit phone number
phone_number_submit_phone_id_locator = 'Input_PhoneNumber'
national_code_submit_phone_id_locator = 'Input_NatinalCode'
confirm_number_submit_phone_xpath_locator = '//button[contains(text(), "تایید شماره")]'

# locator in main page
enter_submit_button_main_page_locator = '//button[contains(text(),"ورود")]'

# locator in chose role in modal
radio_btn_chose_role_xpath_locator = "//div[contains(@class,'trigger-listAnimation')]//label[@class='ng-tns-c49-1'and not(contains(text(),'رده پیش فرض'))]"
continue_role_btn_xpath_locator = '//bhr-button[@btntitle="ادامه"]'

# locator in menu locator
# system_management
system_management_btn_menu_xpath_locator = '//span[text()="مدیریت سیستم"]'
structure_organization_btn_menu_link_text_locator = '/identity/organization'
role_organization_btn_menu_link_text_locator = '/identity/role/tree'
user_management_btn_menu_link_text_locator = '/identity/user-management'
user_access_management_btn_menu_link_text_locator = '/identity/user-access-management'
# planning
planing_btn_menu_xpath_locator = '//span[text()="برنامه‌ریزی"]'
planing_grid_btn_menu_link_text_locator = '/planing/grid'
# base information
base_information_btn_menu_xpath_locator = '//span[text()="اطلاعات پایه"]'
base_information_tree_btn_menu_link_text_locator = '/base-information/tree'
base_information_relations_btn_menu_link_text_locator = '/base-information/relations'
base_information_processes_relations_btn_menu_link_text_locator = '/base-information/processes-relations'
base_information_processes_places_btn_menu_link_text_locator = '/base-information/places'
# Human Capital
human_capital_btn_menu_xpath_locator = '//span[text()="سرمایه انسانی"]'
personal_grid_btn_menu_link_text_locator = '/personnel/grid'
# Certificate
certificate_btn_menu_link_text_locator = '//span[text()="گواهی نامه"]'
certificate_grid_btn_menu_link_text_locator = '/certificate/grid'
certificate_program_registration_btn_menu_link_text_locator = '/certificate-program-registration'
# utilization
utilization_btn_menu_xpath_locator = '//span[text()="بکارگیری"]'
utilization_grid_btn_menu_link_text_locator = '/utilization/grid'
# category_organization
add_category_organization_button_xpath_locator = '//input[@ value="افزودن"]'
