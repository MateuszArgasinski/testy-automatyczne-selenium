
import pytest


from page_objects.logged_in_successfully import LoggedInSuccessfullyPage
from page_objects.login_page import LoginPage


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):

        login_page = LoginPage(driver)
        login_page.open()

        login_page.execute_login("student", "Password123")
        logged_in_page = LoggedInSuccessfullyPage(driver)
        assert logged_in_page.excepted_url == logged_in_page.current_url, "actual URL is not the same as excepted"
        assert logged_in_page.header == "Logged In Successfully", "header is not excepted"
        assert logged_in_page.is_logout_button_displayed(), "Logout button should be visible"



