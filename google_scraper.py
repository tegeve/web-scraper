from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support \
    import expected_conditions as EC
from time import sleep
import pandas as pd


class CautareGoogle:

    def __init__(self, cautare):
        self.cautare = cautare
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get(f'https://www.google.com/maps/')
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#yDmH0d > c-wiz > div > '
                                                                                           'div > div > div.NIoIEf > '
                                                                                           'div.G4njw > div.AIC7ge > '
                                                                                           'div.CxJub > div.VtwTSb > '
                                                                                           'form:nth-child(2) > div > '
                                                                                           'div > button > '
                                                                                           'span'))).click()
        get_element = self.browser.find_element(by=By.ID, value='searchboxinput')
        get_element.send_keys(f'{self.cautare}')
        get_enter = self.browser.find_element(by=By.ID, value='searchbox-searchbutton')
        get_enter.click()
        sleep(5)
        self.get_detalii = ''
        self.rezultate = []
        self.current_url_list = []
        self.address_list = []
        self.review_list = []
        self.number_reviews_list = []
        self.telefon_list = []
        for i in range(3, 41, 2):
            link = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/div[2]'
            lista = list(link)
            lista[-13] = f'{i}'
            link = "".join(lista)
            self.get_detalii = self.browser.find_element(by=By.XPATH, value=link).text.split('\n')[0]
            link2 = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/a'
            lista2 = list(link2)
            lista2[-8] = f'{i}'
            link2 = "".join(lista2)
            link3 = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[' \
                    '2]/div[1]/div/div/div/div[4]/div[1]/span[2]/jsl/span[2] '
            lista = list(link3)
            lista[77] = f'{i}'
            link3 = "".join(lista)
            link4 = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[' \
                    '2]/div[1]/div/div/div/div[3]/div/span[2]/span[2]/span[1] '
            lista = list(link4)
            lista[77] = f'{i}'
            link4 = "".join(lista)
            link5 = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[' \
                    '2]/div[1]/div/div/div/div[3]/div/span[2]/span[2]/span[2] '
            lista = list(link5)
            lista[77] = f'{i}'
            link5 = "".join(lista)
            self.locatie = self.browser.find_element(by=By.XPATH, value=link2).click()
            self.address = str(self.browser.find_element(by=By.XPATH, value=link3).text)
            self.review = str(self.browser.find_element(by=By.XPATH, value=link4).text)
            self.number_review = str(self.browser.find_element(by=By.XPATH, value=link5).text)
            self.detalii = str(self.get_detalii)
            self.rezultate.append(self.detalii)
            self.address_list.append(self.address)
            self.review_list.append(self.review)
            self.number_reviews_list.append(self.number_review)
            self.current_url_list.append(self.browser.current_url)
            elem = self.browser.find_element(by=By.XPATH, value='//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div['
                                                                '1]/div/div/div[2]/div[1]')
            for _ in range(2):
                elem.send_keys(Keys.END)
                sleep(2)

    def get_location(self):
        return self.locatie

    def get_location_list(self):
        return self.get_location_list

    def get_address(self):
        return self.address

    def get_address_list(self):
        return self.address_list

    def get_review(self):
        return self.get_review

    def get_current_url_list(self):
        return self.current_url_list

    def __str__(self):
        dictionar = {'locatie': self.rezultate, 'url': self.current_url_list, 'adresa': self.address_list,
                     'nota review': self.review_list, 'number reviews': self.number_reviews_list}
        self.df = pd.DataFrame(dictionar, columns=('locatie', 'url', 'adresa', 'nota review', 'number reviews'))
        pd.set_option('display.max_columns', None)
        pd.set_option('display.expand_frame_repr', False)
        pd.set_option('max_colwidth', None)
        return f'{self.df}'




var = CautareGoogle("restaurante Cluj-Napoca")
print(var)
