import scrapy
from scrapy import Item, Field
from itemloaders.processors import MapCompose, TakeFirst

def get_price(txt):
    return float(txt.replace('£', ''))

class EbookItem(scrapy.Item):
    title = Field(
        output_processor=TakeFirst()
    )
    price = Field(
        input_processor=MapCompose(get_price, ),
        output_processor=TakeFirst()
    )
    
