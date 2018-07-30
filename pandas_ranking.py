from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import re


# Cleanup
# Cleanup the original list
# f = open('books.txt', 'r')
# w = open('tempfiletwo', 'w')
# w.write('Title@Author\n')
# f = f.readlines()
# for line in f:
# 	line  = line.lower()
# 	line = line.title()
# 	if ' (' in line:
# 		line = line.split(' (')
# 		line = line[0]
# 	if ' By' in line:
# 		line = line.split(' By')
# 		output = line[0].strip() + '@' + line[1].strip() + '\n'
# 		w.write(output.strip()+ '\n')
# 	else:
# 		w.write(line.strip() + '\n')
# w.close()

# import pandas as pd

# pd.options.display.max_rows = 1200

# df = pd.read_csv('tempfiletwo', delimiter='@')
# print(df.head())

# df2 = df['Title'].value_counts()
# df2.to_csv('pandasrankedtwo', sep='@')




import pandas as pd


def books_ranking():
	t = open('bookstempfile','w')
	t.write('Title@Author\n')
	with open('books.txt') as f:
		books = f.readlines()
		for book in books:
			if '\'s' not in book:
				book = book.title()
				t.write(book)
			else:
				t.write(book)
	t.close()

	df = pd.read_csv('bookstempfile', delimiter='#')
	print(df.head())

	df2 = df['Title@Author'].value_counts()
	df2.to_csv('booksranked', sep='%')

def music_ranking():
	t = open('musictempfile','w')

	with open('musicalbums') as f:
		albums = f.readlines()
		for album in albums:
			if '\'s' not in album and '\'t' not in album and 'II' not in album and 'III' not in album and 'IV' not in album:
				album = album.title()
				t.write(album)
			else:
				t.write(album)
	t.close()

	df = pd.read_csv('musictempfile', delimiter='#')
	print(df.head())

	df2 = df['Title@Album'].value_counts()
	df2.to_csv('musicranked', sep='%')

books_ranking()