# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst

def remove_sign(value):
    return value.replace('$','').strip()

def convert_string(value):
    value = int(float(value))
    return value


class SipwhiskeyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor = MapCompose(str.lower,str.strip) , output_processor = TakeFirst())
    price = scrapy.Field(input_processor = MapCompose(remove_sign), output_processor = TakeFirst())
    brand = scrapy.Field(output_processor= TakeFirst())
    
