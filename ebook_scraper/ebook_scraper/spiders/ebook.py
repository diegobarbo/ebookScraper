import scrapy
from ebook_scraper.items import EbookItem


class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        ebooks = response.css("article.product_pod")

        for ebook in ebooks:
            ebook_item = EbookItem()
            
            ebook_item['title'] = ebook.css("h3 a").attrib['title']
            ebook_item['price'] = ebook.css("p.price_color::text").get()

            yield ebook_item