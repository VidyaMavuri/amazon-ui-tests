from utils.driver_factory import get_driver
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage

def test_add_to_cart():
    driver = get_driver()
    try:
        home = HomePage(driver)
        results = SearchResultsPage(driver)
        product = ProductPage(driver)

        home.open()
        home.search("wireless mouse")

        results.click_first_product()
        product.add_to_cart()

        assert product.is_added_to_cart(), "Item was not added to cart"

    finally:
        driver.quit()
