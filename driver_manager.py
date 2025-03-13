from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome

def get_driver():
    service = Service(ChromeDriverManager().install())
    driver = Chrome(service=service)
    return driver
