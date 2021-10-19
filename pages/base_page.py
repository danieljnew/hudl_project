from selenium.webdriver.common.by import By
from typing import Tuple

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote import webelement
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver


class BasePage(object):

    Locator = Tuple[By, str]

    def __init__(self, driver):
        self.driver = driver

    def go_to_url(self, url: str):
        self.driver.get(url)

    def click(self, locator: Locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        click_element = self.driver.find_element(*locator)
        click_element.click()

    def click_checkbox(self, locator: Locator):
        action = ActionChains(self.driver)
        action.move_to_element(locator).click().perform()

    def enter_text(self, locator: Locator, text: str):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        text_element = self.driver.find_element(*locator)
        text_element.clear()
        text_element.send_keys(text)

    def find_element(self, locator: Locator, timeout: int = 10) -> webelement:
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return element
