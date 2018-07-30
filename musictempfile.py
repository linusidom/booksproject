f = open('musictempfile')

for line in f.readlines():
	artist = line.split('@')[0]
	album = line.split('@')[1]
	print album.strip() +'@'+ artist.strip()
f.close()