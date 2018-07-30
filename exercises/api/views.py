from rest_framework import generics
from exercises.api.models import ExerciseSerializer
from exercises.models import Exercise

class ExerciseRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
	lookup ='pk'
	serializer_class = ExerciseSerializer
	queryset = Exercise.objects.all()