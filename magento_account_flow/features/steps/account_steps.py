import time

from behave import given, when, then
from pages.home_page import HomePage
from pages.create_account_page import CreateAccountPage
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('the user is on the Magento homepage')
def step_implementation(context):
    context.driver.get("https://magento.softwaretestingboard.com/")
    time.sleep(15)
    context.home_page = HomePage(context.driver)


@when('the user navigates to Create Account page')
def step_implementation(context):
    context.home_page.go_to_create_account()
    context.create_account_page = CreateAccountPage(context.driver)


@when('the user fills in valid registration details')
def step_implementation(context):
    context.email, context.password = context.create_account_page.register_user()
    WebDriverWait(context.driver, 10).until(
        lambda d: "Welcome" in d.page_source
    )


@then('the account should be created successfully')
def step_implementation(context):
    assert "Welcome" in context.driver.page_source


@then('the user logs out')
def step_implementation(context):
    context.home_page.logout()
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(HomePage.SIGN_IN_LINK)
    )


@when('the user navigates to Sign In page')
def step_implementation(context):
    context.home_page.go_to_sign_in()
    context.login_page = LoginPage(context.driver)


@when('the user enters valid login credentials')
def step_implementation(context):
    with open("user_credentials.txt", "r") as f:
        email, password = f.read().strip().split(",")

    context.login_page.login(email, password)
    time.sleep(5)


@then('the user should be logged in and see the dashboard')
def step_implementation(context):
    WebDriverWait(context.driver, 10).until(
        lambda d: "Welcome" in d.page_source
    )
    assert "Welcome" in context.driver.page_source
