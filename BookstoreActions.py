from selenium.webdriver.common.action_chains import ActionChains
import time

serwisy = ['videopoint','helion','editio','ebookpoint','onepress','sensus','septem','bezdroza',]

class Bookstore:
    logged = dict()
    
    @staticmethod
    def loginToBookstore(webdriver, service, username, password):
        webdriver.get("https://"+service+".pl/users/index2.cgi")
        login = webdriver.find_element_by_name("loginemail")
        login.send_keys(username)
        haslo = webdriver.find_element_by_name("haslo")
        haslo.send_keys(password)
        button = webdriver.find_element_by_css_selector(".form.form-left fieldset .buttons button").click()
        #some functions will require user to be logged in so i  added flags if user is actually logged on each service
        Bookstore.logged[service] = 1

    @staticmethod
    def tryToDownloadPosition(webdriver, service, title, format):
        if Bookstore.logged[service] != 1:
            print("User nie jest zalogowany do serissu "+service+"\n")
        else:
            webdriver.get("https://"+service+".pl/users/konto/biblioteka")
            search = webdriver.find_element_by_css_selector(".searchlib")
            search.send_keys(title)
            bookelem = webdriver.find_element_by_css_selector(".list.lista .cover")
            ActionChains(webdriver).click(bookelem).perform()

            while webdriver.find_element_by_css_selector(".spinnerdiv").is_displayed():
                #loop to wait for position to be generated
                time.sleep(2)

            downloadButton = webdriver.find_element_by_css_selector(".modalbutton#"+format+"_button")
            downloadButton.click()

    @staticmethod
    def tryToAddBonToBasket(webdriver,service,bonid):
        if Bookstore.logged[service] != 1:
            print("User nie jest zalogowany do serissu "+service+"\n")
        else:
            webdriver.get("https://"+service+".pl/zakupy/edit.cgi?xoxo=12345")
            
            if webdriver.find_element_by_css_selector("#kuponinp").is_displayed() == 0:
                webdriver.execute_script("jQuery(\"#strefapromocji .checkbox-line label\")[2].click()")
                print("3 opcja")

            inputKupon = webdriver.find_element_by_css_selector("#kuponinp")
            inputKupon.send_keys(bonid)
            submit = webdriver.find_element_by_css_selector("#kuponok")
            if service == "videopoint":
                webdriver.execute_script("jQuery(\"#kuponok\").click()")
            else:
                submit.click()

            time.sleep(2)
    
    @staticmethod
    def addPositionToBasket(webdriver, service, ident, format):
        #specifying format
        if format == "ebook":
            format = "#format/e"
            btn_id = "ebook"
        elif format == "druk":
            format = "#format/d"
            btn_id = ""
        elif format == "audiobook":
            format = "#format/3"
            btn_id = "3"

        webdriver.get("https://"+service+".pl/ksiazka.cgi?book_id="+ident+format)
        webdriver.find_element_by_css_selector("#addToBasket_"+ident+"_"+btn_id).click()
        time.sleep(4)

    @staticmethod
    def placeOrder(webdriver, service):
        webdriver.get("https://"+service+".pl/zakupy/edit.cgi")
        webdriver.execute_script("jQuery(\"#zamowienie .button button\").click()")
        time.sleep(4)