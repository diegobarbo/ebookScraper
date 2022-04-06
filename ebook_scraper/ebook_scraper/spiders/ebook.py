import scrapy
from ebook_scraper.items import EbookItem
from scrapy.loader import ItemLoader




class EbookSpider(scrapy.Spider):
    name = "ebook"
    # start_urls = ["https://books.toscrape.com/catalogue/category/books/sequencial-art"]

    def __init__(self):
        super().__init__()
        self.page_count = 1
        self.total_pages = 4

    def start_requests(self):
        base_url = "https://books.toscrape.com/catalogue/category/books/sequencial-art"

        while self.page_count <= self.total_pages:
            yield scrapy.Request(
                f"{base_url}/page-{self.page_count}.html"
            )
            self.page_count += 1

    def parse(self, response):
        # self.page_count += 1

        ebooks = response.css("article.product_pod")

        for ebook in ebooks:
            loader = ItemLoader(item=EbookItem(), selector=ebook)
            
            loader.add_css('title', "h3 a::attr(title)")                
            loader.add_css('price', "p.price_color::text")
            
            yield loader.load_item()

        # print("[ PAGE COUNT ]:", self.page_count)
        
        # next_btn = response.css("li.next a")

        # if next_btn:
        #     next_page = f"{self.start_urls[0]}/{next_btn.attrib['href']}"            
        #     yield scrapy.Request(url=next_page)

        