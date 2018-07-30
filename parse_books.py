from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import re


def searchurl(url):
	print("\n\nSouping", url)
	url = Request(url)
	url.add_header('User-Agent', 'Mozilla/5.0')
	with urlopen(url) as response:
		html = response.read()
	page_soup = soup(html, 'html.parser')

	return page_soup

# f = open('./books.txt','a')

# ##!!!! Done Properly
# page_soup = searchurl('http://www.businessinsider.com/100-books-everyone-should-read-amazon-goodreads-2015-3')
# for line in page_soup.findAll('ol'):
# 	result = line.findAll('li')
# 	for items in result:
# 		items = items.text
# 		items = items.replace('"','')
# 		items = items.strip()
# 		msg = items + '\n'
# 		print(items)
# 		f.write(msg)

	

# #!!!!! Done Properly
# page_soup = searchurl('https://www.listchallenges.com/bbcs-top-100-books-you-need-to-read-before-you-die/vote')
# for line in page_soup.findAll('div',{'class':'item-name'}):
# 	line.findNext('div')
# 	result = line.contents[-1]
# 	result = result.replace('\t','').replace('\n','')
# 	# result = result.replace('\t', '').replace('\n','')
# 	print(result)
# 	f.write(result)


# # !!!!!DONE
# page_soup = searchurl('https://www.realsimple.com/work-life/entertainment/amazon-100-book-list')
# for line in page_soup.find_all('p'):
# 	result = line.text
# 	result = result.split('.')
# 	if len(result) > 1:
# 		result = result[1].lstrip()
# 		result = result.replace(', by',' by')
# 		msg = result + '\n'
# 		print(msg)
# 		f.write(msg)


# # !!!!!DONE
# page_soup = searchurl('https://archive.nytimes.com/www.nytimes.com/library/books/072098best-novels-list.html')
# for line in page_soup.find_all('p'):
# 	result = line.text
# 	result = re.sub(r'[0-9]+(\. )','',result)
# 	result = result.replace('," ',' by ').replace('&apos;','\'')
# 	result = result.replace('),',' by').replace('"','').replace('(','')
# 	if ' by' in result:	
# 		msg = result.lstrip() + '\n'
# 		# msg = result
# 		f.write(msg)

# # !!!!!Done
# page_soup = searchurl('https://www.abebooks.com/books/100-books-to-read-in-lifetime/index.shtml')
# for line in page_soup.findAll('div',{'class':'featured-item'}):
# 	title = line.h3.text
# 	author = line.find('div',{'class':'item-subheading'}).text
# 	title = title.strip()
# 	author = author.strip()
# 	result = title + ' ' + author
# 	msg = result + '\n'
# 	f.write(msg)
	
# # Need to manually Add 'The Young Mans Guide by William Alcott'
# # Need to manually Add 'The  Federalist  Papers  by  Alexander  Hamilton, John  Jay, and  James  Madison'
# page_soup = searchurl('https://www.artofmanliness.com/articles/100-must-read-books-the-essential-mans-library/')
# for line in page_soup.findAll('p'):
# 	result = line.text
# 	result = result.replace('\n','')
# 	result = result.strip()
# 	if len(result) < 83 and 'Amazon' not in result and 'Because he' not in result and 'Show Comments' and 'Written by:' not in result and 'A Manly Guest' not in result and 'Last Updated' not in result and 'To see a list' not in result:
# 		print(result)
# 		msg = result + '\n'
# 		f.write(msg.lstrip())

# # !!!!!!!!DONE
# page_soup = searchurl('http://www.modernlibrary.com/top-100/100-best-novels/')
# for line in page_soup.findAll('div', {'class': 'row'}):
# 	result = line.li.text
# 	result = result.lower().title()
# 	result = result.replace('By', 'by')
# 	print(result)
# 	msg = result + '\n'
# 	f.write(msg)


# # !!!!!!!!DONE
# page_soup = searchurl('http://www.harvard.com/ajax/top100/')
# for line in page_soup.findAll('div', {'class':'infobox_interior'}):
# 	result_title = line.find('h2')
# 	author = line.find('div',{'class':'author'})
# 	if author:
# 		print(result_title.text +' '+ author.text)
# 		msg = result_title.text +' '+ author.text + '\n'
# 		f.write(msg)

# # !!!!!!!!DONE
# page_soup = searchurl('https://www.theguardian.com/books/2015/aug/17/the-100-best-novels-written-in-english-the-full-list')
# for line in page_soup.findAll('div',{'class':'content__article-body from-content-api js-article__body'}):
# 	for para in line.findAll('p'):
# 		if re.search(r'^[0-9]', str(para.text)):
# 			result = re.sub(r'^[0-9]+(.)', '', para.text)
# 			print(result.lstrip())
# 			msg = result.lstrip() + '\n'
# 			f.write(msg)

