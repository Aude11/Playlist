#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 15:51:20 2021
@author: aude11
"""
import sys
import time
from datetime import date
from QueryBuilderFactory import QueryBuilderFactory
from QueryBuilder import QueryBuilder
from MediaStrategy import MediaStrategy
from MediaStrategyFactory import MediaStrategyFactory


def main():
    today = date.today()
    month = today.strftime("%B")
    day = int(today.strftime("%d"))
    print("One can listen music thought Spotify, Soundcloud and Youtube" +
          "\nEnter the platform: ",
          end='')
    platform = input()
    queryBuilderFactory = QueryBuilderFactory()
    queryBuilder = queryBuilderFactory.create(day, month)
    query = queryBuilder.buildQuery()
    mediastrategyfactor = MediaStrategyFactory()
    media = mediastrategyfactor.select(platform)
    if media is None:
        sys.exit(0)
    media.runMusic(query)
    time.sleep(2)
    print("Playing music!")
    time.sleep(20)
    print("End of the music")


if __name__ == "__main__":
    main()
