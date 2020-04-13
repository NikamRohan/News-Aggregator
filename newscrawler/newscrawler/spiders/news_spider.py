import scrapy
from ..items import NewscrawlerItem
from news.models import Headline
from newscrawler.spiders import news_spider
from newscrawler import pipelines

class NewsSpider(scrapy.Spider):
	name = 'news'
	start_urls=[
		'https://techcrunch.com/'
	]

	def parse(self, response):

		div_all_news =  response.xpath("//div[@class='river river--homepage']/div[@class='post-block post-block--image post-block--unread']")
		i=0
		for some in div_all_news:
			items = NewscrawlerItem()
			title =  some.xpath("//header[@class='post-block__header']/h2/a/text()")[i].extract()
			title = title[5:]
			title = title[:-3]
			link = some.xpath("//header[@class='post-block__header']/h2/a/@href")[i].extract()
			img = some.xpath("//footer[@class='post-block__footer']/figure/a/img/@src")[i].extract()
			i+=1
			items['title'] = title
			items['image'] = img
			items['url'] = link
			items['source'] = 'Techcrunch'
			yield items
			#if i==12:
			#	break

class TechSpider(scrapy.Spider):
	name = 'technews'
	start_urls=[
		'https://www.theverge.com/tech'
	]

	def parse(self, response):

		
		div_all_news =  response.xpath("//div[@class='c-compact-river']/div/div")
		i=0
		for some in div_all_news:
			items = NewscrawlerItem()
			title =  some.xpath("//div/h2/a/text()")[i].extract()
			link = some.xpath("//div/h2/a/@href")[i].extract()
			s = some.xpath("//a/div/noscript")[i].extract()
			l = s.split('"')
			img = l[3]
			i+=1
			l=[]
			items['title'] = title
			items['image'] = img
			items['url'] = link
			items['source'] = 'The Verge'
			yield items
			if i==12:
				break
