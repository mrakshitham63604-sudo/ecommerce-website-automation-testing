from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_cart_items(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(self.CART_ITEMS)
        )

    def checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()

    def continue_shopping(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_SHOPPING)
        ).click()