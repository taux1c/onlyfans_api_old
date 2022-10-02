import constants
import cogs.auth
import cogs.config

# This is the class that will be used to store  the scrapers profile data. Scrapers will import this class and call methods of the profile.
# For example, jackmehauf2382.scrape('username') or jackmehauf2382.scrape_all() each command will take an argument such as 'photos', 'videos', 'audios'.
# If the argument is left blank it will default to all media types.

class Profile:
    def __init__(self,config_file):
        self.config = cogs.config.Config(config_file)   # This is where the config file is passed to the profile class and as a result the scraper.
        self.active_subscriptions = []   # This is a list of all the active subscriptions for this profile.
        self.messaged_models = []   # This is a list of all the models that have been messaged by this profile.
        self.typed_usernames = []     # This is a list of all the usernames that have been typed by this profile. Each name stored as a string.
        self.auth = cogs.auth.Auth(self.config.auth_file)   # This is the auth object that will be used to authenticate the profile.
        self.config = cogs.config.Config(config_file)   # This is the config object that will be used to configure the scraper for the profile.
        self.messages = []  # This is a list of all the messages that have been sent / received by this profile.
        self.archived_messages = [] # This is a list of all the archived messages that have been sent / received by this profile.
        self.typed_usernames_models = []    # This is a list of all the models that have been typed by this profile in object form if they were able to be constructed.
        self.bad_usernames = []     # This is a list of all the usernames that have been typed by this profile that were not able to be constructed into a model object.
        self.session = cogs.session.Session(self.auth)   # This is the session object that will be used to store the session data for this profile.
        self.pause = False  # This is a boolean that will be used to pause the scraper for this profile.
        self.stop = False   # This is a boolean that will be used to stop the scraper for this profile. This will continue any active downloads but will stop when safe to do so.
        self.resume = False # This is a boolean that will be used to resume the scraper for this profile.
        self.busy = False   # This is a boolean that will be used to indicate if the scraper is busy or not.

    def start(self):
        if self.stop:
            return
        if self.pause:
            return "{} is paused. To resume please use the resume command.".format(self.config.username)

        if self.busy:
            return "{} is busy. Please wait until it is finished before starting it again.".format(self.config.username)
        #This is where the scraper will be started. Remember to set self.busy to True when the scraper is started and set it to False when it is finished.
        self.busy = True




    def pause(self):
        if self.busy:

