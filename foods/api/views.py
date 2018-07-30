from rest_framework import generics
from foods.api.models import FoodSerializer
from foods.models import Food

class FoodRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
	lookup ='pk'
	serializer_class = FoodSerializer
	queryset = Food.objects.all()