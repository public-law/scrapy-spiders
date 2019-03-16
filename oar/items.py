# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class OAR(scrapy.Item):
    chapters = scrapy.Field()

    
class Chapter(scrapy.Item):
    kind = scrapy.Field()
    db_id = scrapy.Field()
    number = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    divisions = scrapy.Field()


class Division(scrapy.Item):
    kind = scrapy.Field()
    db_id = scrapy.Field()
    number = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    rules = scrapy.Field()


class Rule(scrapy.Item):
    kind = scrapy.Field()
    number = scrapy.Field()
    name = scrapy.Field()
    text = scrapy.Field()
    url = scrapy.Field()
