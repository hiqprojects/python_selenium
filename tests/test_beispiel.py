"""Example Script. All Scripts in folder tests with filename containing test_*.py will be executed by pytest.
pytest will search in this files for functions declared as test_* and will do one testcase per each automatically.
Other functions will be ignored if not referenced in one of the test_* functions."""
from pages.dashboard import SuiteCRMDash
from pages.login import SuiteCRMLogin

def test_login(browser, config):
    #variable from config.json
    DATA_USER = config['user']
    DATA_PW = config['pw']

    #create page-objects for the browser and config arguments
    page_login = SuiteCRMLogin(browser, config)

    #teststeps
    page_login.loadSite()
    page_login.checkSite()
    page_login.inputUser(DATA_USER)
    page_login.inputPW(DATA_PW)
    page_login.submitPage()

    page_dash = SuiteCRMDash(browser, config)
    page_dash.checkSite()

#more tests...
