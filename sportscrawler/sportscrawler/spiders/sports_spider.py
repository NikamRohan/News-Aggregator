import scrapy
from ..items import SportscrawlerItem
from news.models import SHeadline
from sportscrawler.spiders import sports_spider
from sportscrawler import pipelines

class SportsSpider(scrapy.Spider):
	name = "sports"
	start_urls = [
		'https://indianexpress.com/section/sports/'
	]

	def parse(self, response):
		


		div_all_news = response.xpath("//div[@class='articles']")
		i=0
		for some in div_all_news:
			items = SportscrawlerItem()
			title = some.xpath("//h2[@class='title']/a/text()")[i].extract()
			link = some.xpath("//h2[@class='title']/a/@href")[i].extract()
			s = some.xpath("//div[@class='snaps']/a/noscript")[i].extract()
			l = s.split(" ")
			img = l[3][5:-1]
			l=[]
			i+=1 
			items["title"] = title
			items["image"] = img
			items["url"] = link
			items['source'] = 'Indian Express'
			yield items

class HtimesSpider(scrapy.Spider):
	name = "Htimes"
	start_urls = [
		'https://www.hindustantimes.com/other-sports/'
	]

	def parse(self, response):
		


		div_all_news = response.xpath("//section[@class='container']/div[@class='news-area more-news-section']/div/div[@class='col-sm-7 col-md-8 col-lg-9']/div[@id='scroll-container']/ul[@class='latest-news-morenews more-latest-news more-separate newslist-sec']/li/div")
		i=0
		j=0
		for some in div_all_news:
			items = SportscrawlerItem()
			title = some.xpath("//div[@class='media-body']/div/a/text()")[i].extract()
			link = some.xpath("//div[@class='media-body']/div/a/@href")[i].extract()
			if i<3:
				img = some.xpath("//div[@class='media-left']/div/a/img/@src")[i].extract()
			else:
				img = some.xpath("//div[@class='media-left']/a/img/@src")[j].extract()
				j+=1
			i+=1 
			items["title"] = title
			items["image"] = img
			items["url"] = link
			items['source'] = 'Hindustan'
			yield items
