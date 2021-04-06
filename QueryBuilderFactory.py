#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 00:14:09 2021
@author:aude11
"""
from QueryBuilder import *


class QueryBuilderFactory():
    def __init__(self):
        self.spring_month = ("March", "April", "May")
        self.winter_month = ("December", "January", "February")
        self.summer_month = ("June", "July", "August")
        self.autum_month = ("September", "October", "November")

    def create(self, day, month):
        if month in self.spring_month:
            return Spring(day, month)
        elif month in self.winter_month:
            return Winter(day, month)
        elif month in self.summer_month:
            return Summer(day, month)
        else:
            return Autum(day, month)
