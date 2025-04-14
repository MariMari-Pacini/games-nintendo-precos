import scrapy


class GamesSpider(scrapy.Spider):
    name = "games"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/jogo-nintendo-switch#D[A:jogo%20nintendo%20switch]"]

    def parse(self, response):
        
        products = response.css('div.ui-search-result__wrapper')

        for product in products:
            yield{
                'brand': product.css('span.poly-component__brand::text').get(),
                'name': product.css('a.poly-component__title::text').get()

            }
            