# # !!!!!!DONE
# page_soup = searchurl('https://www.librarything.com/bookaward/Newsweek%27s+Top+100+Books%3A+The+Meta-List')
# for line in page_soup.find('table',{'class':'worksinseries'}):
# 	result = line.text
# 	if '2009' in result:
# 		result = result.split('2009')[0]
# 		msg = result + '\n'
# 		f.write(msg)
# 	else:
# 		msg = result + '\n'
# 		f.write(msg)

# f.close()

# albums
# Artist, Title, Year, Amazon Link, Wiki Link


# f = open('musicalbums','w')

# !!!!!!!!!!!!DONE
# page_soup = searchurl('https://www.discogs.com/lists/The-Guardian-100-Best-Albums-Ever/10967?page=1&limit=100')
# for line in page_soup.findAll('div',{'class':'listitem_mobile_header'}):
# 	result = line.h3.text
# 	result.strip()
# 	print(result)


# # !!!!DONE but has to be an easier way to unpack the <td>
# page_soup = searchurl('http://www.popvortex.com/music/100-greatest-albums/')
# for line in page_soup.findAll('tr'):
# 	one = line.findNext('td')
# 	two = one.findNext('td')
# 	three = two.findNext('td')
# 	four = three.findNext('td')
# 	five = four.findNext('td')
# 	msg = two.text+'@'+three.text+'@'+four.text.strip()
# 	print(msg)
# 	# f.write(msg)
# # f.close()

# # !!!!!!DONE but has some formatting challenges - need to find a way to get the data in the same line
# for i in range(1,11):
# 	url = 'https://www.besteveralbums.com/thechart.php?c=5&cbid=0&f=&fv=&orderby=Rank&sortdir=asc&page='+str(i)
# 	print(url)
# 	page_soup = searchurl(url)
# 	for line in page_soup.findAll('a',{'class': 'nav2emph bigger'}):
# 		print(line.text)

# # https://www.rollingstone.com/music/music-lists/500-greatest-albums-of-all-time-156826/?list_page=9
# # !!!!!!DONE 100-50
# page_soup = searchurl('https://www.rollingstone.com/music/music-lists/500-greatest-albums-of-all-time-156826/?list_page=9')
# for line in page_soup.findAll('h3',{'class':'c-list__title t-bold'}):
# 	print(line.text.strip())
# # https://www.rollingstone.com/music/music-lists/500-greatest-albums-of-all-time-156826/?list_page=10
# page_soup = searchurl('https://www.rollingstone.com/music/music-lists/500-greatest-albums-of-all-time-156826/?list_page=10')
# for line in page_soup.findAll('h3',{'class':'c-list__title t-bold'}):
# 	print(line.text.strip())


# !!!!!!DONE
# page_soup = searchurl('https://www.billboard.com/charts/greatest-billboard-200-albums')
# for line in page_soup.findAll('div',{'class':'chart-row__title'}):
# 	album = line.find('h2')
# 	try:
# 		artist = line.a.text
# 	except:
# 		artist = line.find('span')
# 		artist = artist.text
# 	print(album.text.strip(), artist.strip())

# # !!!!!!!DONE
# page_soup = searchurl('https://www.digitalmusicnews.com/2017/02/16/100-best-selling-albums-all-time/')
# for line in page_soup.findAll('section',{'class': 'cb-entry-content entry-content clearfix'}):
# 	for item in line.findAll('p'):
# 		print(item.text)

# # !!!!!DONE
# page_soup = searchurl('http://www.nme.com/photos/the-500-greatest-albums-of-all-time-100-1-1426116')
# for line in page_soup.findAll('div',{'itemprop':'description'}):
# 	title = line.find('b')
# 	print(title.text)


# !!!!DONE - Copy the list and format it
# page_soup = searchurl('https://www.stereogum.com/1395702/entertainment-weeklys-100-greatest-albums-ever/franchises/list/')


# Need to figure out Remote Disconnect Error
# for i in range(2,12):
	# page_soup = searchurl('https://247wallst.com/special-report/2018/04/17/100-best-albums-of-all-time/'+str(i)+'/')
	# for line in page_soup.findAll('div'):
	# 	print(line)

# page_soup = searchurl('http://absoluteradio.co.uk/competitions/100-greatest-albums/results.html')







