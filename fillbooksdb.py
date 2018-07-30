from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import urllib
import json

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','booksproject.settings')

import django
django.setup()

from booksproject import settings
from books.models import Book



from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import requests
import time

def populate():
	with open('booksranked') as f:
		books = f.readlines()
		for book in books:
			title_author = book.split('%')[0]
			title = title_author.split('@')[0]
			author = title_author.split('@')[1]
			occurrences = book.split('%')[1]
			Book.objects.get_or_create(title=title,
										author=author,
										occurrences=occurrences)
	return None

def delete_all_records():
	Book.objects.all().delete()
	return None

def get_amazon_link(title, author):
	title = title.replace(' ','+')
	author = author.replace(' ','+')
	url = 'https://www.google.com/search?q=amazon+paperback+'+title+'+'+author
	print(url)
	url = Request(url)
	url.add_header('User-Agent', 'Mozilla/5.0')

	with urlopen(url) as f:
		data = f.readlines()

		page_soup = soup(str(data), 'html.parser')
		for line in page_soup.findAll('h3',{'class':'r'}):
			for item in line.findAll('a', href=True):
				item = item['href'].split('=')[1]
				item = item.split('&')[0]
				print(item)
				return item


def get_wiki_link(title, author):
	title = title.replace(' ','+')
	author = author.replace(' ','+')
	url = 'https://www.google.com/search?q=wiki+novel+book+'+title+'+'+author
	print(url)
	url = Request(url)
	url.add_header('User-Agent', 'Mozilla/5.0')

	with urlopen(url) as f:
		data = f.readlines()

		page_soup = soup(str(data), 'html.parser')

		for line in page_soup.findAll('h3',{'class':'r'}):
			for item in line.findAll('a', href=True):
				item = item['href'].split('=')[1]
				item = item.split('&')[0]
				return item

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

# delete_all_records()
# populate()



# books = Book.objects.filter(pubdate=None)
# for book in books:
# 	title = str(book.title)
# 	author = str(book.author)
# 	amazon_result = get_amazon_link(title, author)
# 	time.sleep(5)
# 	wiki_result = get_wiki_link(title, author)    
# 	time.sleep(5)
# 	pub_auth = pollamazon(amazon_result)
# 	releasedate = pub_auth[0].strip()
# 	author = pub_auth[1].strip()
# 	Book.objects.filter(title=book).update(pubdate = releasedate,
# 											wikilink=wiki_result,
# 											amazonlink = amazon_result)








