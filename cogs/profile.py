import constants
import cogs.auth
import cogs.config

# This is the class that will be used to store  the scrapers profile data. Scrapers will import this class and call methods of the profile.
# For example, jackmehauf2382.scrape('username') or jackmehauf2382.scrape_all() each command will take an argument such as 'photos', 'videos', 'audios'.
# If the argument is left blank it will default to all media types.

class Profile:
    def __init__(self,auth_file,config_file):
        self.config = cogs.config.Config(config_file)   # This is where the config file is passed to the profile class and as a result the scraper.
        self.active_subscriptions = []   # This is a list of all the active subscriptions for this profile.
        self.messaged_models = self.    # This is a list of all the models that have been messaged by this profile.
        self.typed_usernames = []     # This is a list of all the usernames that have been typed by this profile. Each name stored as a string.
        self.auth = cogs.auth.Auth(auth_file)   # This is the auth object that will be used to authenticate the profile.
        self.config = cogs.config.Config(config_file)   # This is the config object that will be used to configure the scraper for the profile.
        self.messages = []  # This is a list of all the messages that have been sent / received by this profile.
        self.archived_messages = [] # This is a list of all the archived messages that have been sent / received by this profile.
        self.typed_usernames_models = []    # This is a list of all the models that have been typed by this profile in object form if they were able to be constructed.
        self.bad_usernames = []     # This is a list of all the usernames that have been typed by this profile that were not able to be constructed into a model object.



