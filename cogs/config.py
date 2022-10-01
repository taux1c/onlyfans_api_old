import json

class Config:
    def __init__(self,config_file):
        self.config_file = config_file
        self.config = json.loads(self.config_file)
        



