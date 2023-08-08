import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

PATH = "C:\\Users\\user\\Documents\\Alisher\\python\\chromedriver.exe"

HALF_SECOND = 0.5


class Fullstack(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=Service(PATH), options=options)
        self.driver.maximize_window()
        # self.current_test = self.id().split(".")[-1]

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print(f"Ending test for {self.driver}")

    def test_login_to_facebook(self):
        pass

    def test_wikipedia(self):
        self.driver.get("https://www.wikipedia.org/")
        print("Getting url...")
        slogan = self.driver.find_element(By.CLASS_NAME, "localized-slogan")
        print(slogan)
        print("ID: -> ", slogan.get_property("id"))
        print("link.text: -> ", slogan.text)

        text_to_write = "FullStack programming"
        search_input = self.driver.find_element(By.ID, "searchInput")
        search_input.send_keys(text_to_write)
        time.sleep(HALF_SECOND)
        btn = self.driver.find_element(By.CLASS_NAME, "svg-search-icon")
        btn.click()
        time.sleep(HALF_SECOND*2)
        expected_heading = self.driver.find_element(By.ID, "firstHeading")
        assert expected_heading.text == "Search results"
        assert "Search results" in self.driver.page_source


# to run this test from command line:
# python -m unittest -v functional_tests.py
# -v  =>  verbose mode  (means that we will see all the output from the test)
# -m  =>  module  (means that we will run the test from the module)
