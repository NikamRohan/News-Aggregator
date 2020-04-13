import scrapy
from ..items import LifestylecrawlerItem
from news.models import LHeadline
from lifestylecrawler.spiders import lifestyle_spider
from lifestylecrawler import pipelines

class LifestyleSpider(scrapy.Spider):
	name = "lifestyle"
	start_urls = [
		'https://indianexpress.com/section/lifestyle/'
	]

	def parse(self, response):
		


		#div_all_news = response.xpath("//div[@class='css-13mho3u']/ol/li/div/div")
	
		for i in range(18):
			items = LifestylecrawlerItem()
			title = response.xpath("//div[@class='nation']/div[@class='articles']/h2/a/text()")[i].extract()
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

class HealthSpider(scrapy.Spider):
	name = "health"
	start_urls = [
		'https://www.foxnews.com/health'
	]

	def parse(self, response):
		


		#div_all_news = response.xpath("//div[@class='css-13mho3u']/ol/li/div/div")
	
		for i in range(12):
			items = LifestylecrawlerItem()
			title = response.xpath("//div[@class='content article-list']/article/div[@class='info']/header/h4/a/text()")[i].extract()
			link = 'https://www.foxnews.com' + response.xpath("//div[@class='content article-list']/article/div[@class='m']/a/@href")[i].extract()
			img = img = response.xpath("//div[@class='content article-list']/article/div[@class='m']/a/img/@src")[i].extract()
			items["title"] = title
			items["image"] = img
			items["url"] = link
			items['source'] = 'Fox News'
			yield items
			