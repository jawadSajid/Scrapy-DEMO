import scrapy
from ..items import QuotesItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    page_number = 2
    start_urls = [
        "http://quotes.toscrape.com/page/1/"
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

        # Follow multiple pages
        # next_page = response.css("li.next a::attr(href)").get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)

        # Pagination
        next_page = "http://quotes.toscrape.com/page/" + str(QuotesSpider.page_number) + "/"
        print(next_page)
        if QuotesSpider.page_number < 11:
            QuotesSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
