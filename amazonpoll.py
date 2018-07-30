from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, Request
import time


def pollamazon(url):
	url = Request(url)
	url.add_header('User-Agent', 'Mozilla/5.0')

	publisher = '1111111111'
	author = '1111111111'

	with urlopen(url) as f:
		data = f.readlines()

		page_soup = soup(str(data), 'html.parser')
		for line in page_soup.findAll('li'):
			# print(line)
			if 'Publisher:' in line.text:
				print(line.text)
				publisher = line.text
		for line in page_soup.findAll('a', {'class': 'contributorNameID'}):
			# print(line.text)
			author = line.text
		if author == '1111111111':
			# print('Author not found')
			for line in page_soup.findAll('span', {'class': 'author notFaded'}):
				author = line.a.text
		return publisher, author

am = open('amazonresults','w')

with open('amazonbookslinks','r') as a:
	links = a.readlines()

	for lines in links:
		book = lines.split('@')[0]
		link = lines.split('@')[1]
		print(link)
		time.sleep(5)
		result = pollamazon(link)
		publisher = result[0].strip()
		author = result[1].strip()
		link = link.strip()
		msg = book +'@'+ author +'@'+ publisher +'@'+ link + '\n'
		print(msg)
		am.write(msg)

am.close()

