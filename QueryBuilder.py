#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 12:13:12 2021
@author: aude11

"""
import random


class QueryBuilder():
    def __init__(self, day, month):
        self.query = "playlist mix- "
        self.month = month
        self.day = day

    def buildQuery(self):
        pass


class Spring(QueryBuilder):
    def __init__(self, day, month):
        QueryBuilder.__init__(self, day, month)

    def buildQuery(self):
        if self.month == "March":
            return self.query + "classic"
        elif self.month == "April":
            return self.query + "rock"
        elif self.month == "May":
            return self.query + "electro"
        else:
            return self.query + "wap"


class Autum(QueryBuilder):
    def __init__(self, day, month):
        QueryBuilder.__init__(self, day, month)

    def buildQuery(self):
        if self.month == "September":
            return self.query + "school song"
        elif self.month == "October":
            return self.query + "spooky song"
        elif self.month == "November":
            return self.query + "chillout rain"
        else:
            return self.query + "wap"


class Summer(QueryBuilder):
    def __init__(self, day, month):
        QueryBuilder.__init__(self, day, month)

    def buildQuery(self):
        self.query = random.choice(['playlist mix - summer',
                                    'mix - summer hit',
                                    'mix - latinos song'])
        return self.query


class Winter(QueryBuilder):
    def __init__(self, day, month):
        QueryBuilder.__init__(self, day, month)

    def buildQuery(self):
        if self.month == "December":
            if self.day <= 25:
                return self.query + "christmas rock"
            else:
                return self.query + "skiing"
        elif self.month == "January":
            return self.query + "metal"
        elif self.query == "February":
            return self.query + "chill out"
        else:
            return self.query + "wap mix"
