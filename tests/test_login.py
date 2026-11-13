from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_valid_login(driver):
    login = LoginPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(driver)

    assert products.get_title() == "Products"


def test_invalid_login(driver):
    login = LoginPage(driver)

    login.open()
    login.login("invalid_user", "wrong_password")

    assert "Username and password do not match" in login.get_error_message()


def test_locked_user_login(driver):
    login = LoginPage(driver)

    login.open()
    login.login("locked_out_user", "secret_sauce")

    assert "locked out" in login.get_error_message().lower()
    