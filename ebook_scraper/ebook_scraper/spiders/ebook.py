import scrapy

class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        print("[ parse ]")
        
        print('[css]:', response.css('h3 a::text')[0])
        print('[xpath]:', response.xpath('//h3/a/text()')[0])