from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Config
from config import logger



class GumtreePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.TIMEOUT)

    """ Confirm the title is displayed"""
    def validate_page(self, link):
        self.driver.get(link)
        title = self.driver.title
        logger.info(f"Title of the page: {title}")
        assert title, "Title is not displayed"

        