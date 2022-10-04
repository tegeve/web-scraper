from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support \
    import expected_conditions as EC
from time import sleep



class CautareLinkedin:

    def __init__(self):
        self.get_detalii = None
        self.search_global = None
        self.user = None
        self.password = None
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
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#main > div > div > '
                                                                                           'div:nth-child(1) > '
                                                                                           'div.search'
                                                                                           '-results__cluster-bottom'
                                                                                           '-banner.artdeco-button'
                                                                                           '.artdeco-button--tertiary'
                                                                                           '.artdeco-button--muted > '
                                                                                           'a'))).click()



    def search_jobs(self):
        self.browser.find_element(by=By.XPATH, value='//*[@id="global-nav"]/div/nav/ul/li[3]/a').\
            send_keys(Keys.ENTER)





var = CautareLinkedin()
var.login_linkedin('terecgeluvlad@yahoo.com', 'franky1#')
var.global_search("cluj")
print(var)
