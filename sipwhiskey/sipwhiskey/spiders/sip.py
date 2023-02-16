
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from sipwhiskey.items import SipwhiskeyItem
from scrapy.loader import ItemLoader
#https://sipwhiskey.com/collections/irish-whiskey
#https://sipwhiskey.com/collections/irish-whiskey/products/redbreast-12-year-old

class SipSpider(CrawlSpider):
    name = 'sip'
    allowed_domains = ['sipwhiskey.com']
    start_urls = ['http://sipwhiskey.com/']

    rules=(
        Rule(LinkExtractor(allow='collections',deny='products')),
        Rule(LinkExtractor(allow='products'),callback='parse_item')
        

    )

    def parse_item(self, response):
        #item = SipwhiskeyItem()
        loader = ItemLoader(item = SipwhiskeyItem() , response=response)
        loader.add_css("name","h1.title::text")
        loader.add_css("price","span.price::text")
        loader.add_css("brand","div.vendor a::text")
        
        # item['name'] = response.css('h1.title::text').get()
        # item['price'] = response.css('span.price::text').get()
        # item['brand'] = response.css('div.vendor a::text').get()
        
        yield loader.load_item()
        # yield{
        #     'name':response.css('h1.title::text').get(),
        #     'price':response.css('span.price::text').get() ,
        #     'brand':response.css('div.vendor a::text').get()
            
            
        # }
    