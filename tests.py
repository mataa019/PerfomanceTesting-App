import time
import pandas as pd
from selenium import webdriver
from login import LoginPage
from register import RegisterPage

class TestWebApp:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000")

    def test_login(self):
        login_data = pd.read_csv('loginTestData.csv')
        for _, row in login_data.iterrows():
            username = row['username']
            password = row['password']
            login_page = LoginPage(self.driver)
            login_page.enter_username(username)
            login_page.enter_password(password)
            login_page.click_login_button()
            # Add assertions for successful login
        time.sleep(10)  # Pause for 10 seconds after the test

    def test_register(self):
        register_data = pd.read_csv('registerTestData.csv')
        for _, row in register_data.iterrows():
            email = row['email']
            password = row['password']
            confirm_password = row['confirm_password']
            register_page = RegisterPage(self.driver)
            register_page.enter_email(email)
            register_page.enter_password(password)
            register_page.confirm_password(confirm_password)
            register_page.click_register_button()
            # Add assertions for successful registration
        time.sleep(10)  # Pause for 10 seconds after the test

    def teardown_method(self):
        self.driver.quit()