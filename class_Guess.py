from random import randint
from module_adivina.class_Menu import Menu

class Guess():


    def _init_(self):
        self.set_acert(0)
        self.set_incorrects(0)
        self.set_number(0)
        self.set_attmepts(1)
    
    def get_number(self):
        return self._number

    def get_acert(self):
        return self._acert
    
    def get_incorrects(self):
        return self._incorrects
    
    def get_attempts(self):
        return self._attempts

    def set_number(self,number):
        self._number = number

    def set_attmepts(self,attempts):
        self._attempts = attempts

    def set_incorrects(self, incorrects):
        self._incorrects = incorrects

    def set_acert(self, acert):
        self._acert = acert
        
    def acert_failed_number(self, number_input):
        return number_input != self._number
    
    def help_or_not(self,attempt):
        return attempt == 1
    
    def again_play(self, input):
         return input == Menu().menu_yes

    def generate_number(self):
        return randint(1,10) 

    def  add_acerts(self):
        self.set_acert(self.get_acert + 1)
    
    def add_incorrects(self):
        self.set_incorrects(self._incorrects + 1)
    
    def is_in_range(self,number_input):
        return self.get_number in randint(1,10)

    def first_intent_failed(self,input):
        return input != self.get_number() and self.help_or_not(self.get_attempts())
     
    def helper(self,input):
        if input > self.get_number:
            return Menu().menu_higher
        else:
            return Menu().menu_less

    def show_results(self):
        return "MISTAKES: " + str(self.get_incorrects) + " ACERTS: " + str(self.get_acert)




    
