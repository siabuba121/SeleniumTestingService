from enum import Enum
from selenium import webdriver

class Browsers(Enum):
    Firefox = "1"
    Chrome = "2"
    Opera = "3"
    Ie = "4"

class TestingService:
    browsers = []

    def __init__(self, drivers):
        for driver in drivers:
            if driver == "1":
                self.browsers.append(webdriver.Firefox())
            if driver == "2":
                self.browsers.append(webdriver.Chrome())
            if driver == "3":
                self.browsers.append(webdriver.Opera())
            if driver == "4":
                self.browsers.append(webdriver.Ie())
    
    #for checking passing arguments probably no use in testing 
    def printSelectedBrowsers(self):
        for browser in self.browsers:
            print("driver\n")

    #test is a function passed as argument it should have specified argument for a driver
    def fireTest(self, test):
        for browser in self.browsers:
            test(browser)