#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 12:53:04 2021

@author: vaude11
"""
import webbrowser
import urllib.request
import urllib.parse
import re
from MediaStrategy import MediaStrategy


class MediaYoutube(MediaStrategy):
    def __init__(self):
        MediaStrategy.__init__(self)
        self.url = self.url + 'www.youtube.com/results?search_query='

    def runMusic(self, query):
        query_string = urllib.parse.urlencode({"search_query": query})
        html = urllib.request.urlopen(self.url +
                                      query_string)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        playlist_yt_link = "https://www.youtube.com/watch?v=" + video_ids[0]
        return webbrowser.open(playlist_yt_link, new=2)
