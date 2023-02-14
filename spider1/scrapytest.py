import scrapy
#Step 8, 9, 10
class NewSpider(scrapy.Spider):
    name = "new spider"
    start_urls = ['http://172.18.58.80/hr2/']

    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {'Image Link': x.xpath(newsel).extract_first(), }

        page_selector = '.next a ::attr(href)'
        next_page = response.css(page_selector).extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

#cd to spider1 first
#Command to save file: scrapy runspider scrapytest.py -o filename.json -t json

