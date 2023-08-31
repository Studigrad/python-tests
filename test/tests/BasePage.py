from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def getElementByXpath(self, path: str) -> WebElement:
        return self.driver.find_element(By.XPATH, path)