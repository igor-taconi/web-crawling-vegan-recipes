import scrapy


class TudogostosoSpider(scrapy.Spider):
    name = 'tudogostoso'
    allowed_domains = ['tudogostoso.com.br']
    start_urls = ['https://www.tudogostoso.com.br/busca?q=vegana']

    def parse(self, response):
        pass
