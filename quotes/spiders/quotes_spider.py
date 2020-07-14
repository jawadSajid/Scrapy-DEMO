import scrapy
from .. items import QuotesItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "http://quotes.toscrape.com/"
    ]

    def parse(self, response):
        # title = response.css("title::text").extract()
        # yield {'titletext': title}

        items = QuotesItem()

        all_div_quotes = response.css("div.quote")

        for quote in all_div_quotes:
            title = quote.css("span.text::text").extract()
            author = quote.css("span small.author::text").extract()
            tag = quote.css(".tags meta").xpath("@content").extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            # yield {
            #     "title": title,
            #     "author": author,
            #     "tag": tag
            # }

            yield items
