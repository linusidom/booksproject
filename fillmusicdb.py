from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import urllib
import json

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','booksproject.settings')

import django
django.setup()

from booksproject import settings
from albums.models import Album
import time

# Populate the DB with the initial data set
	
def populate():
	with open('musicranked') as f:
		albums = f.readlines()
		for album in albums:
			title_artist = album.split('%')[0]
			title = title_artist.split('@')[0]
			artist = title_artist.split('@')[1]
			occurrences = album.split('%')[1]
			print(title_artist)
			Album.objects.get_or_create(title=title,
										artist=artist,
										occurrences=occurrences)
	return None

def delete_all_records():
	Album.objects.all().delete()
	return None

def get_amazon_link(title, artist):
	title = title.replace(' ','+')
	artist = artist.replace(' ','+')
	url = 'https://www.google.com/search?q=amazon+album+'+title+'+'+artist
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
				print('Google Item ', item)
				return item


def get_wiki_link(title, artist):
	title = title.replace(' ','+')
	artist = artist.replace(' ','+')
	url = 'https://www.google.com/search?q=wiki+album+'+title+'+'+artist
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
	print(url)
	url = Request(url)
	url.add_header('User-Agent', 'Mozilla/5.0')

	publisher = '1111111111'
	author = '1111111111'

	with urlopen(url) as f:
		data = f.readlines()

		page_soup = soup(str(data), 'html.parser')
		for line in page_soup.findAll('li'):
			# print(line)
			if 'Original Release Date:' in line.text:
				# print(line.text)
				publisher = line.text
		for divs in page_soup.findAll('div',{'class':'content'}):
			for line in divs.findAll('li'):
				if 'Audio CD' in line.text:
					print('Audio CD',line.text)
					publisher = line.text
		for line in page_soup.findAll('a', {'class': 'contributorNameID'}):
			# print(line.text)
			author = line.text
			print('ContrbutorID', author)
		if author == '1111111111':
			# print('Author not found')
			for line in page_soup.findAll('span', {'class':'author notFaded'}):
				author = line.a.text
				print('Author Not Faded ', author)
			if author == '1111111111':
				line = page_soup.find('a',{'id':'ProductInfoArtistLink'})
				print('Line ',line)
				if line == None:
					author = '2222222222'
				else:
					author = line.text
				print('ProductInfo ',author)
			if author == None:
				author = '2222222222'
		print(publisher, author)
		return publisher, author


def manual_update(pk,year, **kwargs):
	update = Album.objects.filter(pk=pk).update(year=year)
	return update



# delete_all_records()
# populate()



# albums = Album.objects.filter(amazonlink=None)
# for album in albums:
# 	title = str(album.title)
# 	artist = str(album.artist)
# 	amazon_result = get_amazon_link(title, artist)
# 	time.sleep(5)
# 	wiki_result = get_wiki_link(title, artist)    
# 	time.sleep(5)
# 	pub_auth = pollamazon(amazon_result)
# 	releasedate = pub_auth[0].strip()
# 	author = pub_auth[1].strip()
# 	Album.objects.filter(title=album).update(year = releasedate,
# 											wikilink=wiki_result,
# 											amazonlink = amazon_result)




f = open('backupofalbums','w')
albums = Album.objects.all()
for album in albums:
	msg = album.title+'@'+album.artist+'@'+album.year+'@'+album.wikilink+'@'+album.amazonlink+'@'+str(album.occurrences)+'\n'
	f.write(msg)
f.close()

