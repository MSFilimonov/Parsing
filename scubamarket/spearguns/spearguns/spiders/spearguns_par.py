import scrapy

class spearguns_par(scrapy.Spider):
    name = 'scubamarket'
    start_urls = ['https://www.scubamarket.ru/catalog/spearguns/']

    def parse(self, response):
        for link in response.css('div.offer a::attr(href)'):
            yield response.follow(link, callback=self.parse_guns)

        for i in range (1.25):
            next_page = f'https://www.scubamarket.ru/catalog/spearguns/?PAGEN_1={i}'
            yield response.follow(next_page, callback=self.parse)

    def parse_guns(self, response):
        yield{
            'name':response.css('a.kakh3::text').get,
            'price':response.css('div.offer div.price span::text').get().lstrip('\n             ') 

                       
        }