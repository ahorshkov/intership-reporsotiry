from pages.base_page import Page

class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "h1[class*=StyledHeading']")

     def verify_cart_empty_msg(self):
            # actual_text = self.find_element(*self.CART_EMPTY_MSG).text
            # expected_text = 'Your cart is empty'
            # assert expected_text == actual_text, f'Expected {expected_text}, got {actual_text}
            self.verify_text('Your cart is empty', self.find_element(*self.CART_EMPTY_MSG).text)