import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Make sure ChromeDriver is installed
    yield driver
    driver.quit()

def test_google_title(browser):
    browser.get("https://www.royalenfield.com/in/en/home/")
    assert "Royal Enfield India | Roadster, Adventure, Cruiser Motorcycles India" in browser.title