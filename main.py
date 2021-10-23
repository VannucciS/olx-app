''' App para facilitar a publicação de anúncios no site olx
com ele será possível a republicação das fotos, mudança dos valores anunciados e histórico dos anúncios
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common import By
from  time import sleep as sleep
import password


url = 'https://www2.olx.com.br/desapega'

#options = Options()
#options.headless = True
#options.add_argument("--window-size=1920,1200")

PATH = 'C:\webdriver\chromedriver.exe'
browser = webdriver.Chrome(executable_path = PATH) # (options=options, executable_path=DRIVER_PATH)
browser.get(url)


def foto():
    ''' 
    Nesta função será possível salvar as imagens dos anúncios, vinculando aos dados textuais do anúncio.
    '''
    # teste de commit
    pass


def texto():
    '''
    Nesta função será armazenada as informações do anúncio como título, descrição, categoria, tipo, novo/usado, preço
    '''
    pass


def anuncio():
    '''
    Função que acessa o site e insere o anúncio
    '''
    pass


def login():
    '''
    Função que faz o login no site
    '''
    email = browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[1]/div[2]/form/div[1]/div[2]/input')
    password = browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[1]/div[2]/form/div[2]/div[2]/div/div/input')
    if email:
         email.send_keys('username')
    if password:
         password.send_keys('password')
    


def salva_registro():
    '''
    Função que salva o endereço do anúncio
    '''
    pass


def modifica():
    '''
    Função que altera o anúncio no site
    '''
    pass


def media_preco():
    '''
    Função que verifica os anúncios similares e retorna um preço médio
    '''

# https://www2.olx.com.br/ai/form/0/
login()

sleep(10)

browser.quit()