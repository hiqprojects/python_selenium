"""this file contains fixtures for the test suite
(fixtures are python's way of depency injections)"""

import json
import pytest
from selenium import webdriver 

@pytest.fixture
def config(scope = "session"):
    """reads config file and converts json to py-dictionary. 
    scope = session to read file only once per run and provide settings for every instance and test case"""

    #read config
    with open('config.json') as config_file:
        setting = json.load(config_file)

    #plauability check of values
    assert setting['browser'] in ['Firefox', 'Chrome'] #contains valid browser?

    #return config 
    return setting 


@pytest.fixture
def browser(config):
    """function sets up browser, returns object (yield), cleans up after testcase function did its job
    imports configuration via config function."""
    if config["browser"] == "Firefox":
        try:
            driver = webdriver.Firefox()
        except:
            try:
                headOption = webdriver.FirefoxOptions()
                headOption.add_argument('--headless')
                headOption.add_argument('--window-size=1920,1080')
                driver = webdriver.Firefox(options = headOption)
            except:
                raise Exception('FAILURE: Firefox or WebDriver does not work.')    
    elif config["browser"] == "Chrome":
        try:
            driver = webdriver.Chrome()
        except:
            try:
                headOption = webdriver.ChromeOptions()
                headOption.add_argument('--headless')
                headOption.add_argument('--window-size=1920,1080')
                driver = webdriver.Chrome(options = headOption)
            except:
                raise Exception('FAILURE: Chrome or WebDriver does not work.')  
    else:
        raise Exception(f'Browser "{config["browser"]}" wird nicht unterstützt.')

    yield driver
    
    driver.quit()