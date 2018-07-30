from rest_framework import generics
from tagr.api.models import PostSerializer
from tagr.models import Post

class PostRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
	lookup ='pk'
	serializer_class = PostSerializer
	queryset = Post.objects.all()