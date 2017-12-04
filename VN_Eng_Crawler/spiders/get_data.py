from bs4 import BeautifulSoup as bs
from urllib2 import urlopen


def get_data(html):
	html = urlopen(html).read()  # Read page's source
	soup = bs(html)  # Create new bs4

	# Get Vietnamese text:
	vietnamese = soup.find("div", id="vietnamese").text.encode('utf-8')
	# Get English text:
	english = soup.find("div", id="english").text.encode('utf-8')

	# Return:
	return [vietnamese, english]


# temp = get_data("http://cep.com.vn/cong-viec-phu-cua-nhung-ga-khong-lo-cong-nghe"
#                 "-trung-quoc-giup-bac-kinh-theo-doi-nguoi-dung-5471.html")
# print temp
