from behave import given, when, then

from urllib.parse import urljoin
from data.config import settings


@given('I load the website')
def step_impl(context):
    context.login.visit()


@when('I enter the credentials "{admin}" for user and "{rhebo}" for password')
def step_impl(context, admin, rhebo):
    context.login.login(admin, rhebo)


@then('I should be redirected to the "{page}" page')
def step_impl(context, page):
    assert urljoin(settings['base_url'], page.lower()) == context.login.get_current_url(), 'Login failed'
