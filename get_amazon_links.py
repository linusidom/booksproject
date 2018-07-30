from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import urllib
import json

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','booksproject.settings')
import sys

import django
django.setup()

from booksproject import settings
from books.models import Book







def searchamazon(url):
		
	kw = ['Series', 'Publisher', 'ISBN-10']

	print(url)
	url = Request(url)
	url.add_header('User-Agent', 'Mozilla/5.0')
	
	with urlopen(url) as f:
		dataset = f.read()
		page_soup = soup(dataset, 'html.parser')
		# print(page_soup)
		for line in page_soup.findAll('h2'):
			# print('Finding H2')
			if line.text == 'Product details':
				# print('Found Product Detaila')
				for item in line.findNext('div',{'class': 'content'}):
					# print('Found Content')
					content = soup(str(item), 'html.parser')
					for data in content.findAll('li'):
						# print('Found List Item')
						if any(variable in data.text for variable in kw):
							print(data.text)



# SEarch Google for Amazon Links
f = open('googlebooksearchmanent','w')

with open('LOTR') as fileopen:
  books = fileopen.readlines()
  for book in books:
    book = book.strip()
    book = book.replace(' ','+')
    url = "curl --header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36' 'https://www.google.com/search?q=amazon+"
    url = url + book + '\''

    print url

    output = os.popen(url).read()
    page_soup = soup(output, 'html.parser')

    for line in page_soup.findAll('h3',{'class':'r'}):
      for item in line.findAll('a', href=True):
        print book + '@' +item['href']
        f.write(book + '@' +item['href']+'\n')
        break
      break
f.close()


# Search Amazon for Pub Date
with open('googlebooksearch') as g:
	books = g.readlines()

	for book in books:
		amazonlink = book.split('@')[1]
		searchamazon(amazonlink)
	


