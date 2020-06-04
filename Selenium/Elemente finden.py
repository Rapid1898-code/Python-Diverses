# https://www.youtube.com/watch?v=Ak4-l5XkQ3k&list=PLNmsVeXQZj7ruEf-FwVD3Z5owHgdXNKlb&index=4

import unittest
import os
from selenium import webdriver

class GoogleTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome (os.getcwd () + '/chromedriver')

    def test_google_search(self):                   # Erster Testlauf
        self.driver.get("https://www.google.com/xhtml")
        self.assertIn("Google", self.driver.title)
        field = self.driver.find_element_by_name("q")
        field.send_keys("google")
        field.submit()
        assert "Es wurden keine mit deiner Suchanfrage - " not in self.driver.page_source

    def test_google_negative_search(self):          # Zweiter Testlauf
        self.driver.get("https://www.google.com/xhtml")
        self.assertIn("Google", self.driver.title)
        field = self.driver.find_element_by_name("q")
        field.send_keys("dsklfjalskjflakjfdlköjafslkdjf")
        field.submit()
        assert "Es wurden keine mit deiner Suchanfrage - " in self.driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


