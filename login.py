from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.XPATH, '//*[@id="username"]')
        self.password_input = (By.XPATH, '//*[@id="password"]')
        self.login_button = (By.XPATH, '//*[@id="login"]')

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()
