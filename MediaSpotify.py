#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 12:58:03 2021

@author: aude11
"""
import time
import pickle
from os import path
from webscraper import WebScraper
from MediaStrategy import MediaStrategy
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from getpass import getpass #not working on spyder IDE (to hide password)


class MediaSpotify(MediaStrategy):
    def __init__(self):
        MediaStrategy.__init__(self)
        self.url = self.url + 'open.spotify.com/search'
        self.username = ''
        self.password = ''

    def runMusic(self, query):
        if path.isfile('cookies.pkl') is True:
            cookies = pickle.load(open("cookies.pkl", "rb"))
            driver = WebScraper(self.url).setWebdriver(False)
            for cookie in cookies:
                driver.add_cookie(cookie)
                driver.refresh()
            play = self.search_playlist(driver, query)
        else:
            driver = self.log_into_spotify()
            play = self.search_playlist(driver, query)
        return play.click()

    def search_playlist(self, driver, query):
        search_box = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/input')
        search_box.send_keys(query)
        time.sleep(2)
        playlist = driver.find_element_by_xpath('//*[@id="searchPage"]/div/div/section[1]/div[2]/div/div/div/div[4]')
        playlist.click()
        time.sleep(2)
        play = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[3]/main/div[2]/div[2]/div/div/div[2]/section/div[2]/div[2]/div/button[1]')
        return play

    def get_login(self):
        print('Enter email id : ', end='')
        self.username = input()
        print('Enter password : ', end='')
        #self.password = input()
        self.password = getpass('Enter Password:') #not working on spyder IDE

    def log_into_spotify(self):
        self.get_login()
        driver = WebScraper(self.url).setWebdriver(False)
        cookies_pop = WebDriverWait(driver, 2).until(ec.presence_of_element_located((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')))
        cookies_pop.click()
        driver.implicitly_wait(3)
        loggin_sign = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[5]/button[2]')
        loggin_sign.click()
        driver.implicitly_wait(3)
        username_field = driver.find_element_by_xpath('//*[@id="login-username"]')
        username_field.send_keys(self.username)
        time.sleep(2)
        password_field = driver.find_element_by_xpath('//*[@id="login-password"]')
        password_field.send_keys(self.password)
        time.sleep(2)
        button_login = driver.find_element_by_xpath('//*[@id="login-button"]')
        button_login.click()
        time.sleep(3)
        pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
        return driver
