import json

class Load():

    def load(self,input_load):
        file = open(input_load + ".json","r")
        json_parsed = file.read()
        file.close()
        return json.loads(json_parsed)
 