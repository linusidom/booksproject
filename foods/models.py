from __future__ import unicode_literals

from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
import datetime
User = get_user_model()
# Create your models here.

class Food(models.Model):
	user = models.ForeignKey(User, related_name='food_user')
	food_item = models.CharField(max_length= 50)
	calories = models.IntegerField(default = 500)
	servings = models.IntegerField(default = 1)
	create_date = models.DateField(default=datetime.datetime.now)
	fat = models.IntegerField(default=100)
	protein = models.IntegerField(default=200)
	carbs = models.IntegerField(default=200)

	def __str__(self):
		return self.food_item

	def get_absolute_url(self):
		return reverse('foods:food_detail', kwargs={'pk':self.pk})


	class Meta():
		ordering = ['-create_date']