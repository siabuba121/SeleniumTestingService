from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import time

serwisy = ['videopoint','helion','editio','ebookpoint','onepress','sensus','septem','bezdroza',]

class Bookstore:
    logged = dict()
    
    #used for login to bookstore
    #@param webdriver webdriver object
    #@param service text/string  (bookstore name domain)
    #@param username text/string (login/username)
    #@param password text/string (password)
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


    #used for checking if position can be downloaded by logged in user
    #@param webdriver webdriver object
    #@param service text/string  (bookstore name domain)
    #@param title text/string (title of requested position)
    #@param format text/string ("mobi","epub","pdf", "mp3")
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

    ###
    #used to add giftcard code to basket
    #@param webdriver webdriver object
    #@param service text/string  (bookstore name domain)
    #@param bonid text/string (giftcard code)
    ###
    @staticmethod
    def tryToAddBonToBasket(webdriver,service,bonid):
        if Bookstore.logged[service] != 1:
            print("User nie jest zalogowany do serwisu "+service+"\n")
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
    
    ###
    #used for adding requested position to basket
    #@param webdriver webdriver object
    #@param service text/string  (bookstore name domain)
    #@param ident text/string (unique bookstore ident)
    #@param format test/string (selected format fot requested position) example: "ebook" OR "druk"
    ###
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

    ###
    #used for submiting shoping basket for next step of transaction
    #@param webdriver webdriver object
    #@param service text/string  (bookstore name domain)
    ###
    @staticmethod
    def placeOrder(webdriver, service):
        webdriver.get("https://"+service+".pl/zakupy/edit.cgi")
        webdriver.execute_script("jQuery(\"#zamowienie .button button\").click()")
        time.sleep(4)
    

    ###
    #used for checking if solr is responsing correctly
    #@param webdriver webdriver object
    #@param service text/string  (bookstore name domain)
    #@param searchPhrase text/string (text that will be send to search input)
    #@param(optional) callbackAction function (function that will be done after succesfully checking solr response)
    #@param(optional) callbackActionParam object (object/param that will be send to callback function)
    ###
    @staticmethod
    def searchForPositionMainPage(webdriver, service, searchPhrase, callbackAction="", callbackActionParam=""):
        webdriver.get("https://"+service+".pl")
        search = webdriver.find_element_by_css_selector("#inputSearch")
        search.send_keys(searchPhrase)
        time.sleep(2)
        if webdriver.find_element_by_css_selector(".suggest-list").is_displayed():
            webdriver.execute_script("alert(\"solr ok\")")
            if callbackAction:
                Alert(webdriver).accept()
                callbackAction(webdriver, callbackActionParam)
            return
        else:
            webdriver.execute_script("alert(\"solr not ok or cannot find phrase\")")       
            print("error or not find on service "+service+"\n")
            Alert(driver).accept()
            time.sleep(2)

    ###
    #used as collback in solr tersting it click's requested elem of solr response html representation or clicks button showall
    #@param webdriver webdriver object
    #@param which int (index of position in solr response seaech that will be clicked if not specified it will click showall button)
    ###
    @staticmethod
    def clickFromSuggestions(webdriver, which):
        if which == "":
            webdriver.find_element_by_css_selector(".suggest-list .wszystkie .button a").click()
        elif which>0:
            suggestions = webdriver.find_elements_by_css_selector(".suggest-list .suggest-ksiazka")
            if len(suggestions) != 0:
                suggestions[which-1].click()
