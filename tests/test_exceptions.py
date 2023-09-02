import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestExceptions:

    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        wait = WebDriverWait(driver, 10)
        row2_input_element = wait.until(
            ec.presence_of_element_located((By.XPATH, "(//input[@class='input-field'])[2]")))
        assert row2_input_element.is_displayed(), "Row 2 input should be displayed but it's no"

    @pytest.mark.exceptions
    def test_element_no_interactable_exception(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        wait = WebDriverWait(driver, 10)
        row2_input_element = wait.until(ec.presence_of_element_located((By.XPATH, "(//input["
                                                                                  "@class='input-field'])["
                                                                                  "2]")))
        row2_input_element.send_keys("Burger")

        driver.find_element(By.XPATH, "(//button[@name='Save'])[2]").click()

        confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        confirmation_message = confirmation_element.text
        assert confirmation_message == "Row 2 was saved", "confirmation massage is not displayed"

    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        row_1_edit_button = driver.find_element(By.ID, "edit_btn")
        row_1_edit_button.click()

        row_1_input_element = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        wait = WebDriverWait(driver, 10)
        wait.until(ec.element_to_be_clickable(row_1_input_element))
        row_1_input_element.clear()

        row_1_input_element.send_keys("Shushi")

        driver.find_element(By.ID, "save_btn").click()

        confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        confirmation_message = confirmation_element.text

        assert confirmation_message == "Row 1 was saved", "confirmation message is not displayed"

    @pytest.mark.exceptions
    @pytest.mark.debugs
    def test_stale_element_reference_exception(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.invisibility_of_element_located((By.ID, "instructions")),"Instruction text element should be displayed ")

    def test_timeout_exceptions(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()
        wait = WebDriverWait(driver, 6)
        assert wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='row2']/input"))," Input field should be displayed but it's not")



