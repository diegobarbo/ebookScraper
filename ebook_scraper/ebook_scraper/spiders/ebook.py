import scrapy
from ebook_scraper.items import EbookItem
from scrapy.loader import ItemLoader




class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls = ["https://books.toscrape.com/catalogue/category/books/travel_2/"]

    def parse(self, response):
        ebooks = response.css("article.product_pod")

        for ebook in ebooks:
            loader = ItemLoader(item=EbookItem(), selector=ebook)
            
            loader.add_css('title', "h3 a::attr(title)")                
            loader.add_css('price', "p.price_color::text")
            
            yield loader.load_item()