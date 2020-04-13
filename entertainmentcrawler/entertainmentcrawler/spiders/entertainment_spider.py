import scrapy
from ..items import EntertainmentcrawlerItem
from news.models import ENHeadline
from entertainmentcrawler.spiders import entertainment_spider
from entertainmentcrawler import pipelines

class EntertainmentSpider(scrapy.Spider):
	name = "entertainment"
	start_urls = [
		'https://variety.com/'
	]

	def parse(self, response):
		


		for i in range(13):
			items = EntertainmentcrawlerItem()
			title = response.xpath("//div[@class='l-river__content']/ul/li/article/header/h3/a/text()")[i].extract()
			link =  response.xpath("//div[@class='l-river__content']/ul/li/article/figure/a/@href")[i].extract()
			img = response.xpath("//div[@class='l-river__content']/ul/li/article/figure/a/img/@data-src")[i].extract()
			items["title"] = title
			items["image"] = img
			items["url"] = link
			items['source'] = 'Variety'
			yield items

class EntrtnmentSpider(scrapy.Spider):
	name = "entrtnment"
	start_urls = [
		'https://indianexpress.com/section/entertainment/'
	]

	def parse(self, response):
		


		for i in range(17):
			items = EntertainmentcrawlerItem()
			title = response.xpath("//div[@class='nation']/div[@class='articles']/div[@class='title']/a/text()")[i].extract()
			link =  response.xpath("//div[@class='nation']/div[@class='articles']/div[@class='snaps']/a/@href")[i].extract()
			s = response.xpath("//div[@class='nation']/div[@class='articles']/div[@class='snaps']/a/noscript")[i].extract()
			l = s.split('"')
			img = l[5]
			l=[]
			items["title"] = title
			items["image"] = img
			items["url"] = link
			items['source'] = 'Indian Express'
			yield items