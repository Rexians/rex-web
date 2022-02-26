from __future__ import unicode_literals
from pytube import Search
import random

class ytdownload:
    def __init__(self):
        None

    def download(self,link):
        video = link.streams.filter(file_extension="mp4").first()
        filepath = video.download()
        return filepath

class YT:
    def __init__(self) -> None:
        pass

    def get_mcoc_links(self):
        queries = ['mcoc', 'Marvel Contest of Champions', 'Seatin MCOC', 'Rich the man MCOC', 'Lagacy MCOC', 'ContestChampion MCOC', 'Bero Man MCOC']
        query = random.choice(queries)
        s = Search(query)
        links = []
        i = 0
        while i!=10:
            for result in s.results:
                id = result.video_id
                link = f'https://youtube.com/watch?v={id}'
                links.append(link)
                i+=1
        return links          
        
