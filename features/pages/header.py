from selenium.webdriver.common.by import By

from pages.base_page import Page


class Header(Page):
    SEARCH_INPUT = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")

    def search_product(self, item):
        self.input_text(item, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)

    def click_cart(self):
        self.wait_until_clickable_click(*self.CART_ICON)
        self.save_screenshot('clicked_cart.png')