import scrapy


class VeganRecipesItem(scrapy.Item):
    title = scrapy.Field()
    image = scrapy.Field()
    ingredients = scrapy.Field()
    preparation = scrapy.Field()
    time = scrapy.Field()
    url = scrapy.Field()
