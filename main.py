''' App para facilitar a publicação de anúncios no site olx
com ele será possível a republicação das fotos, mudança dos valores anunciados e histórico dos anúncios
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common import By
from  time import sleep as sleep

from selenium.webdriver.firefox.webdriver import WebDriver
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
    Nesta função será possível inserir as imagens no anúncio.
    '''
    # teste de commit
    ad_foto = browser.find_element_by_xpath('//*[@id="group-image-container"]/div[2]/div[2]/span[1]')

    pass


def texto():
    '''
    Nesta função será armazenada as informações do anúncio como título, descrição, categoria, tipo, novo/usado, preço
    '''
    # Criar uma dbase em sql armazenar texto e fotos
    
    titulo = str(input('Digite o título do seu anúncio: '))
    descricao = str(input('Digite a descrição do anúncio: '))
    
    cat= ''# informe a categoria
    sub_cat = ''
    preco = int(input('Digite o valor do que vai ser vendido: '))
    


def anuncio():
    '''
    Função insere o anúncio no formulário
    '''    
    cat = 'Música e hobbies'
    sub_cat = 'Livros e revistas'
    tit = 'teste'
    prec = '1'
    anuncio = 'vendo barato para desapegar'


    categoria = ['Música e hobbies', 'Eletrônicos e celulares']
    sub_categoria = ['Livros e revistas', 'Cds e dvds']
    url = 'https://www2.olx.com.br/ai/form/0/'
    titulo = browser.find_element_by_xpath('//*[@id="input_subject"]')
    descricao = browser.find_element_by_xpath('//*[@id="input_body"]')
    preco = browser.find_element_by_xpath('//*[@id="price"]')
    enviar_anuncio = browser.find_element_by_xpath('//*[@id="ad_insertion_submit_button"]')
    if browser.current_url == url:
        
        if cat in categoria:
            cat_musica_hobbies = browser.find_element_by_xpath('//*[@id="category_item-11000"]')
            
        if sub_cat in sub_categoria:
            sub_cat_livros = browser.find_element_by_xpath('//*[@id="category_item-11060"]')

        titulo.send_keys(tit)
        descricao.send_keys(anuncio)
        preco.send_keys(prec)
        enviar_anuncio.click()



def login():
    '''
    Função que faz o login no site
    '''
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

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
    if browser.find_element_by_xpath('//*[@id="__next"]/div/div/div[1]/div/div[1]/span'):
        browser.find_element_by_xpath('//*[@id="__next"]/div/div/div[1]/div/div[2]/form/button').click()
        WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.xpath,'//*[@id="__next"]/div/div/div[1]/div/div[2]/form/div[2]/button'))
            )
        browser.find_element_by_xpath('//*[@id="__next"]/div/div/div[1]/div/div[1]/span').click()



    


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

''''
Passos registra anúncio básico
1 - login
2 - inserir texto 
3 - escolher categoria
4 - preço
5 - fotos
6 - submeter
'''
login()
sleep(20)
anuncio()
sleep(20)
sleep(20)
sleep(20)



print('saindo')
browser.quit()