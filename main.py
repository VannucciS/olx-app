''' App para facilitar a publicação de anúncios no site olx
com ele será possível a republicação das fotos, mudança dos valores anunciados e histórico dos anúncios
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common import By
from  time import sleep as sleep

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
import password
import sqlite3


url = 'https://www2.olx.com.br/desapega'

options = Options()
#options.headless = True
options.add_argument("user-data-dir=C:\\webdriver\\selenium")

PATH = 'C:\webdriver\chromedriver.exe'
browser = webdriver.Chrome (options=options, executable_path=PATH) # (executable_path = PATH)
browser.get(url)
browser.maximize_window()
palavra = password.username
senha = password.password

def foto(image):
    ''' 
    Nesta função será possível inserir as imagens no anúncio.
    '''
    import pyautogui
    browser.find_element_by_xpath('//*[@id="group-image-container"]/div[2]/div[2]/span[2]').click()
    sleep(6)
    pyautogui.write(image, interval = 1)
    pyautogui.press('return')
    print('Foto enviada')
    sleep(20)
    


def texto():
    '''
    Nesta função será armazenada as informações do anúncio como título, descrição, categoria, tipo, novo/usado, preço
    '''
    # Criar uma dbase em sql armazenar texto e fotos
    
    entry_title = str(input('Digite o título do seu anúncio: '))
    entry_decription = str(input('Digite a descrição do anúncio: '))
    
    cat= ''# informe a categoria
    sub_cat = ''
    preco = int(input('Digite o valor do que vai ser vendido: '))
    


def anuncio():
    '''
    Função insere o anúncio no formulário
    '''    
    print('Anuncio started')
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
    enviar_anuncio = browser.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/button') #//*[@id="ad_insertion_submit_button"]

    if browser.current_url == url:
        titulo.send_keys(tit)
        sleep(3)
        print('titulo')

        descricao.send_keys(anuncio)
        sleep(3)
        print('descricao')
        
        if cat in categoria:
            cat_musica_hobbies = browser.find_element_by_xpath('//*[@id="category_item-11000"]')
            cat_musica_hobbies.click()
            sleep(3)
            
        if sub_cat in sub_categoria:
            sub_cat_livros = browser.find_element_by_xpath('//*[@id="category_item-11060"]')
            sub_cat_livros.click()
            sleep(3)
        
        
        
        preco = browser.find_element_by_xpath('//*[@id="price"]') 
        sleep(3)        
        preco.send_keys(prec)
        print('preco')
        sleep(3)
        browser.find_element_by_xpath('//*[@id="cookie-notice-ok-button"]').click() # Aceito cookies
        foto(r'C:\Users\homel\Olx-app\olx-app\foto.JPG')
        print('foto enviada')
        '''
        enviar_anuncio.click()
        sleep(20)
        print('sem destaque')
        browser.find_element_by_xpath('//*[@id="root"]/section/div/a').click() # Nao aceito pagar pelo anuncio
        '''
    print('Anuncio ended')


def login():
    '''
    Função que faz o login no site
    '''
    print('Login started')
    sleep(5)
    url = 'https://www2.olx.com.br/ai/form/0/'

    if not url:   
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
                # https://selenium-python.readthedocs.io/waits.html
        if browser.find_element_by_xpath('//*[@id="__next"]/div/div/div[1]/div/div[1]/span'):
            browser.find_element_by_xpath('//*[@id="__next"]/div/div/div[1]/div/div[2]/form/button').click()
            WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.xpath,'//*[@id="__next"]/div/div/div[1]/div/div[2]/form/div[2]/button'))
            )
            browser.find_element_by_xpath('//*[@id="__next"]/div/div/div[1]/div/div[1]/span').click()
    print('Login ended')


    


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
anuncio()

print('saindo')
browser.quit()