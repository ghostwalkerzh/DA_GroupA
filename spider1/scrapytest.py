import scrapy
class NewSpider(scrapy.Spider):
    name = "new spider"
    start_urls = ['http://172.18.58.80/index.html']

    def parse(self, response):
        xpath_selector = '//img'
        for x in response.xpath(xpath_selector):
            newsel = '@src'
            yield {'Image Link': x.xpath(newsel).extract_first(), }
