from django import forms
from exercises.models import Exercise

class ExerciseForm(forms.ModelForm):
	class Meta():
		model = Exercise
		fields = ['exercise_type','minutes','calories_burned','create_date']

	def __init__(self, *args, **kwargs):
		super(ExerciseForm, self).__init__(*args, **kwargs)
		self.fields['minutes'].required = False
		self.fields['calories_burned'] = False