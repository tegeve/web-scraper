from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support \
    import expected_conditions as EC
from time import sleep
import pandas as pd


class CautareLinkedin:

    def __init__(self, cautare):
        self.search_global = None
        self.user = None
        self.password = None
        self.cautare = cautare
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get(f'https://ro.linkedin.com/')
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#artdeco-global-alert'
                                                                                           '-container > div > '
                                                                                           'section > div > '
                                                                                           'div.artdeco-global-alert'
                                                                                           '-action__wrapper > '
                                                                                           'button:nth-child('
                                                                                           '1)'))).click()

    def login_linkedin(self, user, password):
        self.user = user
        self.password = password
        self.browser.find_element(by=By.ID, value='session_key').send_keys(self.user)
        self.browser.find_element(by=By.ID, value='session_password').send_keys(self.password)
        self.browser.find_element(by=By.CLASS_NAME, value='sign-in-form__submit-button').submit()

    def global_search(self, search_global):
        self.search_global = search_global
        self.browser.find_element(by=By.XPATH, value='//*[@id="global-nav-typeahead"]/input').\
            send_keys(self.search_global)
        self.browser.find_element(by=By.XPATH, value='//*[@id="global-nav-typeahead"]/input').send_keys(Keys.ENTER)
        sleep(5)

    def filter_by_jobs(self):
        self.browser.find_element(by=By.XPATH, value='//*[@id="search-reusables__filters-bar"]/div/div/button').\
            send_keys(Keys.ENTER)
        sleep(5)
        self.browser.find_element(by=By.ID, value='//*[@id="ember2201"]').click()


var = CautareLinkedin("")
var.login_linkedin('terecgeluvlad@yahoo.com', 'franky1#')
var.global_search('cluj')
var.filter_by_jobs()
print(var)
