import scrapy


class AlltimeTabletsSpider(scrapy.Spider):
    name = "chocolate_tablets"
    allowed_domains = ["www.chocolate.co.uk"]
    start_urls = ["https://www.chocolate.co.uk/collections/all"]

    custom_settings = {
        'CONCURRENT_REQUEST': 1,
        'DONWLOAD_DELAY': 2
    }

    def start_requests(self):
        self.current_page = 1
        urls = [f'https://www.chocolate.co.uk/collections/all?page={i}' for i in range(1, 4)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        products_items = response.css('div.product-item__info > div > a::text').extract()
        products_prices = response.css('div.product-item__info > div > div > div > span::text').extract()
        product_photos = response.css('div.product-item__image-wrapper > a > img::attr(src)').extract()
        print('-----------------------------')
        print(products_items)
        print(product_photos)
        print('-----------------------------')
        data = zip(products_items, products_prices, product_photos)
        for item in data:
            scared_info = {
                'page': response.url,
                'name': item[0],
                'price': item[1].strip(),
                'photo': item[2].strip()
            }
            if not scared_info['price']:
                continue
            yield scared_info
            self.current_page += 1
