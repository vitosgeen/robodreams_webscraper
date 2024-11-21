import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    current_page = 0
    max_pages = 1

    custom_settings = {
        "FEEDS_URI": "quotes.json",
        "FEEDS_FORMAT": "json",
        "DOWNLOAD_DELAY": 1,
    }

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").extract_first(),
                "author": quote.css("span small.author::text").extract_first(),
                "tags": quote.css("div.tags a.tag::text").extract(),
            }

        next_page = response.css("li.next a::attr(href)").extract_first()
        if next_page is not None and self.current_page < self.max_pages:
            self.current_page += 1
            yield response.follow(next_page, self.parse)
