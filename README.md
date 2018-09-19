# SeleniumTestingService
Small python library wchich uses selenium webdriver to perform tests on Bookstores

# Basic use 
```python
#required files and objects
from TestingService import Browsers, TestingService, ScreenSize
from BookstoreActions import Bookstore,serwisy

#init TestingService
browsersList = [Browsers.Chrome.value]
test = TestingService(browsersList,ScreenSize.hd)

#prepare some test
#driver param is obligatory when passing test to TestingService
def test(driver):
  driver.get("www.google.pl")
  
  
#pass test to TestingService
test.fireTest(test1)
```
# BookstoreActions 
  - Login to bookstore
```python
def test(driver):
    Bookstore.loginToBookstore(driver,service,username,password)
```
  - Try to download position from account on selected bookstore
```python
def test(driver):
    Bookstore.loginToBookstore(driver,service,username,password)
    Bookstore.tryToDownloadPosition(driver, service, title, fileFormat)
```
  - Add giftcard by form in basket
```python
def test(dirver):
     Bookstore.loginToBookstore(driver,service,username,password)
     Bookstore.tryToAddBonToBasket(driver,service,bon)
```
  - Add position to basket
```python
def test(driver):
    #You can be logged in but you don't have to
    #Bookstore.loginToBookstore(driver,service,username,password)
    Bookstore.addPositionToBasket(driver, service, troya, format)
    #possible formats: ebook, druk, audiobook
```
  - Place order from basket
```python
def test(driver):
    #Being logged is optional
    #Bookstore.loginToBookstore(driver, service,username,password)
    Bookstore.placeOrder(driver, service)
```
  - Check if search suggestions are working properly version 
```python
def test(driver):
    #search without callback
    Bookstore.searchForPositionMainPage(driver, service, searchPhrase)
    #Bookstore.searchForPositionMainPage(driver, service, searchPhrase,Bookstore.clickFromSuggestions,1) with callback and argument passed to callback
    #Bookstore.searchForPositionMainPage(driver, service, searchPhrase,Bookstore.clickFromSuggestions) witch callback and default param in callback
```
