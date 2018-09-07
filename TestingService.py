from enum import Enum
from selenium import webdriver

class Browsers(Enum):
    firefox = "1"
    chrome = "2"
    opera = "3"
    internetexplorer = "4"

class TestingService:
    browsers = []
    def __init__(self, drivers):
        #declare which drivers should be used
        print(drivers)
        for driver in drivers:
            if driver == "1":
                #there we fire up drivers(browsers and add hanlder to list)
                self.browsers.append(webdriver.Firefox())
                print("appended")
            if driver == "2":
                print("not implemented")
    
    def printSelectedBrowsers(self):
        for browser in self.browsers:
            print("driver\n")

    #test is a function passed as argument it should have specified argument for a driver
    def fireTest(self, test):
        for browser in self.browsers:
            test(browser)