import scrapy

class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        print("[ parse ]")
        
        print(response.xpath("//h3/a").get())