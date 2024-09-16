import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import DOMAIN, NAME, URL


class PepSpider(scrapy.Spider):
    name = NAME
    allowed_domains = [DOMAIN]
    start_urls = [URL]

    def parse(self, response):
        index_tag = response.css('section#numerical-index')
        pep_links = index_tag.css('a::attr(href)').getall()
        for link in pep_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        data = {
            'number': response.css(
                'li:contains("PEP Index") + li::text').get().split(' ')[1],
            'name': response.css('h1.page-title::text').get().split('– ')[1],
            'status': response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get(),
        }
        yield PepParseItem(data)
