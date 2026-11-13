from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_products_page_title(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(driver)

    assert products.get_title() == "Products"


def test_add_product_to_cart(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(driver)
    products.add_product_to_cart()

    assert products.get_cart_count() == "1"


def test_open_cart(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(driver)
    products.add_product_to_cart()
    products.open_cart()

    assert "cart.html" in driver.current_url