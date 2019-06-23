from module_adivina.class_Guess import Guess
from module_adivina.class_Menu import Menu

class Console:
    
    def _init_(self):
        self.p = Guess()
        self.set_number_g(0)
        self.p = Guess()

    def set_number_g(self, numberv):
        self.number_g = numberv

    def options(self):
        print(Menu.menu_principal_console)
        inp = input()
        if inp == 2:
            print("save") #FALTA REALIZAR LA FUNCION SAVE
        
    def out_range_input(self):
        print(Menu.input_number)
        number = int(input())
        self.p.set_number(number)
        while not self.p.is_in_range(number):
            print(Menu().input_number())
            number = int(input())
            self.p.set_number(number)

    def console_juego(self,load):
        variable=""
        yes = "y"
        while variable.lower == yes:    
            self.p
            if load == 0:
                self.set_number_g(self.p.generate_number())
            load = 0
            while self.p.get_attempts() <= 2:
                self.options()
                self.out_range_input()
                if self.p.first_intent_failed(self.number_g):
                    self.p.add_incorrects()
                    print(self.p.helper(self.number_g))
                elif self.number_g != self.p.get_number():
                    self.p.add_incorrects()
                    print(Menu().lose())
                    self.p.set_attmepts(3)
                else:
                    self.p.add_acerts()
                    print(Menu().win())
                    self.p.set_attmepts(3)
                print(self.p.show_results())
                self.p.set_attmepts(self.p.get_attempts + 1)
            print(Menu().menu_try_again())
            variable = input()

