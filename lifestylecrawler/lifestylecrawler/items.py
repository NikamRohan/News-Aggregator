# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy_djangoitem import DjangoItem

import sys

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'News_Aggregator.settings'

from news.models import LHeadline


class LifestylecrawlerItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = LHeadline
