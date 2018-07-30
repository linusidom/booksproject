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






##################
# Wiki lookup with Pandas Lsit
##################


def searchpubdate(booktitle):
	booktitle = booktitle.replace(' ','_')
	url = 'https://en.wikipedia.org/wiki/'+booktitle	
	author = '11111111'
	pubdate = '11111111'
	try:
		print(url)
		with urlopen(url) as f:
			data = f.read()
	except:
		print('Entering novel append Case')
		# url = url+'_(novel)'
		print(url+'_(novel)')
		with urlopen(url+'_(novel)') as f:
			data = f.read()

	page_soup = soup(data, 'html.parser')
	if page_soup.find(text='Publication date'):
		pubdate = page_soup.find(text='Publication date').findNext('td').text
	elif page_soup.find(text='Published'):
		pubdate = page_soup.find(text='Published').findNext('td').text
	elif page_soup.find(text='Date'):
		pubdate = page_soup.find(text='Date').findNext('td').text
	
	if page_soup.find(text='Author'):
		author = page_soup.find(text='Author').findNext('td').text
	elif page_soup.find(text='Created'):
		author = page_soup.find(text='Created').findNext('td').text
	elif page_soup.find(text='Created by'):
		author = page_soup.find(text='Created by').findNext('td').text
		
	elif page_soup.find(text='Creators'):
		author = page_soup.find(text='Creators').findNext('td').text
	
	# Case that Wiki page exists but it doesn't have an author
	elif author == '11111111':
		try:
			print('Entering Else Author Case')
			# url = url+'_(novel)'
			print(url+'_(novel)')
			with urlopen(url+'_(novel)') as f:
				data = f.read()
		except:
			print('Entering Else Author Case with book')
			# url = url+'_(book)'
			print(url+'_(book)')
			with urlopen(url+'_(book)') as f:
				data = f.read()
		# else: 
		# 	return author, pubdate, url

		page_soup = soup(data, 'html.parser')
		if page_soup.find(text='Author'):
			author = page_soup.find(text='Author').findNext('td').text

		if page_soup.find(text='Publication date'):
			pubdate = page_soup.find(text='Publication date').findNext('td').text

		if page_soup.find(text='Published'):
			pubdate = page_soup.find(text='Published').findNext('td').text

	return author, pubdate, url

	

with open('pandasranked','r') as f:
	titles = f.readlines()

	for title in titles:
		if '"' in title:
			book = title.split('",')[0]
			book_title = book.strip()
			book_title = book_title.replace('"','')
			occurrences = title.split('",')[1]
			print(book_title, occurrences)
		else:
			book = title.split(',')[0]
			book_title = book.strip()
			occurrences = title.split(',')[1]
			print(book_title, occurrences)

		# entry = Book.objects.get_or_create(title=book_title,occurrences=occurrences)[0]

		shakespeare = ['Hamlet', 'Romeo and Juliet', 'Macbeth', 'King Lear', 'Othello']

		if book_title in shakespeare:
			continue

		match = Book.objects.filter(title__iexact = book_title)
		if not match:
			result = searchpubdate(book_title)
			print(book_title, result[0], result[1], result[2])
			entry = Book.objects.get_or_create(title=book_title,
												author = result[0],
												pubdate = result[1],
												wikilink = result[2],
												occurrences=occurrences)[0]
