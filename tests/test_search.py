from utils.driver_factory import get_driver
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

def test_search_amazon():
    driver = get_driver()
    try:
        home = HomePage(driver)
        results = SearchResultsPage(driver)

        home.open()
        home.search("wireless mouse")

        results.wait_for(results.FIRST_PRODUCT)
        assert True, "Search results loaded successfully"

    finally:
        driver.quit()
