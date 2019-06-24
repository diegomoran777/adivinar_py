from random import randint
from module_adivina.class_text_constants import TextConstants

class Guess():


    def __init__(self):
        self.set_hit(0)
        self.set_incorrects(0)
        self.set_number(0)
        self.set_attempts(1)
    
    def get_number(self):
        return self._number

    def get_hit(self):
        return self._hit
    
    def get_incorrects(self):
        return self._incorrects
    
    def get_attempts(self):
        return self._attempts

    def set_number(self,number):
        self._number = number

    def set_attempts(self,attempts):
        self._attempts = attempts

    def set_incorrects(self, incorrects):
        self._incorrects = incorrects

    def set_hit(self, hit):
        self._hit = hit
        
    def hit_failed_number(self, number_input):
        return number_input != self._number
    
    def help_or_not(self,attempt):
        return attempt == 1
    
    def again_play(self, input):
         return input == TextConstants.menu_yes

    def generate_number(self):
        return randint(1,10) 

    def  add_acerts(self):
        self.set_hit(self.get_hit + 1)
    
    def add_incorrects(self):
        self.set_incorrects(self._incorrects + 1)
    
    def is_in_range(self,number_input):
        return self.get_number in randint(1,10)

    def first_attempt_failed(self,input):
        return input != self.get_number() and self.help_or_not(self.get_attempts())
     
    def helper(self,input):
        if input > self.get_number:
            return TextConstants.menu_higher
        return TextConstants.menu_less

    def show_results(self):
        return "MISTAKES: " + str(self.get_incorrects) + " HITS: " + str(self.get_hit)




    
