from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    CREATE_ACCOUNT_LINK = (By.LINK_TEXT, "Create an Account")
    SIGN_IN_LINK = (By.LINK_TEXT, "Sign In")
    CUSTOMER_MENU = (By.XPATH, '//button[@data-action="customer-menu-toggle"]')
    SIGN_OUT_LINK = (By.CSS_SELECTOR, "li.authorization-link a")

    def go_to_create_account(self):
        self.click(self.CREATE_ACCOUNT_LINK)

    def go_to_sign_in(self):
        self.click(self.SIGN_IN_LINK)

    def logout(self):
        self.click(self.CUSTOMER_MENU)
        self.click(self.SIGN_OUT_LINK)
