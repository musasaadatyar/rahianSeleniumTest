from archives.classpages.submit.submit import Submit
from archives.classpages.checkStatusPhoneNumber.checkStatusPhoneNumber import CheckStatusPhoneNumber
from time import sleep


class SubmitTest:
    def __init__(self, driver, connection):
        self.driver = driver
        self.connection = connection

    def test_submit_user(self):
        cursor = self.connection.execute("SELECT * from submitUsers")
        self.driver.get('http://localhost:4200/landing')
        submit_obj = Submit(self.driver)
        check_status_phone_number_obj = CheckStatusPhoneNumber(self.driver)
        submit_obj.click_submit_enter_submit_main_page()
        submit_obj.enter_submit_button_link_login()
        for row in cursor:
            submit_obj.clear_enter_national_code()
            submit_obj.enter_national_code(row[1])
            submit_obj.clear_enter_phone_number()
            submit_obj.enter_phone_number(row[2])
            submit_obj.clear_enter_birth_date()
            submit_obj.enter_birth_date(row[3])
            submit_obj.clear_enter_password()
            submit_obj.enter_password(row[4])
            submit_obj.clear_confirm_password()
            submit_obj.confirm_password(row[5])
            submit_obj.click_submit_btn()
            print(row)
            check_status_phone_number_obj.close_pup_up_btn()
            # sleep(239847648)
            # sleep(12313)
            if check_status_phone_number_obj.close_pup_up_btn():
                check_status_phone_number_obj.close_pup_up_btn()
                sleep(4)
                print(1)
            else:
                check_status_phone_number_obj.enter_submit_button_link_login()
                sleep(4)
                print(2)
