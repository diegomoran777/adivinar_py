from tkinter import *
from tkinter.ttk import *
from module_adivina.class_Guess import Guess
from module_adivina.class_Menu import Menu
from tkinter import messagebox

class Window():
    
    def _init_(self):
        self.window = Tk()
        self.combo = Combobox(self.window)
        self.p = Guess()
        self.m = Menu()
        self.number_g

    def set_number(self):
        self.number_g = self.p.generate_number()
    
    def get_number(self):
        return self.number_g

    def positive(self):
        self.p.set_attmepts(1)
        self.set_number()

    def button_event(self,value):
        value2 = int(value)
        self.p.set_number(value2)  
        if self.p.first_intent_failed(self.number_g):
            self.p.add_incorrects()
            messagebox.showinfo(message=self.p.helper(self.get_number), title="AYUDA")
            self.p.set_attmepts(self.p.get_attempts + 1)
        elif self.number_g != self.p.get_number():
             self.p.add_incorrects()
             messagebox.showinfo(message=self.m.lose(), title="PEDISTE")
             self.p.set_attmepts(2)
             self.play_again()
        else:
            self.p.add_acerts()
            messagebox.showinfo(message=self.m.win() + self.p.show_results() , title="GANASTE")
            self.p.set_attmepts(2)
            self.play_again()

    def play_window(self):
        self.window.title("ADIVINA EL NUMERO")
        self.window.geometry('350x200')
        label = Label(self.window, text= self.p.show_results())
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
        lbl = Label(window_again, text=self.m.menu_play_again())
        lbl.grid(column=3, row=0)
        btn = Button(window_again, text="SI", command=  self.positive)
        btn.configure(command=window_again.destroy())
        btn.grid(column=3, row=1)
        btnTwo = Button(window_again, text="NO", command= self.window.destroy())
        btnTwo.configure(command= window_again.destroy())
        btnTwo.grid(column=4, row=1)