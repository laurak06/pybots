import scrapy


class AlltimeTabletsSpider(scrapy.Spider):
    name = "alltime_tablets"
    allowed_domains = ["www.alltime.ru"]
    start_urls = ["https://www.alltime.ru/watch/"]

    custom_settings = {
        'CONCURRENT_REQUEST': 1,
        'DONWLOAD_DELAY': 2
    }

    def start_requests(self):
        self.current_page = 1
        urls = [f'https://www.alltime.ru/watch/?PAGEN_1={i}' for i in range(1, 10)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        products_items = response.css('a.catalog-item-link>span::text').extract()
        product_prices = response.css('div.catalog-item-price-prices > span.catalog-item-price.text-h5::text').extract()
        print('-----------------------------')
        print(products_items)
        print(product_prices)
        print('-----------------------------')
        data = zip(products_items, product_prices)
        for item in data:
            scared_info = {
                'page': response.url,
                'name': item[0],
                'price': item[1].replace('\t', '').replace('\n', '')
            }
            yield scared_info
            self.current_page += 1
