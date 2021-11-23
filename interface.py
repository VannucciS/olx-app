from tkinter import *
from tkinter import ttk

def enviar():
    pass

def gravar():
    pass


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
t['state'] = 'disabled'
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

# categoria deve ser um dropdown box
ttk.Label(mainframe, text = "Selecione uma categoria").grid(column=1, row=7, sticky=W)
categoryvar = StringVar()
category = ttk.Combobox(mainframe, textvariable=categoryvar)
category.bind('<<ComboboxSelected>>', gravar)
category['values'] = ('Imóveis', 'Autos e peças', 'Para a sua casa', 'Eletrônicos e celulares', 'Música e hobbies', 'Esporte e lazer', 'Artigos infantis', 'Animais de estimação',
                        'Moda e beleza')
category.state(['readonly'])
category.grid(column=1, row=8, sticky=W)

# Subcategoria deve ser um dropdow box
ttk.Label(mainframe, text = "Selecione uma sub-categoria").grid(column=2, row=7, sticky=W)
sub_categoryvar = StringVar()
sub_category = ttk.Combobox(mainframe, textvariable=sub_categoryvar)
sub_category.bind('<<ComboboxSelected>>', gravar)
sub_category['values'] = ('Imóveis', 'Autos e peças', 'Para a sua casa', 'Eletrônicos e celulares', 'Música e hobbies', 'Esporte e lazer', 'Artigos infantis', 'Animais de estimação',
                        'Moda e beleza')
sub_category.state(['readonly'])
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

def foto(num):
    # https://stackoverflow.com/questions/22802989/displaying-the-selected-image-using-tkinter
    filename = filedialog.askopenfilename()
    im = Image.open(filename)
    tkimage = ImageTk.PhotoImage(im)
    myvar = Label(mainframe, image= tkimage)
    myvar.image = tkimage
    myvar.grid(column=num, row=10, sticky=w)
    


#image1 = PhotoImage(file=)
ttk.Label(mainframe, text = "Selecione a(s) foto(s)").grid(column=1, row=9, sticky=W)
ttk.Button(mainframe, text = "Selecionar foto", command= foto(1)).grid(column=2, row=13, sticky=E)

ttk.Button(mainframe, text = "Gravar", command= gravar).grid(column=3, row=14, sticky=E)

from tkinter import messagebox

#messagebox.showinfo(message = "Anúncio gravado!")



for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)



title_entry.focus()
root.bind("<Return>", gravar)






root.mainloop()