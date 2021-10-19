from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver


class HomePage(BasePage):

    LOGOUT_BTN = [By.XPATH, '//a[@data-qa-id="webnav-usermenu-logout"]']
    USER_NAME = [By.XPATH, '//div[@class="hui-globaluseritem__display-name"]/span']

    def get_logged_in_user(self) -> str:
        try:
            email_element = self.driver.find_element(self.USER_NAME, timeout=5)
        except:
            return "No user logged in"
        return email_element.text

    def log_out(self):
        move_to = ActionChains(self.driver)
        self.driver.click(self.USER_NAME)
        log_out = self.driver.find_element(self.LOGOUT_BTN)
        move_to.move_to_element(log_out)
        self.driver.click(self.LOGOUT_BTN)
