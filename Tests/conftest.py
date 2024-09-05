from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption(
        "--driver_path", action="store", default="/home/cbnits/Documents/Makemytrip_Assignment/chromedriver"       
    )

@pytest.fixture(scope="class")
def driver_setup(request):
    BASE_URL = "https://www.makemytrip.com/"
    browser_name = request.config.getoption("browser_name")
    driver_path = request.config.getoption("driver_path")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-error')
    if browser_name == "chrome":
        # service_obj = Service("/home/cbnits/Downloads/chromedriver")
        service_obj = Service(driver_path)
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
        # driver = webdriver.Chrome(service=service_obj)
    driver.get(BASE_URL)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()