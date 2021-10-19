from pages.login_page import LoginPage
from pages.home_page import HomePage
from selenium import webdriver
import const
import pytest
import json


@pytest.fixture(scope="class")
def base_driver(request):
    driver = webdriver.Chrome(executable_path=const.CHROME_BINARY_PATH)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def load_credentials(request):
    with open('config.json') as file:
        config = json.load(file)
    username = config["users"][0]["username"]
    password = config["users"][0]["password"]
    yield username, password


@pytest.fixture()
def login(request, base_driver, load_credentials):
    login_page = LoginPage(base_driver)
    login_page.go_to_url(const.HUDL_LOGIN_URL)
    login_page.login_with_credentials(load_credentials[0], load_credentials[1])
    yield login_page


class TestLogin(object):

    def test_user_can_login(self, base_driver: webdriver, load_credentials):
        login_page = LoginPage(base_driver)
        login_page.go_to_url(const.HUDL_LOGIN_URL)
        login_page.login_with_credentials(load_credentials[0], load_credentials[1])
        home_page = HomePage(login_page)
        logged_in_user = home_page.get_logged_in_user()
        assert logged_in_user == const.LOGGED_IN_COACH

    def test_user_can_logout(self, login):
        home_page = HomePage(login)
        home_page.log_out()
        assert home_page.get_logged_in_user() == "No user logged in"

    def test_remember_me_remembers(self, base_driver: webdriver, load_credentials):
        login_page = LoginPage(base_driver)
        login_page.go_to_url(const.HUDL_LOGIN_URL)
        login_page.login_with_credentials(load_credentials[0], load_credentials[1], remember_me=True)
        home_page = HomePage(login_page)
        home_page.log_out()
        login_page.go_to_url(const.HUDL_LOGIN_URL)
        assert login_page.remembered_username() == load_credentials[0]

    def test_wrong_password_message(self, base_driver: webdriver, load_credentials):
        login_page = LoginPage(base_driver)
        login_page.go_to_url(const.HUDL_LOGIN_URL)
        login_page.login_with_credentials(load_credentials[0], const.BAD_PASSWORD)
        assert login_page.get_login_error_message() is not None

    def test_wrong_email_message(self, base_driver: webdriver, load_credentials):
        login_page = LoginPage(base_driver)
        login_page.go_to_url(const.HUDL_LOGIN_URL)
        login_page.login_with_credentials(const.BAD_USERNAME, load_credentials[1])
        assert login_page.get_login_error_message() is not None

    def test_no_email_or_password(self, base_driver: webdriver):
        login_page = LoginPage(base_driver)
        login_page.go_to_url(const.HUDL_LOGIN_URL)
        login_page.login_with_credentials("", "")
        assert login_page.get_login_error_message() is not None

    def test_no_email_correct_password(self, base_driver: webdriver, load_credentials):
        login_page = LoginPage(base_driver)
        login_page.go_to_url(const.HUDL_LOGIN_URL)
        login_page.login_with_credentials("", load_credentials[1])
        assert login_page.get_login_error_message() is not None

    def test_no_password_correct_email(self, base_driver:webdriver, load_credentials):
        login_page = LoginPage(base_driver)
        login_page.go_to_url(const.HUDL_LOGIN_URL)
        login_page.login_with_credentials(load_credentials[0], "")
        assert login_page.get_login_error_message() is not None
