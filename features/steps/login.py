from behave import given, when, then

from urllib.parse import urljoin
from data.config import settings


@given('I load the website')
def step_impl(context):
    context.browser.visit()


@when('I enter the credentials "{admin}" for user and "{rhebo}" for password')
def step_impl(context, admin, rhebo):
    username_field = context.browser.find_by_xpath('//*[@id="username"]')
    password_field = context.browser.find_by_xpath('//*[@id="password"]')
    username_field.send_keys(admin)
    password_field.send_keys(rhebo)
    submit_button = context.browser.find_by_xpath('//*[@id="login-button"]')
    submit_button.click()


@then('I should be redirected to the "{page}" page')
def step_impl_login_as_admin(context, page):
    assert urljoin(settings['base_url'], page.lower()) == context.browser.get_url(), 'Login failed'
