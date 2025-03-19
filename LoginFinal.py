import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class TestLoggingIntoHudl:
    def setup_method(self, method):
        """Set up the WebDriver before each test."""
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(996, 988)
        self.vars = {}

    def teardown_method(self, method):
        """Close the WebDriver after each test."""
        self.driver.quit()

    def login(self, email, password):
        self.driver.get("https://www.hudl.com/en_gb/")
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        self.driver.find_element(By.CSS_SELECTOR, ".subnav__item:nth-child(1) > .subnavitem__label").click()

        self.driver.find_element(By.ID, "username").send_keys(email)
        self.driver.find_element(By.NAME, "action").click()
        time.sleep(2)

        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.NAME, "action").click()
        time.sleep(2)

    def check_error_message(self):
        return WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "error-element-password"))
        )

    def test_valid_login(self):
        """Test valid login credentials."""
        self.login("s.harbage@gmail.com", "")
        assert "home" in self.driver.current_url, "❌ Login failed, did not reach dashboard!"
        print("✅ Valid login test passed.")

    def test_invalid_email(self):
        """Test login with an incorrect email."""
        self.login("invalid_email@gmail.com", "")
        error_message = self.check_error_message()
        assert error_message.is_displayed(), "❌ Error message not displayed for invalid email!"
        print("✅ Invalid email test passed.")

    def test_invalid_password(self):
        """Test login with an incorrect password."""
        self.login("s.harbage@gmail.com", "wrongpassword123")
        error_message = self.check_error_message()
        assert error_message.is_displayed(), "❌ Error message not displayed for invalid password!"
        print("✅ Invalid password test passed.")

    def test_invalid_email_and_password(self):
        """Test login with both incorrect email and password."""
        self.login("fakeemail@example.com", "fakepassword")
        error_message = self.check_error_message()
        assert error_message.is_displayed(), "❌ Error message not displayed for invalid email and password!"
        print("✅ Invalid email & password test passed.")

    def test_empty_email(self):
        """Test login with an empty email field."""
        self.login("", "")
        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[text()='Please fill in this field']"))
        )
        assert error_message.is_displayed(), "Error message 'Please fill in this field' not found."
        print("✅ Invalid email test passed.")

    def test_empty_password(self):
        """Test login with an empty password field."""
        self.login("s.harbage@gmail.com", "")
        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Please fill in this field')]"))
        )
        assert error_message.is_displayed(), "Error message 'Please fill in this field' for password not found."
        print("✅ Invalid password test passed.")