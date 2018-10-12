from TestingService import Browsers, TestingService, ScreenSize
from BookstoreActions import Bookstore,serwisy
from credentials import username,password,bon
from selenium.webdriver.common.action_chains import ActionChains
import time


browsersList = [Browsers.Chrome.value]
test = TestingService(browsersList,ScreenSize.iphone5)
test.printSelectedBrowsers()

def test1(driver):
    driver.get("https://ebookpoint.pl")

#test.fireTest(test1)

def test2(driver):
    Bookstore.loginToBookstore(driver,"ebookpoint",username,password)

#test.fireTest(test2)

def test3(driver):
    Bookstore.loginToBookstore(driver,"ebookpoint",username,password)
    #it can bee just a prt of title its required to search in library
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

def test7(driver):
    #search without callback
    Bookstore.searchForPositionMainPage(driver,'ebookpoint',"java")

def test8(driver):
    #search with callback with argument
    Bookstore.searchForPositionMainPage(driver,'ebookpoint',"java",Bookstore.clickFromSuggestions,1)

def test9(driver):
    Bookstore.searchForPositionMainPage(driver,'ebookpoint',"java",Bookstore.clickFromSuggestions)

def testVideoPlayer(driver):
    for serwis in serwisy:
        driver.get("https://"+serwis+".pl/ksiazki/python-3-kurs-video-kompendium-efektywnego-pythonisty-bartosz-zaczynski,vpytpz.htm?xoxo=12345#format/w")
        try:
            element = driver.find_element_by_css_selector(".jp-controls-holder")
        except:
            continue
        driver.execute_script("window.scrollTo(0, $(\"#jp_container_N\").offset().top);")
        time.sleep(2)

test.fireTest(testVideoPlayer)
test.endTests()
