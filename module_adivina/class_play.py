from tkinter import *
from tkinter.ttk import *
from module_adivina.class_Guess import Guess
from module_adivina.class_text_constants import TextConstants
from module_adivina.class_window import Window
from module_adivina.class_console import Console
from module_adivina.class_load import Load
from tkinter import messagebox

class Play():

    def __init__(self):
        self.window = Tk()
        self.play_console = Console()
        self.play_window = Window()

    def play_game(self):
        self.window.title("ADIVINA EL NUMERO")
        self.window.geometry('350x200')
        btn = Button(self.window, text="JUGAR POR CONSOLA" , command= self.play_console.console_game(0))
        btn.grid(column=3, row=2)
        btn2 = Button(self.window, text="JUGAR POR PANTALLA" , command= self.play_window.play_window(0))
        btn2.grid(column=3, row=3)
        btn3 = Button(self.window, text="LOAD", command= self.load_game()) 
        btn3.grid(column=3, row=4)
        self.window.mainloop()

    def load_game(self):
        window_load = Tk()
        window_load.title("CARGAR JUEGO")
        window_load.geometry('300x200')
        lbl = Label(window_load, text= TextConstants.menu_load())
        lbl.grid(column=3, row=0)
        entry = Entry(window_load)
        entry.grid(column=3, row=1)
        try:
            btn = Button(window_load, text="CARGAR POR CONSOLA", command= self.loadConsole(entry.get()))
            btn.configure(command=window_load.destroy())
            btn.grid(column=3, row=2)
        except:
            messagebox.showinfo(message="ERROR AL CARGAR, VUELVA A INTENTARLO", title="ERROR")
        try:
            btn2 = Button(window_load, text="CARGAR POR PANTALLA", command= self.loadWindow(entry.get()) )
            btn2.configure(command=window_load.destroy())
            btn2.grid(column=4, row=2)
        except:
            messagebox.showinfo(message="ERROR AL CARGAR, VUELVA A INTENTARLO", title="ERROR")
        window_load.mainloop()
    
    def loadConsole(self,entry):
        load = Console()
        load.load_console(entry)
        load.console_game(1)
    
    def loadWindow(self,entry):
        load = Window()
        load.load_play(Load().load(entry))
        load.play_window(1)
