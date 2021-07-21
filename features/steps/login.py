from behave import given
from behave import then
from behave import when
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given('launch the application')
def launch_app(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


@when('open the orangeHrm')
def open_app(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewAdminModule")


@then('verify login to app')
def login_to_app(context):
    context.driver.find_element(By.ID, 'txtUsername').send_keys('Admin')
    context.driver.find_element(By.ID, 'txtPassword').send_keys('admin123')
    context.driver.find_element(By.ID, 'btnLogin').click()


@then('Enter the username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element(By.ID, 'txtUsername').send_keys(user)
    context.driver.find_element(By.ID, 'txtPassword').send_keys(pwd)
    context.driver.find_element(By.ID, 'btnLogin').click()


@then('close browser')
def close_browser(context):
    try:
        text = context.driver.find_element(By.XPATH, "//*[@id='content']/div/div[1]/h1").text
        print(text)
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Dashboard":
        context.driver.close()
        assert True, "Test Passed"
