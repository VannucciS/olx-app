from tkinter import Frame, Tk


root = Tk()


class app():
    def __init__(self) :
        self.root = root
        self.tela()
        self.frames_da_tela()
        root.mainloop()
    
    def tela(self):
        self.root.title("Gerenciamento de anúncios OLX")
        self.root.configure(background = "gray")
        self.root.geometry("780x500")
        self.root.resizable(True, True)
        self.root.maxsize(width = 900, height = 700)
        self.root.minsize(width = 480, height = 300)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg='lightgray', highlightbackground='white', highlightthickness=2)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame_2 = Frame(self.root, bd=4, bg='lime', highlightbackground='white', highlightthickness=2)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)


app()

