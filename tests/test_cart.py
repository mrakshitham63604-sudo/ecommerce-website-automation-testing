from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_cart_contains_added_product(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(driver)
    products.add_product_to_cart()
    products.open_cart()

    cart = CartPage(driver)

    assert len(cart.get_cart_items()) == 1


def test_checkout_button(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(driver)
    products.add_product_to_cart()
    products.open_cart()

    cart = CartPage(driver)
    cart.checkout()

    assert "checkout-step-one" in driver.current_url