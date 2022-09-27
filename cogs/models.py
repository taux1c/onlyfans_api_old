import config

# This class will be used to store the models information. Including their media, profile information, and other data.
# This is what will be passed to the scraper for downloading.
# For example, if big_jugs69 is a model then big_jugs69.messages.media will return a list of all media in the models messages.

# Eventually there will be a post frequency function that will return the average frequency of posts in days.


Class Model:
    def __init__(self):
        self.model_name = ""
        self.model_id = ""
        self.messages = []
        self.highlights = []
        self.posts = []
        self.archived_posts = []

    def has_media(self):
        if len(self.messages) > 0:
            return True
        elif len(self.highlights) > 0:
            return True
        elif len(self.posts) > 0:
            return True
        elif len(self.archived_posts) > 0:
            return True
        else:
            return False
