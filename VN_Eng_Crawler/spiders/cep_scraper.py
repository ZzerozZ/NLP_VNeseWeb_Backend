import scrapy
from bs4 import BeautifulSoup as bs
from get_data import get_data
import os


class CEPSpider(scrapy.Spider):
	name = "CEP_Spider"
	category = ""

	def start_requests(self):
		# List of category's url:
		urls = [
			"http://cep.com.vn/news/xa-hoi",
			"http://cep.com.vn/news/the-gioi",
			"http://cep.com.vn/news/the-thao",
			"http://cep.com.vn/news/giai-tri",
			"http://cep.com.vn/news/giao-duc",
			"http://cep.com.vn/news/co-khi-che-tao",
			"http://cep.com.vn/news/xay-dung-kien-truc",
			"http://cep.com.vn/news/ha-tang-ky-thuat",
			"http://cep.com.vn/news/nong-lam-ngu-nghiep",
			"http://cep.com.vn/news/y-te-suc-khoe",
			"http://cep.com.vn/news/cong-nghe-thong-tin",
			"http://cep.com.vn/news/dien-dien-tu",
			"http://cep.com.vn/news/facebook",
			"http://cep.com.vn/news/google",
			"http://cep.com.vn/news/khoa-hoc-nghien-cuu",
			"http://cep.com.vn/news/kinh-doanh",
			"http://cep.com.vn/news/ke-toan-kiem-toan",
			"http://cep.com.vn/news/tai-chinh-ngan-hang",
			"http://cep.com.vn/news/luat-kinh-te",
			"http://cep.com.vn/news/ky-nang",
		]
		for url in urls:
			# Create new category if not exist:
			self.category = url.split('/')[-1]
			if not os.path.isdir("./" + self.category):
				os.makedirs("./" + self.category)
			# Parse:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		result = []  # temporary list<string> for save all data crawled
		names = []  # temporary string for save name of article
		# Get a part of html code where include article link/url:
		temp = response.xpath("/html[1]/body[1]/section[1]/div[1]/div[1]/div[1]/div[2]").extract()

		# Get articles:
		for i in xrange(len(temp)):
			# New beautifulsoup:
			soup = bs(temp[i])
			links = soup.find_all("a")
			skip = False  # Skip url which already exist in url list

			# Crawl all urls one by one:
			for link in links:
				if skip is False:
					names.append(link.get('href').split("/")[-1].replace(".html", ""))  # Add article's name
					result.append(get_data(link.get('href')))   # Add article data
				skip = not skip

		# Write article's data in Vietnamese to files:
		for i in xrange(len(result)):
			with open("./" + self.category + "/" + names[i] + ".VIE", 'wb') as f:
				f.write(result[i][0])
				self.log('Saved file ' + names[i] + ".VIE")

		# Write article's data in English to files:
		for i in xrange(len(result)):
			with open("./" + self.category + "/" + names[i] + ".ENG", 'wb') as f:
				f.write(result[i][1])
				self.log('Saved file ' + names[i] + ".ENG")
