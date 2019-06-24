from tkinter import *
from tkinter.ttk import *
from module_adivina.class_Guess import Guess
from module_adivina.class_text_constants import TextConstants
from tkinter import messagebox

class Window():
    
    def __init__(self):
        self.window = Tk()
        self.combo = Combobox(self.window)
        self.logic_game = Guess()
        self.number_to_guess

    def set_number(self):
        self.number_to_guess = self.logic_game.generate_number()
    
    def get_number(self):
        return self.number_to_guess

    def positive(self):
        self.logic_game.set_attempts(1)
        self.set_number()

    def button_event(self,value):
        value2 = int(value)
        self.logic_game.set_number(value2)  
        if self.logic_game.first_attempt_failed(self.number_to_guess):
            self.logic_game.add_incorrects()
            messagebox.showinfo(message=self.logic_game.helper(self.get_number), title="AYUDA")
            self.logic_game.set_attempts(self.logic_game.get_attempts + 1)
        elif self.number_to_guess != self.logic_game.get_number():
             self.logic_game.add_incorrects()
             messagebox.showinfo(message=TextConstants.lose(), title="PEDISTE")
             self.logic_game.set_attempts(2)
             self.play_again()
        else:
            self.logic_game.add_acerts()
            messagebox.showinfo(message=TextConstants.win() + self.logic_game.show_results() , title="GANASTE")
            self.logic_game.set_attempts(2)
            self.play_again()

    def play_window(self):
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
        btn2 = Button(self.window, text="SAVE")
        btn2.grid(column=3, row=2)
        self.window.mainloop()

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