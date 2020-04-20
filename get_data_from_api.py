import requests
import json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','booksproject.settings')

import django
django.setup()

from books.models import Book
from albums.models import Album

with open('./books.json') as f:
	lines = f.readlines()
	lines = json.loads(lines[0])

# try:
for line in lines:
	# print('Line', line)
	Book.objects.get_or_create(
		title=line['fields']['title'],
		author=line['fields']['author'],
		pubdate=line['fields']['pubdate'],
		wikilink=line['fields']['wikilink'], 
		occurrences=line['fields']['occurrences'], 
		amazonlink=line['fields']['amazonlink']
		)

		# print('Printing',
		# 	line['fields']['title'],
		# 	line['fields']['artist'],
		# 	line['fields']['year'],
		# 	line['fields']['wikilink'], 
		# 	line['fields']['occurrences'], 
		# 	line['fields']['amazonlink']
		# 	)
# except:
# 	print("can't print")