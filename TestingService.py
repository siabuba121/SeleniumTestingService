import time
from enum import Enum
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

class Browsers(Enum):
    Firefox = "1"
    Chrome = "2"
    Opera = "3"
    Ie = "4"

class ScreenSize(Enum):
    hd = [1280,720]
    fullhd = [1920,1080]
    iphone7 = [750,1334]

class TestingService:
    browsers = []

    def __init__(self, drivers, screenSize):

        for driver in drivers:
            if driver == "1":
                self.browsers.append(webdriver.Firefox(firefox_profile=self.getAutoDownloadOptionsFirefox()))
            if driver == "2":
                self.browsers.append(webdriver.Chrome())
            if driver == "3":
                self.browsers.append(webdriver.Opera())
            if driver == "4":
                self.browsers.append(webdriver.Ie())

        self.setScreenSize(screenSize)

    #screen size set
    def setScreenSize(self, screenSize):
        if screenSize == "":
            screenSize = ScreenSize.hd
        for driver in self.browsers:
            driver.set_window_size(screenSize.value[0],screenSize.value[1])


    #for checking passing arguments probably no use in testing 
    def printSelectedBrowsers(self):
        for browser in self.browsers:
            print(browser)

    #test is a function passed as argument it should have specified argument for a driver
    def fireTest(self, test):
        for browser in self.browsers:
            test(browser)

    def getAutoDownloadOptionsFirefox(self):
        profile = FirefoxProfile()
        profile.set_preference("browser.download.panel.shown", False)
        profile.set_preference("browser.download.folderList", 2);
        profile.set_preference("browser.download.dir", "c:\\temp\\")
        #only works on downloading epub i dont know why
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", '["application/epub+zip","application/pdf","application/mobi","application/zip"]')

        return profile

    def endTests(self):
        time.sleep(2)
        for driver in self.browsers:
            driver.quit()