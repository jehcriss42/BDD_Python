# coding=utf-8
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pytest_bdd import given,scenario,then,when,parsers

"""Login feature tests."""

# Constants

AUTOMATION_SITE = "http://automationpractice.com/"

@scenario('/home/jessica/Documentos/BDD_Python/tests/features/login.feature','Customer login to the application')
def test_login():
    pass

# Fixtures

@pytest.fixture
def browser():
    path = "/home/jessica/Documentos/drivers/chromedriver"
    b = webdriver.Chrome(executable_path=path)
    b.implicitly_wait(10)
    yield b

@given('I am in the website')
def i_am_in_the_website(browser):
    browser.get(AUTOMATION_SITE)    

@when('I press Sign in')
def i_press_sign_in(browser):
    browser.find_element_by_class_name("login").click()

@when(parsers.parse('I pass my e-mail: "{email}" and my password: "{password}"'))
def i_pass_my_email_and_my_password(browser,email,password):
    browser.find_element_by_id("email").send_keys("aaa@jjj.com")
    browser.find_element_by_id("passwd").send_keys("12345")
    browser.find_element_by_id("SubmitLogin").click()

@then('I can see my account')
def i_can_see_my_account(browser):
    checkLogin = browser.find_element_by_class_name("account").text
    #Added this pause so it is possible to follow the test result
    assert "Jessica Tavares" in checkLogin
