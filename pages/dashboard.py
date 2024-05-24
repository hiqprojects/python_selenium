"""Page-Object for SuiteCRM Dashboard Page. 
Contains Methods for laoding page and interaction"""

#from selenium.webdriver.common.keys import Keys #keyinput option for textfields
from selenium.webdriver.common.by import By #class for locating html objects
from selenium.webdriver.support import expected_conditions as ec #conditions for waiting, i.e. element_to_be_clickable oder title_is, tiltle_contains
from selenium.webdriver.support.ui import WebDriverWait

from tests.conftest import browser #waiter for site or content to be loaded and option for timeout


class SuiteCRMDash:
    """Methoden für die Interaktion mit der Dashboard-Seite"""
    #initialize instance of browser
    def __init__(self, browser, config):
        self.browser = browser
        
        #variable from config.json
        self.TARGET_LINK = (By.LINK_TEXT, config['target_link'])

    #methods section
    def checkSite(self, error_msg = 'FAILURE: Dashboard nicht geladen.'):
        """returns Exception, if one elememt of a list conatains a target-string"""
        #if not self.browser.find_elements(self.TARGET_LINK):
        #    raise Exception(error_msg)
        try:
            WebDriverWait(self.browser, 10).until(ec.presence_of_all_elements_located(self.TARGET_LINK))
        except:
            self.browser.save_screenshot('./output/error_DashboardNotReady.png')
            raise Exception(error_msg)

    #more elements for interaction with webpage...