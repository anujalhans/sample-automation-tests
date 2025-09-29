import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Ensure ChromeDriver is installed & in PATH
    driver.maximize_window()
    yield driver
    driver.quit()

def accept_cookies_if_present(driver):
    """Utility to accept cookies if the popup is present"""
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept')]"))
        ).click()
    except:
        # No popup found → continue silently
        pass


def test_royal_enfield_title(browser):
    """Check if the page title is correct"""
    browser.get("https://www.royalenfield.com/in/en/home/")
    accept_cookies_if_present(browser)
    assert "Royal Enfield India | Roadster, Adventure, Cruiser Motorcycles India" in browser.title


def test_royal_enfield_logo_visible(browser):
    """Check if the Royal Enfield logo is displayed"""
    browser.get("https://www.royalenfield.com/in/en/home/")
    accept_cookies_if_present(browser)
    logo = browser.find_element(By.CSS_SELECTOR, "img[alt='Royal Enfield India']")
    assert logo.is_displayed(), "Royal Enfield logo should be visible on the homepage"


def test_motorcycles_navigation(browser):
    """Check if navigation to 'Motorcycles' page works"""
    browser.get("https://www.royalenfield.com/in/en/home/")
    accept_cookies_if_present(browser)
    motorcycles_link = browser.find_element(By.XPATH, "//a[@title='Motorcycles']//span[@class='desktop-title-text']")
    motorcycles_link.click()

    # Allow time for navigation (you can replace with WebDriverWait if needed)
    browser.implicitly_wait(5)
    assert "Motorcycles" in browser.title or "motorcycles" in browser.current_url
