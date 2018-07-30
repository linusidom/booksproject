from rest_framework import serializers
from tagr.models import Post

class PostSerializer(serializers.ModelSerializer):
	class Meta():
		model = Post