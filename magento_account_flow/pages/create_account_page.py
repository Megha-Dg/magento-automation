from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class CreateAccountPage(BasePage):
    FIRST_NAME = (By.ID, "firstname")
    LAST_NAME = (By.ID, "lastname")
    EMAIL = (By.ID, "email_address")
    PASSWORD = (By.ID, "password")
    CONFIRM_PASSWORD = (By.ID, "password-confirmation")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.action.submit.primary")

    def register_user(self):
        email = f"John{int(time.time())}@test.com"
        password = 'Johnmary@123987'
        self.enter_text(self.FIRST_NAME, "John")
        self.enter_text(self.LAST_NAME, "Mary")
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.PASSWORD, password)
        self.enter_text(self.CONFIRM_PASSWORD, password)
        self.click(self.SUBMIT_BUTTON)

        with open("user_credentials.txt","w+") as f:
            f.write(f"{email},{password}")

        return email, password
