import scrapy
from scrapy import Selector,Request
from myCrawling.items import MycrawlingItem

class ZhaopinSpider(scrapy.Spider):
    name = "zhaopin"
    allowed_domains = ["zhaopin.com"]
    start_urls = ["https://sou.zhaopin.com/?jl=530&kw=java&p=1"]
    def start_requests(self):
        for i in range(1,21):
            yield Request(url=f'https://sou.zhaopin.com/?jl=576&kw=java&p={i}')

    custom_settings = {
        'ITEM_PIPELINES': {'myCrawling.pipelines.MycrawlingPipeline': 300}
    }

    def parse(self, response):
        sel=Selector(response)
        lists=sel.css("#positionList-hook > div > div.joblist-box__item.clearfix")
        for item in lists:
            mydata=MycrawlingItem()
            mydata["job"]=item.css("div.iteminfo__line.iteminfo__line1 > div.iteminfo__line1__jobname > span::attr(title)").extract_first()
            mydata["city"]=item.css("div.iteminfo__line.iteminfo__line2 > div.iteminfo__line2__jobdesc > ul > li:nth-child(1)::text").extract_first()
            mydata["workage"]=item.css("div.iteminfo__line.iteminfo__line2 > div.iteminfo__line2__jobdesc > ul > li:nth-child(2)::text").extract_first()
            mydata["education"]=item.css("div.iteminfo__line.iteminfo__line2 > div.iteminfo__line2__jobdesc > ul > li:nth-child(3)::text").extract_first()
            mydata["skill"]=item.css("div.iteminfo__line.iteminfo__line3 > div.iteminfo__line3__welfare div::text").extract()
            mydata["salary"]=item.css("div.iteminfo__line.iteminfo__line2 > div.iteminfo__line2__jobdesc > p::text").extract_first()

            yield mydata