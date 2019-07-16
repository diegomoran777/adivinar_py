from tkinter import *
from tkinter.ttk import *
from module_adivina.class_guess import Guess
from module_adivina.class_text_constants import TextConstants
from tkinter import messagebox
from module_adivina.class_save import Save
import json

class Window():
    
    def __init__(self):
        self.window = Tk()
        self.combo = Combobox(self.window)
        self.logic_game = Guess()
        self.save = Save()
    
    def set_number_to_guess(self, parsed_mumber):
        self.number_to_guess = parsed_mumber

    def positive(self):
        self.logic_game.set_attempts(1)
        self.logic_game.set_number(self.logic_game.generate_number())

    def button_event(self,value):
        value2 = int(value)
        if self.logic_game.first_attempt_failed(value2):
            self.logic_game.add_incorrects()
            messagebox.showinfo(message=self.logic_game.helper(value2), title="AYUDA")
            self.logic_game.set_attempts(self.logic_game.get_attempts + 1)
        elif self.logic_game.get_number() != value2:
             self.logic_game.add_incorrects()
             messagebox.showinfo(message=TextConstants.lose(), title="PEDISTE")
             self.logic_game.set_attempts(2)
             self.play_again()
        else:
            self.logic_game.add_hits()
            messagebox.showinfo(message=TextConstants.win() + self.logic_game.show_results() , title="GANASTE")
            self.logic_game.set_attempts(2)
            self.play_again()

    def play_window(self,load):
        if load == 0:
            self.logic_game.set_number(self.logic_game.generate_number())
        load = 0
        self.window.title("ADIVINA EL NUMERO")
        self.window.geometry('350x200')
        label = Label(self.window, text= self.logic_game.show_results())
        label.grid(column=4, row=0)
        label2 = Label(self.window, text="QUE NUMERO PUEDE SER EL OCULTO?")
        label2.grid(column=0, row=0)
        self.combo
        self.combo['values'] = (1,2,3,4,5,6,7,8,9,10)
        self.combo.current(0)
        self.combo.grid(column=0, row=1)
        btn = Button(self.window, text="ACEPTAR" , command= self.button_event(self.combo.get()))
        btn.grid(column=1, row=2)
        btn2 = Button(self.window, text="SAVE", command= self.save_play())
        btn2.grid(column=3, row=2)
        self.window.mainloop()

    def save_play(self):
        window_save = Tk()
        window_save.title("SALVAR JUEGO")
        window_save.geometry('300x200')
        lbl = Label(window_save, text=TextConstants.menu_save)
        lbl.grid(column=3, row=0)
        entry = Entry(window_save)
        entry.grid(column=3, row=1)
        try:
            btn = Button(window_save, text="SALVAR", command= self.save.save_window(self.Json_pass(),entry.get()))
            btn.configure(command=window_save.destroy())
            btn.grid(column=3, row=2)
        except:
            messagebox.showinfo(message="ERROR AL SALVAR, VUELVA A INTENTARLO", title="ERROR")
        window_save.mainloop()

    def play_again(self):
        window_again = Tk()
        window_again.title("VOLVER AJUGAR")
        window_again.geometry('300x200')
        lbl = Label(window_again, text=TextConstants.menu_play_again())
        lbl.grid(column=3, row=0)
        btn = Button(window_again, text="SI", command=  self.positive)
        btn.configure(command=window_again.destroy())
        btn.grid(column=3, row=1)
        btnTwo = Button(window_again, text="NO", command= self.window.destroy())
        btnTwo.configure(command= window_again.destroy())
        btnTwo.grid(column=4, row=1)
        window_again.mainloop()

    def load_play(self,json_loads):
        self.logic_game.set_number(json_loads["number_to_guess"])
        self.logic_game.set_attempts(json_loads["attempts"])
        self.logic_game.set_incorrects(json_loads["incorrects"])
        self.logic_game.set_hit(json_loads["hits"])

    def Json_pass(self):
        json_dic = { "number_to_guess" : self.logic_game.get_number(), "attempts" : self.logic_game.get_attempts(), "incorrects" : self.logic_game.get_incorrects(), "hits" : self.logic_game.get_hit() }
        parsed_dic = json.dumps(json_dic)
        return parsed_dic


