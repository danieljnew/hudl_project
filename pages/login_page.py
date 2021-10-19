from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    EMAIL_FIELD = [By.ID, "email"]
    PASSWORD_FIELD = [By.ID, "password"]
    LOGIN_BTN = [By.ID, "logIn"]
    REMEMBER_ME = [By.ID, "remember-me"]
    LOGIN_ERROR_MSG = [By.XPATH, '//div[@class="login-error-container"]/p']

    def login_with_credentials(self, username: str, password: str, remember_me: bool = False):
        self.enter_text(self.EMAIL_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        if remember_me:
            remember_check = self.find_element(self.REMEMBER_ME)
            self.click_checkbox(remember_check)
        self.click(self.LOGIN_BTN)

    def remembered_username(self) -> str:
        remembered_name = self.find_element(self.EMAIL_FIELD)
        return remembered_name.get_attribute('value')

    def get_login_error_message(self) -> str:
        error_message = self.find_element(self.LOGIN_ERROR_MSG)
        return error_message.text
