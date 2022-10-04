from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support \
    import expected_conditions as EC
from time import sleep
import pandas as pd


class CautareFacebook:

    def __init__(self):
        self.search_global = None
        self.user = None
        self.password = None
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get(f'https://www.facebook.com/policies/cookies/')
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="u_0_3_qH"]'))).click()

    def login_linkedin(self, user, password):
        self.user = user
        self.password = password
        self.browser.find_element(by=By.XPATH, value='//*[@id="email"]').send_keys(self.user)
        self.browser.find_element(by=By.XPATH, value='//*[@id="pass"]').send_keys(self.password)
        self.browser.find_element(by=By.CLASS_NAME, value='//*[@id="u_0_9_Gx"]').submit()


var = CautareFacebook()
print(var)
