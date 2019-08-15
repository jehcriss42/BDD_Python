# coding=utf-8
"""Login feature tests."""

from pytest_bdd import given,scenario,then,when

@scenario('../features/login.feature', 'Customer login to the application')
def test_customer_login_to_the_application():
    pass


@given('I am in the website')
def i_am_in_the_website():
    """I am in the website."""
    


@when('I pass my e-mail and my password')
def i_pass_my_email_and_my_password():
    """I pass my e-mail and my password."""


@when('I press Sign in')
def i_press_sign_in():
    """I press Sign in."""

@then('I can see my account')
def i_can_see_my_account():
    """I can see my account."""


