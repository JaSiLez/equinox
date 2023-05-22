from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

use_step_matcher("re")


@given("I am an Equinox Admin")
def step_impl(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.set_capability("browserVersion", "113.0.5672.126")
    chrome_options.set_capability("platformName", "linux")
    context.selenium = webdriver.Chrome(options=chrome_options)
    # Login to the Admin Panel
    context.selenium.get(f'{context.test.live_server_url}/admin/')

    # Fill Login Information
    username = context.selenium.find_element("name", "username")
    username.send_keys("admin")
    password = context.selenium.find_element("name", "password")
    password.send_keys("admin")


@when('I click on the Login link')
def step_impl(context):
    # Locate login button and click on it
    context.selenium.find_element(By.XPATH, '//button[normalize-space()="Log in"]').click()


@then('I am on the Equinox Admin page')
def step_impl(context):
    context.test.assertEquals(context.selenium.title, "Site administration | Equinox")
