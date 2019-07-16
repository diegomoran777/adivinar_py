from module_adivina.class_guess import Guess
from module_adivina.class_text_constants import TextConstants
from module_adivina.class_save import Save
from module_adivina.class_load import Load
import json

class Console:
    
    def __init__(self):
        self.game_logic = Guess()
        self.set_number(0)
        self.save = Save()

    def set_number(self, numberv):
        self.number = numberv

    def get_number(self):
        return self.number

    def options(self):
        inp = input(TextConstants.main_menu_console)
        if inp == 2:
            input_save = input(TextConstants.menu_save)
            try:
                self.save.save_console(self.json_pass,input_save)
            except:
                print(TextConstants.menu_error_save())
                self.options()
        
    def out_range_input(self):
        self.set_number(int(input(TextConstants.input_number)))
        while not self.game_logic.is_in_range(self.get_number()):
            self.set_number(int(input(TextConstants.input_number)))
            
    def console_game(self,load):
        variable="y"
        yes = "y"
        while variable.lower() == yes:    
            if load == 0:
                self.game_logic.set_number(self.game_logic.generate_number())
            load = 0
            while self.game_logic.get_attempts() <= 2:
                self.options()
                self.out_range_input()
                if self.game_logic.first_attempt_failed(self.get_number()):
                    self.game_logic.add_incorrects()
                    print(self.game_logic.helper(self.get_number()))
                elif self.get_number() != self.game_logic.get_number():
                    self.game_logic.add_incorrects()
                    print(TextConstants.lose())
                    self.game_logic.set_attempts(3)
                else:
                    self.game_logic.add_hits()
                    print(TextConstants.win())
                    self.game_logic.set_attempts(3)
                print(self.game_logic.show_results())
                self.game_logic.set_attempts(self.game_logic.get_attempts + 1)
            variable = input(TextConstants.menu_try_again())

    def json_pass(self):
        json_dic = { "number_to_guess" : self.game_logic.get_number() , "attempts" : self.game_logic.get_attempts(), "incorrects" : self.game_logic.get_incorrects(), "hits" : self.game_logic.get_hit() }
        parsed_dic = json.dumps(json_dic)
        return parsed_dic

    def load_set_console(self,json_loads):
        self.game_logic.set_number(json_loads["number_to_guess"])
        self.game_logic.set_attempts(json_loads["attempts"])
        self.game_logic.set_incorrects(json_loads["incorrects"])
        self.game_logic.set_hit(json_loads["hits"])
    
    def load_console(self,entry):
        self.load_set_console(Load().load(entry))
