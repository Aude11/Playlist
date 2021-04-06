#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 13:15:43 2021

@author: aude11
"""
import time
from webscraper import WebScraper
from MediaStrategy import MediaStrategy


class MediaSoundcloud(MediaStrategy):
    def __init__(self):
        MediaStrategy.__init__(self)
        self.url = 'https://soundcloud.com'

    def runMusic(self, query):
        driver = WebScraper(self.url).setWebdriver(True)
        search_box = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/div/div[1]/span/span/form/input')
        search_box.send_keys(query)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/div/div[1]/span/span/form/button').click()
        time.sleep(2)
        play_button = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[3]/div/div/div/ul/li[1]/div/div/div/div[2]/div[1]/div/div/div[1]/a')
        music_play = play_button.click()
        return music_play  