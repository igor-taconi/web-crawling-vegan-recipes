import scrapy


class TudogostosoSpider(scrapy.Spider):
    name = 'tudogostoso'
    allowed_domains = ['tudogostoso.com.br']
    start_urls = ['http://tudogostoso.com.br/']

    def parse(self, response):
        pass
