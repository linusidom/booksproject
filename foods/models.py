from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
import datetime
User = get_user_model()
# Create your models here.

class Food(models.Model):
	user = models.ForeignKey(User, related_name='food_user', on_delete=models.CASCADE)
	food_item = models.CharField(max_length= 50)
	calories = models.IntegerField(blank=True)
	servings = models.IntegerField(default = 1)
	create_date = models.DateField(default=datetime.datetime.now)
	fat = models.IntegerField(default=10)
	protein = models.IntegerField(default=20)
	carbs = models.IntegerField(default=20)

	def __str__(self):
		return self.food_item

	def get_absolute_url(self):
		return reverse('foods:food_detail', kwargs={'pk':self.pk})


	class Meta():
		ordering = ['-create_date']

def pre_calories(sender, instance, *args, **kwargs):
	if not instance.calories:
		instance.calories = (instance.fat * 9) + (instance.carbs * 4) + (instance.protein * 4)

pre_save.connect(pre_calories, sender=Food)





