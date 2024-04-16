import unittest
from ddt import ddt, data, unpack
from selenium import webdriver
from Q1.page_objects.home_page import HomePage
import csv

def read_data_from_csv(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        return list(reader)

@ddt
class TestHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.home_page = HomePage(self.driver)

    @data(*read_data_from_csv('login_data.csv'))
    @unpack
    def test_sign_in(self, username, password):
        self.home_page.click_sign_in()
        self.home_page.enter_credentials(username, password)
        assert self.driver.current_url == 'http://www.example.com/sign-in'

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()