from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import sqlite3

root = Tk()
global foto
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
        fotos TEXT(200)
        );
    """)
        self.conn.commit(); print("BD criado")
        self.desconecta_bd()

    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.tit_entry.delete(0, END)
        self.preco_entry.delete(0, END)
        self.texto_entry.delete('1.0', 'end-1c')
        #self.e1.destroy('all')   
        for i in range(len(self.frame_1.winfo_children())):             
            if i> 17:
                print(self.frame_1.winfo_children()[i])
                self.frame_1.winfo_children()[i].destroy()

    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.titulo = self.tit_entry.get()
        self.anuncio = self.texto_entry.get('1.0', 'end-1c')
        self.preco = self.preco_entry.get()
        self.categoria = self.category_box.get()
        self.sub_categoria = self.sub_category_box.get()
        self.fotos = str(self.filename)
        print(self.fotos)

    def add_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(
            """
            INSERT INTO anuncios
            (
                titulo, preco, texto, categoria, sub_categoria, fotos
            )
            VALUES (?,?,?,?,?,?)
            """,
            (self.titulo,  self.preco, self.anuncio, self.categoria, self.sub_categoria, self.fotos)
        )
        self.conn.commit(), print("Gravado.")
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()

    def select_lista(self):
        self.listacli.delete(*self.listacli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(
            """
            SELECT cod,titulo, preco, texto, categoria, sub_categoria
            FROM anuncios
            ORDER BY titulo ASC    
            """
        )
        for i in lista:
            self.listacli.insert("", END, values=i)
        self.desconecta_bd()           
  
    def duplo_click(self, event):
        self.limpa_tela()
        self.listacli.selection()

        for n in self.listacli.selection():
            col1, col2,col3, col4, col5, col6 = self.listacli.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.tit_entry.insert(END, col2)
            self.preco_entry.insert(END, col3)
            self.texto_entry.insert(END, col4)
            self.category_box.insert(END, col5)
            self.sub_category_box.insert(END, col6)

    def deleta_anuncio(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(
            """
            DELETE FROM anuncios
            WHERE cod = ?            
            """,            
            (self.codigo)
        )
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_tela()
        self.select_lista()

    def altera_anuncio(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(
            """
            UPDATE anuncios
            SET titulo = ?, preco = ?, texto = ?, categoria = ?, sub_categoria = ?
            WHERE cod = ?
            """ ,  (self.titulo, self.preco, self.anuncio, self.categoria, self.sub_categoria, self.codigo)
        )
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()

    def foto(self, event, position):
        self.types = [('jpg files', '*.jpg'),('png files', '*.png')]        
        self.frame_1.filename = filedialog.askopenfilename(initialdir = "/", title = "Selecione a imagem", filetypes=(self.types), multiple = False)
        self.filename = self.frame_1.filename
        print(self.filename)
        self.event = Image.open(self.frame_1.filename).resize((50,50))
        #self.event = self.event.resize(100,50) 
        self.event = ImageTk.PhotoImage(self.event)        
        self.event  = Label(image=self.event).place(relx=position , rely=0.55, relwidth=0.06) # imagem_label 
        
    
    def fotos(self):
        # https://www.youtube.com/watch?v=ndUuy_55jho - open multiple images 
        self.types = [('jpg files', '*.jpg'),('png files', '*.png')]        
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Selecione até 5 imagens", filetypes=(self.types), multiple = True)
        #self.frame_1.filename = filedialog.askopenfilename(initialdir = "/", title = "Selecione a imagem", filetypes=(self.types), multiple = True)
        self.filename = self.filename
        #self.filename = self.frame_1.filename
        if len(self.filename) < 6:
            self.filename = self.filename
        else:
            self.filename =()
            print('Quantidade de fotos excedida.')
        position = 0.19
        for f in self.filename:
            # https://www.plus2net.com/python/tkinter-filedialog-upload-display.php
            print(f)
            self.foto = Image.open(f)
            self.foto = self.foto.resize((50,50))
            self.foto = ImageTk.PhotoImage(self.foto)   
            #self.foto = Label(self.frame_1, image=self.foto)
            self.e1 = Label(self.frame_1)
            self.e1.place(relx=position , rely=0.8, relwidth=0.06)
            self.e1.image = self.foto
            self.e1['image'] = self.foto
            #self.foto.place(relx=position , rely=0.8, relwidth=0.06)
            position = position + 0.1


class App(Functions):
    def __init__(self) :
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.criando_botoes()
        self.label_entries()
        self.combobox()
        self.tree_view()
        self.monta_tabelas()
        self.select_lista()
        self.menus()        
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
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.66)
        self.frame_2 = Frame(self.root, bd=4, bg='lightgray', highlightbackground='white', highlightthickness=2)
        self.frame_2.place(relx=0.02, rely=0.7, relwidth=0.96, relheight=0.26)

    def criando_botoes(self):
        ## criação dos botao limpar
        self.bt_limpar = Button(self.frame_1, text = 'Limpar', bd = 3, bg="#107db2", fg= 'white',font=('arial', 10, 'bold'), command=self.limpa_tela)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        ## criação dos botao buscar
        self.bt_busca = Button(self.frame_1, text = 'Buscar',  bd = 3, bg="#107db2", fg= 'white', font=('arial', 10, 'bold'))
        self.bt_busca.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
         ## criação dos botao novo
        self.bt_novo = Button(self.frame_1, text = 'Novo',  bd = 3, bg="#107db2", fg= 'white', font=('arial', 10, 'bold'), command=self.add_cliente)
        self.bt_novo.place(relx=0.5, rely=0.1, relwidth=0.1, relheight=0.15)
         ## criação dos botao alterar
        self.bt_alterar = Button(self.frame_1, text = 'Alterar',  bd = 3, bg="#107db2", fg= 'white', font=('arial', 10, 'bold'), command=self.altera_anuncio)
        self.bt_alterar.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
         ## criação dos botao apagar
        self.bt_apagar = Button(self.frame_1, text = 'Apagar',  bd = 3, bg="#107db2", fg= 'white', font=('arial', 10, 'bold'), command=self.deleta_anuncio)
        self.bt_apagar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        ## Criação dos botões de exibição, cópia de fotos
        self.fotos = Button(self.frame_1, text = 'Fotos', bd = 3, bg="#107db2", fg= 'white',font=('arial', 8, 'bold'), command=self.fotos)
        self.fotos.place(relx=0.05, rely=0.85, relwidth=0.06)#, relwidth=0.1, relheight=0.15)

        """self.foto2 = Button(self.frame_1, text = 'Foto2', bd = 3, bg="#107db2", fg= 'white',font=('arial', 8, 'bold'), command=lambda: self.foto(2, 0.5))
        self.foto2.place(relx=0.33, rely=0.85, relwidth=0.06)#, relwidth=0.1, relheight=0.15)

        self.foto3 = Button(self.frame_1, text = 'Foto3', bd = 3, bg="#107db2", fg= 'white',font=('arial', 8, 'bold'), command=self.fotos)
        self.foto3.place(relx=0.19, rely=0.85, relwidth=0.06)#, relwidth=0.1, relheight=0.15)

        self.foto4 = Button(self.frame_1, text = 'Foto4', bd = 3, bg="#107db2", fg= 'white',font=('arial', 8, 'bold'), command=self.fotos)
        self.foto4.place(relx=0.26, rely=0.85, relwidth=0.06)#, relwidth=0.1, relheight=0.15)

        self.foto4 = Button(self.frame_1, text = 'Foto5', bd = 3, bg="#107db2", fg= 'white',font=('arial', 8, 'bold'), command=self.fotos)
        self.foto4.place(relx=0.33, rely=0.85, relwidth=0.06)#, relwidth=0.1, relheight=0.15)"""

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
    
    def pick_category(self):
        pass

    def combobox(self):
        self.category = Label(self.frame_1, text="Categoria", bg='lightgray')
        self.category.place(relx=0.05, rely=0.7) 

        categories = ["Imóveis", "Música e hobbies", "Esporte e lazer"]

        self.category_box = ttk.Combobox(self.frame_1, value= categories) 
        self.category_box.place(relx=0.15, rely=0.7, relwidth=0.16)
        self.category_box.current(0)
        self.category_box.state(['readonly'])
        self.category_box.bind('<<ComboboxSelected>>', self.pick_category)


        self.sub_category = Label(self.frame_1, text="Sub-Categoria", bg='lightgray')
        self.sub_category.place(relx=0.34, rely=0.7) 

        sub_categories = ["Imóveis", "Música e hobbies", "Esporte e lazer"]

        self.sub_category_box = ttk.Combobox(self.frame_1, value= sub_categories) 
        self.sub_category_box.place(relx=0.47, rely=0.7, relwidth=0.16)
        self.sub_category_box.current(0)
        self.sub_category_box.state(['readonly'])
        self.sub_category_box.bind('<<ComboboxSelected>>', self.pick_category)
     
    def tree_view(self):
        self.listacli = ttk.Treeview(self.frame_2, height=3, columns=('col1', 'col2','col3', 'col4', 'col5', 'col6'), show='headings')

        # Nome de cada coluna
        self.listacli.heading("#0", text="zero")
        self.listacli.heading("#1", text="Código")
        self.listacli.heading("#2", text="Titulo")
        self.listacli.heading("#3", text="Preço")
        self.listacli.heading("#4", text="Texto")
        self.listacli.heading("#5", text="Categoria")
        self.listacli.heading("#6", text="Subcategoria")

        # Tamanho de cada coluna
        self.listacli.column('#0', width=25) # Faz com que a primeira coluna não apareça no treeview , stretch=NO
        self.listacli.column('#1', width=25)
        self.listacli.column('#2', width=100)
        self.listacli.column('#3', width=100)
        self.listacli.column('#4', width=100)
        self.listacli.column('#5', width=100)
        self.listacli.column('#6', width=50)

        # Posição do widget no frame
        self.listacli.place(relx=0.01, rely=0.01, relheight=0.85, relwidth=0.97)

        # Barra de rolagem lateral
        self.scrollbar = Scrollbar(self.frame_2, orient='vertical', command=self.listacli.yview)
        self.listacli.configure(yscroll=self.scrollbar.set)
        self.scrollbar.place(relx=0.98, rely=0.01, relwidth=0.04, relheight=0.85)
        self.listacli.bind("<Double-1>", self.duplo_click)

    def menus(self):
        menubar = Menu(self.root)
        self.root.config(menu = menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def quit(): self.root.destroy()

        menubar.add_cascade(label = 'Opções', menu = filemenu)
        menubar.add_cascade(label = 'Sobre', menu = filemenu2)

        filemenu.add_command(label='Sair', command=quit)
        filemenu.add_command(label='Limpa Cliente', command=self.limpa_tela)
        filemenu.add_command(label='Cadastrar usuário', command=self.limpa_tela)
        filemenu.add_command(label='Enviar anuncios para OLX', command=self.limpa_tela)
        filemenu2.add_command(label='Saiba mais', command=self.limpa_tela)
    
    
        





App()

