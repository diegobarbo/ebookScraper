import scrapy
from scrapy import Item, Field


class EbookItem(scrapy.Item):
    title = Field()
    price = Field()
    
