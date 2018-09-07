from TestingService import Browsers,TestingService

browsersList = [Browsers.Firefox.value]
test = TestingService(browsersList)
test.printSelectedBrowsers()

def test1(driver):
    driver.get("https://ebookpoint.pl")

test.fireTest(test1)
