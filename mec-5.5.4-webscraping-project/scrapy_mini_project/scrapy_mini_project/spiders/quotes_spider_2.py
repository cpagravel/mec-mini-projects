import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes_2"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        print("Parsing response...\n\n\n")
        print(response.css("title::text"))
        print(response.css("title::text").get())
        print(response.css("title::text")[0].get())
        print(response.css("title::text").getall())

        # Print all quotes
        print(response.css(".text::text").getall())

