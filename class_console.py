from module_adivina.class_Guess import Guess
from module_adivina.class_text_constants import TextConstants

class Console:
    
    def __init__(self):
        self.game_logic = Guess()
        self.set_number_to_guess(0)

    def set_number_to_guess(self, numberv):
        self.number_to_guess = numberv

    def options(self):
        inp = input(TextConstants.main_menu_console)
        if inp == 2:
            print("save") #FALTA REALIZAR LA FUNCION SAVE
        
    def out_range_input(self):
        number = int(input(TextConstants.input_number))
        self.game_logic.set_number(number)
        while not self.game_logic.is_in_range(number):
            number = int(input(TextConstants.input_number()))
            self.game_logic.set_number(number)

    def console_juego(self,load):
        variable="y"
        yes = "y"
        while variable.lower() == yes:    
            if load == 0:
                self.set_number_to_guess(self.game_logic.generate_number())
            load = 0
            while self.game_logic.get_attempts() <= 2:
                self.options()
                self.out_range_input()
                if self.game_logic.first_attempt_failed(self.number_to_guess):
                    self.game_logic.add_incorrects()
                    print(self.game_logic.helper(self.number_to_guess))
                elif self.number_to_guess != self.game_logic.get_number():
                    self.game_logic.add_incorrects()
                    print(TextConstants.lose())
                    self.game_logic.set_attepts(3)
                else:
                    self.game_logic.add_acerts()
                    print(TextConstants.win())
                    self.game_logic.set_attepts(3)
                print(self.game_logic.show_results())
                self.game_logic.set_attepts(self.game_logic.get_attempts + 1)
            variable = input(TextConstants.menu_try_again())

