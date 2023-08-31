from BasePage import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

class AmazonPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def getTitleField(self):
        return self.getElementByXpath("//a[@id='nav-logo-sprites']")

    def getDeliverText(self):
        return self.getElementByXpath("//a[@id='nav-global-location-popover-link']")

    def getSearchInput(self):
        return self.getElementByXpath("//input[@id='twotabsearchtextbox']");

    def getSearchBtn(self):
        return self.getElementByXpath("//input[@id='nav-search-submit-button']");

    def getLanguageSelect(self):
        return self.getElementByXpath("//a[@id='icp-nav-flyout']");

    def getLoginField(self):
        return self.getElementByXpath("//a[@id='nav-link-accountList']");

    def getNavOrders(self):
        return self.getElementByXpath("//a[@id='nav-orders']");

    def getShoppingCart(self):
        return self.getElementByXpath("//a[@id='nav-cart']");

    def goToAmazon(self):
        self.driver.get("https://www.amazon.com/")