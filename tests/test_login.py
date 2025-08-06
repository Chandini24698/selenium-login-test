import pytest
from selenium import webdriver
from pages.login_page import LoginPage

def test_valid_login():
    driver = webdriver.Chrome()
    login = LoginPage(driver)
    login.open_login_page()
    login.login("student", "Password123")
    assert "Logged In Successfully" in driver.page_source
    driver.quit()
