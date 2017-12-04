from bs4 import BeautifulSoup as bs

html = open("test.txt", "r").read()
soup = bs(html)
links = soup.find_all("a")
skip = False

for link in links:
	if skip is False:
		result.append(link.get('href'))
	skip = not skip
print 'AAA'