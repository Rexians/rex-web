from __future__ import unicode_literals
from pytube import YouTube

class ytdownload:
    def __init__(self):
        None

    def download(self,link):
        video = link.streams.filter(file_extension="mp4").first()
        filepath = video.download()
        return filepath
        
