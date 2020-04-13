import scrapy
from ..items import EconomycrawlerItem
from news.models import EHeadline
from economycrawler.spiders import economy_spider
from economycrawler import pipelines

class EconomySpider(scrapy.Spider):
	name = "economy"
	start_urls = [
		'https://economictimes.indiatimes.com/markets/stocks/news'
	]

	def parse(self, response):
		


		div_all_news = response.xpath("//div[@class='eachStory']")
		i=0
		for some in div_all_news:
			items = EconomycrawlerItem()
			title = some.xpath("//h3/a/meta/@content")[i].extract()
			link = "https://economictimes.indiatimes.com" + some.xpath("//h3/a/@href")[i].extract()
			img = some.xpath("//a/span[@class='imgContainer']/img/@data-original")[i].extract()
			i+=1 
			items["title"] = title
			items["image"] = img
			items["url"] = link
			items['source'] = 'Economic Times'
			yield items
			#if i==10:
			#	break

class ExpressSpider(scrapy.Spider):
	name = "express"
	start_urls = [
		'https://indianexpress.com/section/business/economy/'
	]

	def parse(self, response):
		


		div_all_news = response.xpath("//div[@class='articles']")
		i=0
		for some in div_all_news:
			items = EconomycrawlerItem()
			title = some.xpath("//h2/a/text()")[i].extract()
			link = some.xpath("//h2/a/@href")[i].extract()
			s = some.xpath("//div/a/noscript")[i].extract()
			l = s.split('"')
			img = l[5]
			i+=1
			l=[] 
			items["title"] = title
			items["image"] = img
			items["url"] = link
			items["source"] = 'Indian Express'
			yield items
			#if i==10:
			#	break