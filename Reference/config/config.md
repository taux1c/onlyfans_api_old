#Classes
## Config
This is a class that holds a profiles specific configuration. This is to allow for the code to run multiple profiles at the same time.

---

#Config
##Attributes
*config_file (str)*: The path to the config file. This eventually is going to be a pathlib path.


*ignored_models (list)*: A list of models that the user doesn't want to scrape.


*ignored_media_types (list)*: A list of media types that the user doesn't want to scrape.


*max_symotaenous_downloads (int)*: The maximum number of downloads that can be happening at the same time.


*download_location (str)*: The location that the user wants to download the media to for that profile.


*file_name_format (str)*: The format that the user wants the file name to be in.

