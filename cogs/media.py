import constants

# Class used to store media information.
# This allows us to store all data pertaining to a media file in one place.


# List of audio file extensions.
audio_file_extensions = [

    'mp3',
]

#List of video file extensions.
video_file_extensions = [

    'mp4',
    'webm',

]

# List of image file extensions.
image_file_extensions = [

    'jpg',
    'jpeg',
    'png',
    'gif',
    'bmp',
    'tiff',
    'svg',
    '.webp',

]


Class Media:
    def __init__(self):
        self.source = ""
        self.file_name = ""
        self.file_extension = ""
        self.media_type = ""
        self.model = ""
        if self.file_extension in audio_file_extensions:
            self.media_type = "audio"
        elif self.file_extension in video_file_extensions:
            self.media_type = "video"
        elif self.file_extension in image_file_extensions:
            self.media_type = "image"
        else:
            self.media_type = "unknown"


    def is_photo(self):
        if self.file_extension in image_file_extensions:
            return True
        else:
            return False
    def is_video(self):
        if self.file_extension in video_file_extensions:
            return True
        else:
            return False
    def is_audio(self):
        if self.file_extension in audio_file_extensions:
            return True
        else:
            return False
    def is_unknown(self):
        if self.file_extension not in audio_file_extensions and self.file_extension not in video_file_extensions and self.file_extension not in image_file_extensions:
            return True
        else:
            return False
    def is_older_than(self, date: datetime):
        if self.date < date:
            return True
        else:
            return False
    def is_newer_than(self, date: datetime):
        if self.date > date:
            return True
        else:
            return False
