from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from ..items import ImageItem


class OpossumSpider(Spider):
    name = "opossum"
    allowed_domains = ["www.shutterstock.com"]
    start_urls = [
        # "http://www.shutterstock.com/portfolio/search.mhtml?gallery_username=mrsopossum&gallery_landing=1&page=1&safesearch=1&sort_method=newest"
        'http://www.shutterstock.com/portfolio/search.mhtml?searchterm=&media_type=vectors&search_cat=&searchtermx=&people_gender=&people_age=&people_ethnicity=&people_number=&color=&lang=ru&search_source=search_form&version=llv1&anyorall=all&safesearch=1&submitter=948064&photographer_name=Mrs.+Opossum&search_group=&orient=&commercial_ok=&show_color_wheel=1&sort_method=newest'
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        thumbs = hxs.select('//div[@id="grid_cells"]//a[@class="gc_thumb"]/@href').extract()
        next_page = hxs.select('//a[@id="search-results-next-button"]/@href').extract()
        if next_page:
            next_page = next_page[0]

        for thumb in thumbs:
            url = 'http://www.shutterstock.com{0}'.format(thumb)
            yield Request(url, callback=self.parse_image_page)

        if next_page:
            next_page = 'http://www.shutterstock.com{0}'.format(next_page)
            yield Request(next_page, callback=self.parse)

    def parse_image_page(self, response):
        hxs = HtmlXPathSelector(response)

        item = ImageItem()

        item['id'] = hxs.select('//span[@id="photo-id"]/text()').extract()[0]
        item['title'] = hxs.select('//div[@id="image_metadata"]/h1/text()').extract()[0]

        img_url = hxs.select('//div[@id="image_main"]//img[@class="thumb_image"]/@src').extract()[0]
        item['image_urls'] = [img_url]

        keywords = []
        kwitems = hxs.select('//div[@id="image_keyword_container"]/a/text()').extract()
        for kw in kwitems:
            keywords.append(kw)

        item['keywords'] = ','.join(keywords)

        yield item
