from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
import datetime
User = get_user_model()
# Create your models here.

class Exercise(models.Model):
	CARDIO = 'Cardio'
	WEIGHTS = 'Weights'

	CATEGORY = (
		('Cardio','Cardio'),
		('Weights','Weights'),
		)

	user = models.ForeignKey(User, related_name='exc_user', on_delete=models.CASCADE)
	minutes = models.IntegerField(default=30)
	calories_burned = models.IntegerField(default=300)
	exercise_type = models.CharField(max_length =15, choices=CATEGORY, default=CARDIO)
	create_date = models.DateField(default=datetime.datetime.now)

	def __str__(self):
		return 'Exercise Type %s Calories Burned %s Minutes %s' % (self.exercise_type, self.calories_burned, self.minutes)

	def get_absolute_url(self):
		return reverse('exercises:exercise_detail', kwargs={'pk':self.pk})

