from tkinter import *

root = Tk()


class app():
    def __init__(self) :
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.criando_botoes()
        self.label_entries()
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
        self.bt_limpar = Button(self.frame_1, text = 'Limpar')
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        ## criação dos botao buscar
        self.bt_busca = Button(self.frame_1, text = 'Buscar')
        self.bt_busca.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
         ## criação dos botao novo
        self.bt_novo = Button(self.frame_1, text = 'novo')
        self.bt_novo.place(relx=0.5, rely=0.1, relwidth=0.1, relheight=0.15)
         ## criação dos botao alterar
        self.bt_alterar = Button(self.frame_1, text = 'alterar')
        self.bt_alterar.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
         ## criação dos botao apagar
        self.bt_apagar = Button(self.frame_1, text = 'apagar')
        self.bt_apagar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

    def label_entries(self):
        ## criação label e entrada código
        self.lb_codigo = Label(self.frame_1, text='Código')
        self.lb_codigo.place(relx=0.05, rely=0.05, relwidth=0.08)#, relwidth=0.1, relheight=0.15)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.16, relwidth=0.08)

        ## criação label título
        self.lb_tit = Label(self.frame_1, text='Título')
        self.lb_tit.place(relx=0.05, rely=0.3, relwidth=0.08)
        
        self.tit_entry = Entry(self.frame_1)
        self.tit_entry.place(relx=0.15, rely=0.3, relwidth=0.48)

        ## criação label preco
        self.lb_preco = Label(self.frame_1, text='Preço')
        self.lb_preco.place(relx=0.65, rely=0.3, relwidth=0.06)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.73, rely=0.3, relwidth=0.1)

        ## criação label texto
        self.lb_texto = Label(self.frame_1, text='Texto')
        self.lb_texto.place(relx=0.05, rely=0.5, relwidth=0.06)

        self.texto_entry = Text(self.frame_1,height=2, width=50) 
        self.texto_entry.place(relx=0.15, rely=0.5, relwidth=0.7)

    def combobox(self):
        pass
     


app()

