import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

@given('the user is on the Hudl login page')
def step_open_hudl_login_page(context):
    context.driver = webdriver.Firefox()
    context.driver.set_window_size(996, 988)
    context.driver.get("https://www.hudl.com/en_gb/")
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Log in"))
    ).click()
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".subnav__item:nth-child(1) > .subnavitem__label"))
    ).click()

@when('the user enters a valid email')
def step_enter_valid_email(context):
    email = os.getenv("HUDL_EMAIL", "correct_email@email.com")
    context.driver.find_element(By.ID, "username").send_keys(email)

@when('the user enters an invalid email')
def step_enter_invalid_email(context):
    context.driver.find_element(By.ID, "username").send_keys("invalid_email@gmail.com")

@when('the user enters an empty email')
def step_enter_empty_email(context):
    context.driver.find_element(By.ID, "username").send_keys("")

@when('the user enters a valid password')
def step_enter_valid_password(context):
    password = os.getenv("HUDL_PASSWORD", "securepassword")
    context.driver.find_element(By.ID, "password").send_keys(password)

@when('the user enters an invalid password')
def step_enter_invalid_password(context):
    context.driver.find_element(By.ID, "password").send_keys("wrongpassword123")

@when('the user enters an empty password')
def step_enter_empty_password(context):
    context.driver.find_element(By.ID, "password").send_keys("")

@when('clicks the login button')
def step_click_login(context):
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "action"))
    ).click()

@then('the user should be redirected to the dashboard')
def step_verify_dashboard(context):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains("home")
    )
    assert "home" in context.driver.current_url, "❌ Login failed, not redirected to dashboard!"

@then('an error message should be displayed')
def step_verify_error_message(context):
    error_message = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "error-element-password"))
    )
    assert error_message.is_displayed(), "❌ No error message displayed!"

def after_scenario(context, scenario):
    context.driver.quit()