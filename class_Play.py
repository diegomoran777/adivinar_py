from tkinter import *
from tkinter.ttk import *
from module_adivina.class_Guess import Guess
from module_adivina.class_Menu import Menu
from module_adivina.class_Window import Window
from module_adivina.class_console import Console
from tkinter import messagebox

class Play():

    def _init_(self):
        self.window = Tk()

    def play_game(self):
        self.window.title("ADIVINA EL NUMERO")
        self.window.geometry('350x200')
        btn = Button(self.window, text="JUGAR POR CONSOLA" , command= Console().console_juego)
        btn.grid(column=3, row=2)
        btn2 = Button(self.window, text="JUGAR POR PANTALLA" , command= Window().play_window)
        btn2.grid(column=3, row=3)
        btn3 = Button(self.window, text="LOAD") #FALTA REALIZAR LA FUNCION
        btn3.grid(column=3, row=4)
        self.window.mainloop()
