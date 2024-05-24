"""Page-Object for SuiteCRM Login Page. 
Contains Methods for laoding page and interaction"""

#from selenium.webdriver.common.keys import Keys #keyinput option for textfields
from selenium.webdriver.common.by import By #class for locating html objects
from selenium.webdriver.support import expected_conditions as ec #conditions for waiting, i.e. element_to_be_clickable oder title_is, tiltle_contains
from selenium.webdriver.support.ui import WebDriverWait #waiter for site or content to be loaded and option for timeout
import json

class SuiteCRMLogin:
    """Methoden für die Interaktion mit der Login-Seite"""
    #initialize instance of browser
    #variable from config.json
    def __init__(self, browser, config):
        self.browser = browser
        self.URL = config['url']
        self.USER = (By.ID, 'user_name')
        self.PW = (By.ID, 'username_password')
        self.SUBMIT = (By.ID, 'bigbutton')
        self.TITLE = config['title']
        self.TEXT_LOGINERROR = config['text_loginerror']
        self.TARGET_LOGINERROR = (By.CLASS_NAME, config['target_loginerror'])

    #methods section
    def loadSite(self):
        self.browser.get(self.URL)

    def checkSite(self, error_msg = 'FAILURE STATUS: Login could not be loaded.'):
        try:
            WebDriverWait(self.browser, 10).until(ec.title_is(self.TITLE))
        except:
            self.browser.save_screenshot('./output/error_LoginNotReady.png')
            raise Exception(error_msg)

    def inputUser(self, text):
        self.browser.find_element(*self.USER).send_keys(text)

    def inputPW(self, text):
        self.browser.find_element(*self.PW).send_keys(text)

    def submitPage(self):
        self.browser.find_element(*self.SUBMIT).click()



        