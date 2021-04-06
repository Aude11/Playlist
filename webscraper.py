#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 15:24:27 2021

@author: aude11
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class WebScraper():
    def __init__(self, url):
        self.url = url

    def setWebdriver(self, option_private_mode):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches",
                                        ["enable-automation"])
        options.add_experimental_option('useAutomationExtension',
                                        False)
        if option_private_mode is True:
            options.add_argument("--incognito")
        driver = webdriver.Chrome(ChromeDriverManager().install(),
                                  options=options)
        driver.maximize_window()
        driver.get(self.url)
        driver.implicitly_wait(5)
        return driver
