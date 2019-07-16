

class Save():

    def save_console(self,json_parsed, input_save):
        file = open(input_save + ".json" , "w")
        file.write(json_parsed)
        file.close()

    def save_window(self,json_parsed,input_save):
        file = open(input_save + ".json" , "w")
        file.write(json_parsed)
        file.close()
        

