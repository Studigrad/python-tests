from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest


class TestInit(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def getDriver(self):
        return self.driver

    def tearDown(self):
        self.driver.quit()
