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
def test1(driver):
  driver.get("www.google.pl")
  
  
#pass test to TestingService
test.fireTest(test1)
```
