import scrapy

class QuotesSpider(scrapy.Spider):
    name = "toscrape-xpath"

    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        for quote in response.xpath("descendant::div[@class='quote']"):
            text = quote.xpath("descendant::span[@class='text']/text()").get()
            author = quote.xpath("descendant::small[@class='author']/text()").get()
            tags = quote.xpath("descendant::div/a/text()").getall()
            yield dict(text=text, author=author, tags=tags)

        yield from response.follow_all(xpath='//ul/*/a', callback=self.parse)
