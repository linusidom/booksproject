from django import forms
from exercises.models import Exercise

class ExerciseForm(forms.ModelForm):
	class Meta():
		model = Exercise
		fields = ['exercise_type','minutes','calories_burned','create_date']
