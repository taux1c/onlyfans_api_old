
import pathlib
import json

class Config:
    def __init__(self,config_file):
        self.config_file = config_file
        import self.config_file
        self.ignored_models = []
        self.ignored_media_types = []
        self.max_symotaenous_downloads = 0
        self.download_location = ""
        

