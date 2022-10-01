


class Config:
    def __init__(self,config_file):
        self.config_file = config_file
        import self.config_file
        self.ignored_models = self.config_file.ignored_models
        self.ignored_media_types = self.config_file.ignored_media_types
        self.max_symotaenous_downloads = self.config_file.max_symotaenous_downloads
        self.download_location = self.config_file.download_location
        self.file_name_format = self.config_file.file_name_format


