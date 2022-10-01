#Classes
##Profile

This is a class for each account that the person scraping has or perhaps their friends. Whatevver, this is just the accounts to sign in to scrape with.

___
#Profile


###Attributes
* username
* auth
* config
* session
* active_subscriptions
* messaged_models
* archived_messages
* typed_usernames
* messages
* bad_usernames
* typed_usernames_models

###username: str
The username of the account.

###auth: object
The auth object is an object that containss the auth details of a profile.
More can be read about this in the auth.md file.

###config: object
The config object is an object that contains the config details of a profile. For example this profile may want to ignore certain media types. This is where that would be stored. 
More can be read about this in the Reference/config/config.md file.

##session: object
This is an object that contains the async http session of a profile. This is used to make requests to the onlyfans site.
More can be read about this in the Reference/session/session.md file.

###active_subscriptions: list of objects
This is a list of the models that the profile has active subscriptions to. Each model is an object that contains the model's details.
More can be read about this in the Reference/models.md file.

###messaged_models: list of objects
This is a list of all of the models a profile has messaged. Each model is an object that contains the model's details. More can be read about this in the Reference/messages/messages.md file.

###messages: list of objects
This is a list of messages as objects. Each message object will contain details such as the model object of the other party in the message, a list of media objects in the mssage, and the message text. as well as any other data onlyfans adds to messages. You can read more about this in the Reference/messages/messages.md file.

###archived_messages: list of objects
This is the same as the messages attribute but it contains the archived messages instead of the normal messages.

###typed_usernames: list of strings
Thiese are stored as strings because in the event of a typo or deleted account, name change, etc. the username could be invalid and thus the username would be dumped. The model objects for the models in this list can be found in the typed_usernames_models attribute.

###typed_usernames_models: list of objects
This is the model objects that were able to be constructed from the typed_usernames.

###bad_typesd_usernames: list of strings
These are the usernames that could not be constructed into a model object. This could be that the user deleted their account, was banned, username was changed / misspelled, etc.


###Methods
Coming Soon



