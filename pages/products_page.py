from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:

    TITLE = (By.CLASS_NAME, "title")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.TITLE)
        ).text

    def add_product_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(self.CART_BADGE)
        )

    def open_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CART_ICON)
        ).click()

    def get_cart_count(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.CART_BADGE)
        ).text