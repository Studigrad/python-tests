from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from BasePage import BasePage

class GooglePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def getSearchField(self) -> WebElement:
        return self.getElementByXpath("//textarea[@id='APjFqb']")

    def goToGoogle(self):
        self.driver.get("https://www.google.com.ua/")
