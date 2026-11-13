from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_successful_checkout(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(driver)
    products.add_product_to_cart()
    products.open_cart()

    cart = CartPage(driver)
    cart.checkout()

    checkout = CheckoutPage(driver)
    checkout.enter_details("John", "Smith", "560001")
    checkout.continue_checkout()
    checkout.finish_checkout()

    assert checkout.get_success_message() == "Thank you for your order!"


def test_checkout_without_first_name(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(driver)
    products.add_product_to_cart()
    products.open_cart()

    cart = CartPage(driver)
    cart.checkout()

    checkout = CheckoutPage(driver)
    checkout.enter_details("", "Smith", "560001")
    checkout.continue_checkout()

    error = driver.find_element("css selector", "[data-test='error']").text

    assert "First Name is required" in error