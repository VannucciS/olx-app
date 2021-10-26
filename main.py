''' App para facilitar a publicação de anúncios no site olx
com ele será possível a republicação das fotos, mudança dos valores anunciados e histórico dos anúncios
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common import By
from  time import sleep as sleep
import password
import sqlite3


url = 'https://www2.olx.com.br/desapega'

#options = Options()
#options.headless = True
#options.add_argument("--window-size=1920,1200")

PATH = 'C:\webdriver\chromedriver.exe'
browser = webdriver.Chrome(executable_path = PATH) # (options=options, executable_path=DRIVER_PATH)
browser.get(url)

palavra = password.username
senha = password.password

def foto():
    ''' 
    Nesta função será possível salvar as imagens dos anúncios, vinculando aos dados textuais do anúncio.
    '''
    # teste de commit
    ad_foto = browser.find_element_by_xpath('//*[@id="group-image-container"]/div[2]/div[2]/span[1]')

    pass


def texto():
    '''
    Nesta função será armazenada as informações do anúncio como título, descrição, categoria, tipo, novo/usado, preço
    '''
    titulo = str(input('Digite o título do seu anúncio: '))
    descricao = str(input('Digite a descrição do anúncio: '))
    categoria = # informe a categoria
    preco = int(input('Digite o valor do que vai ser vendido: ')
    pass


def anuncio():
    '''
    Função insere o anúncio no formulário
    '''
    url = 'https://www2.olx.com.br/ai/form/0/'
    titulo = browser.find_element_by_xpath('//*[@id="input_subject"]')
    descricao = browser.find_element_by_xpath('//*[@id="input_body"]')
    preco = browser.find_element_by_xpath('//*[@id="price"]')
    enviar_anuncio = browser.find_element_by_xpath('//*[@id="ad_insertion_submit_button"]')



    pass


def login():
    '''
    Função que faz o login no site
    '''
    email = browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[1]/div[2]/form/div[1]/div[2]/input')
    password = browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[1]/div[2]/form/div[2]/div[2]/div/div/input')
    submit = browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[1]/div[2]/form/button')   
    
    if email:
         email.send_keys(palavra)
         print('usuario')
    if password:
         password.send_keys(senha)
         print('senha')
         sleep(3)
         submit.click()
         print('click')
    

    


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

sleep(20)
print('saindo')
browser.quit()