from rest_framework import serializers
from albums.models import Album

class AlbumSerializer(serializers.ModelSerializer):
	class Meta():
		model = Album
		fields = ['pk','title','artist','year','occurrences']