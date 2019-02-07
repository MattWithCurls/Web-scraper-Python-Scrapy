# -*- coding: utf-8 -*-
import scrapy


class WormSpider(scrapy.Spider):
    name = 'worm'
    allowed_domains = ['netelek.co.za']
    start_urls = ['https://netelek.co.za/']

    def parse(self, response):
        title = response.xpath("//").extract()
        yield{''}
