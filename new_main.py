from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common import By
from  time import sleep as sleep

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
import password
import sqlite3

class Send_ad():
    def __init__(self):
        self.webdriver()
        self.login()

    def webdriver(self):
        self.url = 'https://www2.olx.com.br/desapega'

        self.options = Options()
        #options.headless = True
        self.options.add_argument("user-data-dir=C:\\webdriver\\selenium")

        PATH = 'C:\webdriver\chromedriver.exe'
        self.browser = webdriver.Chrome (options=self.options, executable_path=PATH) # (executable_path = PATH)
        self.browser.get(self.url)
        self.browser.maximize_window()
        self.palavra = password.username
        self.senha = password.password

    def login(self):
        '''Função que faz o login no site'''
        print('Login started')
        self.sleep(5)
        self.url2 = 'https://www2.olx.com.br/ai/form/0/'

        if not self.url:
            from selenium.webdriver.common.by import By
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC

            self.email = self.browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[1]/div[2]/form/div[1]/div[2]/input')
            self.password = self.browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[1]/div[2]/form/div[2]/div[2]/div/div/input')
            self.submit = self.browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[1]/div[2]/form/button')                 
            
            if self.email:
                self.email.send_keys(self.palavra)
                print('usuario')
            if self.password:
                self.password.send_keys(self.senha)
                print('senha')
                sleep(3)
                self.submit.click()
                print('click')
                    # https://selenium-python.readthedocs.io/waits.html
            if self.browser.find_element_by_xpath('//*[@id="__next"]/div/div/div[1]/div/div[1]/span'):
                self.browser.find_element_by_xpath('//*[@id="__next"]/div/div/div[1]/div/div[2]/form/button').click()
                WebDriverWait(self.browser, 30).until(
                EC.presence_of_element_located((By.xpath,'//*[@id="__next"]/div/div/div[1]/div/div[2]/form/div[2]/button'))
                )
                self.browser.find_element_by_xpath('//*[@id="__next"]/div/div/div[1]/div/div[1]/span').click()
        print('Login ended')


Send_ad()