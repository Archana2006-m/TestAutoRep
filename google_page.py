import time
from config import Config
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import shared_logger
class GooglePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.TIMEOUT)
    def open_page(self):
        """Open the Google Page"""
        self.driver.get(Config.BASE_URL)
        self.wait.until(EC.presence_of_element_located((By.NAME, "q")))
        shared_logger.info("Opening the Google Page")
    def search(self, query):
        """ Perform a search on Google."""
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.clear()
        for char in query:
            search_box.send_keys(char)
            time.sleep(0.1)
        search_box.send_keys(Keys.RETURN)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.g'))) # Wait for results to load
    def get_search_results(self):
        """Retrieve all search result elements."""
        shared_logger.info("Retrieving the Google Search Results")
        return self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.g')))
    def extract_gumtree_links(self):
        """ Extract Gumtree links from the search results."""
        results = self.get_search_results()
        gumtree_links = []
        for result in results:
            try:
                link = result.find_element(By.TAG_NAME, 'a').get_attribute('href')
                if Config.GUMTREE_DOMAIN in link:
                    gumtree_links.append(link)
            except Exception as e:
                shared_logger.info(f"Error extracting link: {e}")
        return gumtree_links

    
