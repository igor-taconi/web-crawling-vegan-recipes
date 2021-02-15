from scrapy import Spider, Request
from ..items import VeganRecipesItem


class TudogostosoSpider(Spider):
    name = 'tudogostoso'
    # allowed_domains = ['tudogostoso.com.br']
    start_urls = ['https://www.tudogostoso.com.br/busca?q=vegana']

    def parse(self, response):
        """Entrar em cada receita."""
        links = response.xpath(
            '//div[@class="pagination"]/parent::div//a[@class="link row m-0"]/@href'
        ).getall()
        for link in links:
            yield Request(response.urljoin(link), callback=self.parse_recipes)

        # # TODO: testar xpath
        # """Sistema de paginação."""
        # pagination = response.xpath(
        #     '//div[@class="pagination"]//a//@href'
        # ).getall()
        # for next in pagination:
        #     yield Request(response.urljoin(next), callback=self.parse)
        pass

    def parse_recipes(self, response):
        """Parsear a receita."""
        items = VeganRecipesItem()

        title = (
            response.xpath('//h1[@tabindex="0"]//text()')
            .get()
            .replace('\n', '')
        )
        image = response.css('img.pic::attr(src)').get()
        ingredients = ', '.join(
            response.css('div#info-user ul li span::text').getall()
        )
        preparation = ', '.join(
            response.css('div.instructions ol li span::text').getall()
        )
        time = response.css('time.dt-duration::text').get().replace('\n', ' ')

        # yield {
        #     'title': title,
        #     'image': image,
        #     'ingredients': ingredients,
        #     'preparation': preparation,
        #     'time': time,
        #     'url': response.url,
        # }
        items['title'] = title
        items['image'] = image
        items['ingredients'] = ingredients
        items['preparation'] = preparation
        items['time'] = time
        items['url'] = response.url

        yield items
