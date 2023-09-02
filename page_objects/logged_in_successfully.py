from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoggedInSuccessfullyPage:
    _url = "https://practicetestautomation.com/practice-test-login/"
    __header_locator = (By.TAG_NAME, "h1")
    __logout_button_locator = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def excepted_url(self) -> str:
        return self._url

    @property
    def get_header(self) -> str:
        return self._driver.find_element(self.__header_locator).text

    def is_logout_button_displayed(self) -> bool:
        return self._driver.find_element(self.__logout_button_locator).is_displayed()
