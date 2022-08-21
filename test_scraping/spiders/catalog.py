import scrapy


class BookSpider(scrapy.Spider):
    name = 'catalog'
    start_urls = ['https://www.merrell.com/US/en/mens-discount-boots-shoes/']

    def parse(self, response):
        for link in response.css('a.name-link ::attr(href)'):
            print('!!!!!!!!!!!!!!!!!', link.get())
            yield response.follow(link, callback=self.parse_book)

        # Code for several pages
        # for i in range(1, 5):
        #     next_page = f'https://www.merrell.com/US/en/mens-discount-boots-shoes/page-{i}'
        #     yield response.follow(next_page, callback=self.parse)

    def parse_book(self, response):
        item = {
            'url': response.url,
            'title': response.css('div.persistent-details h1::text').get().strip(),
            'price': response.css('span.price-standard::text').get().strip()
        }
        yield item

# run spider for json: scrapy crawl catalog -O shoes.json