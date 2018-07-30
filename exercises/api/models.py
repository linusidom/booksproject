from rest_framework import serializers
from exercises.models import Exercise

class ExerciseSerializer(serializers.ModelSerializer):
	class Meta():
		model = Exercise
		fields = ['user','minutes','calories_burned','exercise_type']