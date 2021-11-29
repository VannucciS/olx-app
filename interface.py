#from sqlite3.dbapi2 import Cursor
from tkinter import *
from tkinter import ttk
import sqlite3

con = sqlite3.connect("anuncios.bd")
cursor = con.cursor()

def desconecta_db():
    con.close()

def monta_tabelas():
    print('Conectando ao banco de dados')
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS anuncios
    (
        cod INTEGER PRIMARY KEY, 
        titulo CHAR(40) NOT NULL, 
        texto CHAR(200), 
        preco INTEGER(8),
        categoria CHAR(30),
        sub_categoria CHAR(30),
        foto1 CHAR(200),
        foto2 CHAR(200),
        foto3 CHAR(200),
        foto4 CHAR(200),
        foto5 CHAR(200)
        );
    """)
    con.commit(); print("BD criado")
    desconecta_db()


monta_tabelas()
desconecta_db()

def enviar():        
    pass

def editar():
    pass

def excluir():
    pass

def gravar():
    con = sqlite3.connect("anuncios.bd")
    cursor = con.cursor()
    print("Gravando na base de dados...")
    titulo = title_entry.get()
    anuncio = t.get('1.0', 'end-1c')
    preco = preco_entry.get()
    categoria = category.get()
    sb_categoria = sub_category.get()

    cursor.execute(
        """
        INSERT INTO anuncios
        (
            titulo, texto, preco, categoria, sub_categoria
        )
        VALUES (?,?,?,?,?)
        """,
        (titulo, anuncio, preco, categoria, sb_categoria)
    )
    con.commit(), print("Gravado.")
    desconecta_db()


root = Tk()
root.title('OLX APP')
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight= 1)

ttk.Label(mainframe, text = "Título do anúncio").grid(column=1, row=1, sticky=W)
title = StringVar()
title_entry = ttk.Entry(mainframe, width=30, textvariable=title)
title_entry.grid(column=1, row=2, sticky=(W, E))

ttk.Label(mainframe, text = "Descrição do anúncio").grid(column=1, row=3, sticky=W)
t = Text(mainframe, width=40, height=10)
t.grid(column=1, row=4, sticky=(W, E))
contents = t.get('1.0', 'end')



#texto = StringVar()
#texto_entry = Tk.Text(mainframe, width=80, textvariable=texto)
#texto_entry.grid(column=1, row=4, sticky=(W, E))


ttk.Label(mainframe, text = "Preço do produto").grid(column=1, row=5, sticky=W)
preco = IntVar()
preco_entry = ttk.Entry(mainframe, width=5, textvariable=preco)
#ttk.Label(mainframe, text = "R$").grid(column=1, row=6, sticky=W)
preco_entry.grid(column=1, row=6, sticky=(W,E))

# https://www.youtube.com/watch?v=bH9r3wM9Idw
# Dependend drop down menu

categories = [
    "Imóveis", 
    "Música e hobbies", 
    "Esporte e lazer"
]

cat_imoveis = [
    'Apartamentos', 
    'Casas', 
    'Aluguel de quartos', 
    'Temporada', 
    'Terrenos, sítios e fazendas',
    'Comércio e indústria'
]

cat_esporte = [
    'Esportes e ginástica',
    'Ciclismo'
    ]
cat_hobbie = [
    'Instrumentos musicais',
    'CDs, DVDs etc',
    'Livros e revistas',
    'Antiguidades',
    'Hobbies e coleções'
]
def pick_category(e):
    if category.get() == 'Imóveis':
        sub_category.config(value = cat_imoveis)
        sub_category.current(0)
    if category.get() == "Música e hobbies":
        sub_category.config(value = cat_hobbie)
        sub_category.current(0)
    if category.get() == "Esporte e lazer":
        sub_category.config(value = cat_esporte)
        sub_category.current(0)


ttk.Label(mainframe, text = "Selecione uma categoria").grid(column=1, row=7, sticky=W)
category = ttk.Combobox(mainframe, value= categories) 
category.current(0)
category.state(['readonly'])
category.grid(column=1, row=8, sticky=W)
category.bind('<<ComboboxSelected>>', pick_category)



# Subcategoria deve ser um dropdow box
ttk.Label(mainframe, text = "Selecione uma sub-categoria").grid(column=2, row=7, sticky=W)
sub_category = ttk.Combobox(mainframe, value = [" "] )
sub_category.current(0)
sub_category.bind('<<ComboboxSelected>>', pick_category)
sub_category.grid(column=2, row=8, sticky=W)
'''
entry_decription = str(input('Digite a descrição do anúncio: '))
cat= ''# informe a categoria
sub_cat = ''
preco = int(input('Digite o valor do que vai ser vendido: '))
'''
####Image#####
from tkinter import filedialog
from PIL import Image, ImageTk

def foto():
    # https://stackoverflow.com/questions/22802989/displaying-the-selected-image-using-tkinter
    # https://stackoverflow.com/questions/56374895/open-a-image-file-then-display-it-in-new-window
    filename = filedialog.askopenfilename()
    im = Image.open(filename)
    im = im.resize((100,100), Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(im)
    myvar = Label(mainframe, image= tkimage)
    myvar.image = tkimage
    myvar.grid(column=1, row=10, sticky=W)
    
'''
FALTA FAZER:
* SALVAR MULTIPLAS FOTOS
* SALVAR O ANUNCIO EM UM BASE DE DADOS
* SALVAR AS FOTOS EM UM DIRETÓRIO ESPECÍFICO
* LIMPAR O FORMULARIO AO CLICAR EM SALVAR

'''


#image1 = PhotoImage(file=)
ttk.Label(mainframe, text = "Selecione a(s) foto(s)").grid(column=1, row=9, sticky=W)
ttk.Button(mainframe, text = "Selecionar foto", command= foto).grid(column=2, row=13, sticky=E)

ttk.Button(mainframe, text = "Gravar", command= gravar).grid(column=3, row=14, sticky=E)

from tkinter import messagebox

#messagebox.showinfo(message = "Anúncio gravado!")



for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)



title_entry.focus()
root.bind("<Return>", gravar)






root.mainloop()