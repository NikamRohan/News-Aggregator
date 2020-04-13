import scrapy
from ..items import PoliticscrawlerItem
from news.models import PHeadline
from politicscrawler.spiders import politics_spider
from politicscrawler import pipelines

class PoliticsSpider(scrapy.Spider):
	name = "politics"
	start_urls = [
		'https://www.nytimes.com/section/politics'
	]

	def parse(self, response):
		


		#div_all_news = response.xpath("//div[@class='css-13mho3u']/ol/li/div/div")
	
		for i in range(10):
			items = PoliticscrawlerItem()
			title = response.xpath("//div[@class='css-13mho3u']/ol/li/div/div/a/h2/text()")[i].extract()
			link = "https://www.nytimes.com" + response.xpath("//div[@class='css-13mho3u']/ol/li/div/div/a/@href")[i].extract()
			img = response.xpath("//div[@class='css-13mho3u']/ol/li/div/div/a/div[@class='css-79elbk']/figure/@itemid")[i].extract()
			items["title"] = title
			items["image"] = img
			items["url"] = link
			items['source'] = 'New York Times'
			yield items
			

class EconomicSpider(scrapy.Spider):
	name = "ecopolitics"
	start_urls = [
		'https://economictimes.indiatimes.com/news/politics-nation?from=mdr'
	]

	def parse(self, response):
		


		for i in range(10):
			items = PoliticscrawlerItem()
			title = response.xpath("//section[@id='bottomContent']/section/div/h3/a/text()")[i].extract()
			link = "https://economictimes.indiatimes.com" + response.xpath("//section[@id='bottomContent']/section/div/a/@href")[i].extract()
			img = response.xpath("//section[@id='bottomContent']/section/div/a/span/img/@data-original")[i].extract()
			items["title"] = title
			items["image"] = img
			items["url"] = link
			items['source'] = 'Economic Times'
			yield items