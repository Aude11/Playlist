#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 19:07:38 2021

@author: aude11
"""
from MediaStrategy import MediaStrategy
from MediaYoutube import MediaYoutube
from MediaSoundcloud import MediaSoundcloud
from MediaSpotify import MediaSpotify


class MediaStrategyFactory():
    def __init__(self):
        self.youtube = "youtube"
        self.spotify = "spotify"
        self.soundcloud = "soundcloud"

    def select(self, platform):
        platform = platform.lower()
        if platform == self.youtube:
            return MediaYoutube()
        elif platform == self.spotify:
            return MediaSpotify()
        elif platform == self.soundcloud:
            return MediaSoundcloud()
        else:
            print("The media entered is unknown\nPlease enter a valid Media")
