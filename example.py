from TestingService import Browsers,TestingService
from BookstoreActions import Bookstore
from credentials import username,password

browsersList = [Browsers.Firefox.value]
test = TestingService(browsersList)
test.printSelectedBrowsers()

def test1(driver):
    driver.get("https://ebookpoint.pl")

#test.fireTest(test1)

def test2(driver):
    Bookstore.loginToBookstore(driver,"ebookpoint",username,password)

#test.fireTest(test2)

def test3(driver):
    Bookstore.loginToBookstore(driver,"ebookpoint",username,password)
    Bookstore.tryToDownloadPosition(driver, "ebookpoint", "nowoczesny javascript. poznaj es6 i praktyczne","mobi")

test.fireTest(test3)
