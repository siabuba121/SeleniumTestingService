from TestingService import Browsers, TestingService, ScreenSize
from BookstoreActions import Bookstore,serwisy
from credentials import username,password,bon


browsersList = [Browsers.Chrome.value]
test = TestingService(browsersList,ScreenSize.fullhd)
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

#test bony
def test4(driver):
    for serwis in serwisy:
        Bookstore.loginToBookstore(driver,serwis,username,password)
        Bookstore.tryToAddBonToBasket(driver,serwis,bon)

def test5(driver):
    Bookstore.loginToBookstore(driver,"ebookpoint",username,password)
    Bookstore.addPositionToBasket(driver, "ebookpoint", "e_0unv", "ebook")

def test6(driver):
    Bookstore.loginToBookstore(driver,"ebookpoint",username,password)
    Bookstore.placeOrder(driver,"ebookpoint")

test.fireTest(test6)
test.endTests()
