import pytest
from pages.google_page import GooglePage
from pages.gumtree_page import GumtreePage
from utils.driver_manager import get_driver
from config import logger
from config import Config

class TestCarSearch:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = get_driver()
        self.google_page = GooglePage(self.driver)
        self.gumtree_page = GumtreePage(self.driver)
        yield
        self.driver.quit()

    def test_search_validation(self):
        """Open Google page"""
        self.google_page.open_page()

        """Perform search"""
        self.google_page.search(Config.SEARCH_TERM)

        """# Collect Gumtree links"""
        gumtree_links = self.google_page.extract_gumtree_links()
        logger.info(f"Number of Gumtree links found: {len(gumtree_links)}")

        """ Validate the number of Gumtree links found is greater than 0"""
        assert len(gumtree_links) > 0, "No Gumtree links found"

        """ Navigate to each Gumtree link"""
        for link in gumtree_links:
            self.gumtree_page.validate_page(link)

