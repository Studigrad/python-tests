# from selenium.webdriver.chrome import webdriver
# from selenium.webdriver.common.by import By
# from selenium import webdriver

from AmazonTest import AmazonTest
from GoogleTest import GoogleTest

def test_amazon():
    AmazonTest()

def test_google():
    GoogleTest()

# def func(x):
#     return x + 1
#
#
# # def test_answer():
# #     assert func(3) == 5
#
#
# def test_eight_components():
#     driver = webdriver.Firefox()
#
#     driver.get("https://www.google.com.ua/")
#
#     title = driver.title
#     #assert title == "Google"
#
#     textBox = driver.find_element(by=By.XPATH,value="//textarea[@class='gLFyf']")
#     btn = driver.find_element(by=By.XPATH, value="//div[@class='FPdoLc lJ9FBc']//input[@class='gNO89b']")
#     assert textBox.is_displayed()
#
#     textBox.send_keys("dogs")
#     btn.click()
#
#     result = driver.find_element(by=By.XPATH,value="//div[@id='result-stats']")
#     assert result.is_displayed()
