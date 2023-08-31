import unittest
from selenium import webdriver
from GooglePage import GooglePage
from TestInit import TestInit

class GoogleTest(TestInit):
    def test_run_google(self):
        new_tab = GooglePage(self.getDriver())
        new_tab.goToGoogle()
        new_tab.getSearchField().send_keys("dogs\n")
        assert new_tab.getSearchField().is_displayed()

