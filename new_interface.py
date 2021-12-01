from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()

class Functions():
    def conecta_bd(self):
        self.conn = sqlite3.connect("anuncios.bd")
        self.cursor = self.conn.cursor()   
        print('Conectando ao banco de dados')

    def desconecta_bd(self):
        self.conn.close(); print('Conexão com o BD perdida...')

    def monta_tabelas(self):
        self.conecta_bd()
        self.cursor.execute("""
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
        self.conn.commit(); print("BD criado")
        self.desconecta_bd()

    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.tit_entry.delete(0, END)
        self.preco_entry.delete(0, END)
        self.texto_entry.delete('1.0', 'end-1c')        
    def buscar(self):
        pass
    def novo(self):
        pass
    def alterar(self):
        pass
    def apagar(self):
        pass

class App(Functions):
    def __init__(self) :
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.criando_botoes()
        self.label_entries()
        self.tree_view()
        self.monta_tabelas()
        root.mainloop()
    
    def tela(self):
        self.root.title("Gerenciamento de anúncios OLX")
        self.root.configure(background = "gray")
        self.root.geometry("780x500")
        self.root.resizable(True, True)
        self.root.maxsize(width = 900, height = 700)
        self.root.minsize(width = 500, height = 400)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg='lightgray', highlightbackground='white', highlightthickness=2)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame_2 = Frame(self.root, bd=4, bg='lightgray', highlightbackground='white', highlightthickness=2)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def criando_botoes(self):
        ## criação dos botao limpar
        self.bt_limpar = Button(self.frame_1, text = 'Limpar', bd = 3, bg="#107db2", fg= 'white',font=('arial', 10, 'bold'), command=self.limpa_tela)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        ## criação dos botao buscar
        self.bt_busca = Button(self.frame_1, text = 'Buscar',  bd = 3, bg="#107db2", fg= 'white', font=('arial', 10, 'bold'))
        self.bt_busca.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
         ## criação dos botao novo
        self.bt_novo = Button(self.frame_1, text = 'Novo',  bd = 3, bg="#107db2", fg= 'white', font=('arial', 10, 'bold'))
        self.bt_novo.place(relx=0.5, rely=0.1, relwidth=0.1, relheight=0.15)
         ## criação dos botao alterar
        self.bt_alterar = Button(self.frame_1, text = 'Alterar',  bd = 3, bg="#107db2", fg= 'white', font=('arial', 10, 'bold'))
        self.bt_alterar.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
         ## criação dos botao apagar
        self.bt_apagar = Button(self.frame_1, text = 'Apagar',  bd = 3, bg="#107db2", fg= 'white', font=('arial', 10, 'bold'))
        self.bt_apagar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

    def label_entries(self):
        ## criação label e entrada código
        self.codigo = Label(self.frame_1, text='Código', bg='lightgray')
        self.codigo.place(relx=0.05, rely=0.05, relwidth=0.08)#, relwidth=0.1, relheight=0.15)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.16, relwidth=0.08)

        ## criação label título
        self.tit = Label(self.frame_1, text='Título', bg='lightgray')
        self.tit.place(relx=0.05, rely=0.3, relwidth=0.08)
        
        self.tit_entry = Entry(self.frame_1)
        self.tit_entry.place(relx=0.15, rely=0.3, relwidth=0.48)

        ## criação label preco
        self.preco = Label(self.frame_1, text='Preço', bg='lightgray')
        self.preco.place(relx=0.65, rely=0.3, relwidth=0.06)

        self.preco_entry = Entry(self.frame_1)
        self.preco_entry.place(relx=0.73, rely=0.3, relwidth=0.1)

        ## criação label texto
        self.texto = Label(self.frame_1, text='Texto', bg='lightgray')
        self.texto.place(relx=0.05, rely=0.5, relwidth=0.06)

        self.texto_entry = Text(self.frame_1,height=2, width=50) 
        self.texto_entry.place(relx=0.15, rely=0.5, relwidth=0.7)

    def combobox(self):
        pass
     
    def tree_view(self):
        self.listacli = ttk.Treeview(self.frame_2, height=3, columns=('col1', 'col2','col3', 'col4'), show='headings')

        # Nome de cada coluna
        self.listacli.heading("#0", text="")
        self.listacli.heading("#1", text="Código")
        self.listacli.heading("#2", text="Titulo")
        self.listacli.heading("#3", text="Preço")
        self.listacli.heading("#4", text="Texto")

        # Tamanho de cada coluna
        self.listacli.column('#0', width=1) # Faz com que a primeira coluna não apareça no treeview , stretch=NO
        self.listacli.column('#1', width=50)
        self.listacli.column('#2', width=200)
        self.listacli.column('#3', width=125)
        self.listacli.column('#4', width=125)

        # Posição do widget no frame
        self.listacli.place(relx=0.01, rely=0.01, relheight=0.85, relwidth=0.97)

        # Barra de rolagem lateral
        self.scrollbar = Scrollbar(self.frame_2, orient='vertical', command=self.listacli.yview)
        self.listacli.configure(yscroll=self.scrollbar.set)
        self.scrollbar.place(relx=0.98, rely=0.01, relwidth=0.04, relheight=0.85)

App()

