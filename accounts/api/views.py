from rest_framework import generics
from accounts.api.models import UserModelSerializer
from accounts.models import UserModel

class UserModelRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
	lookup ='pk'
	serializer_class = UserModelSerializer
	queryset = UserModel.objects.all()