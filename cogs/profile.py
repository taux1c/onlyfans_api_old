import constants
import cogs.auth


# This is the class that will be used to store  the scrapers profile data. Scrapers will import this class and call methods of the profile.
# For example, jackmehauf2382.scrape('username') or jackmehauf2382.scrape_all() each command will take an argument such as 'photos', 'videos', 'audios'.
# If the argument is left blank it will default to all media types.

class Profile:
    def __init__(self,config_file):
        self.active_subscriptions = []
        self.messaged_models = []
        self.typed_usernames = []
        self.auth = cogs.auth.Auth(auth_file)
        self.config = cogs.config.Config(config_file)
        self.messages = []
        self.archived_messages = []
        self.typed_usernames_models = []
        self.bad_usernames = []



