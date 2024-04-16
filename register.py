from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.XPATH, '//*[@id="email"]')
        self.password_input = (By.XPATH, '//*[@id="registerPassword"]')
        self.confirm_password_input = (By.XPATH, '//*[@id="confirmPassword"]')
        self.register_button = (By.XPATH, '//*[@id="register"]')

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def confirm_password(self, password):
        self.driver.find_element(*self.confirm_password_input).send_keys(password)

    def click_register_button(self):
        self.driver.find_element(*self.register_button).click()
