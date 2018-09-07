from selenium.webdriver.common.action_chains import ActionChains
import time

class Bookstore:
    logged = dict()
    
    @staticmethod
    def loginToBookstore(webdriver, service, username, password):
        webdriver.get("https://"+service+".pl/users/index2.cgi")
        login = webdriver.find_element_by_name("loginemail")
        login.send_keys(username)
        haslo = webdriver.find_element_by_name("haslo")
        haslo.send_keys(password)
        button = webdriver.find_element_by_css_selector(".form.form-left fieldset .buttons button")
        click_action = ActionChains(webdriver)
        click_action.click(button)
        click_action.perform()
        #should add some wait till user i logged
        time.sleep(3)
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