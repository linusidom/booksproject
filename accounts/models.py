# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserModel(AbstractUser):
	ideal_fat = models.IntegerField(default=20)
	ideal_protein = models.IntegerField(default=40)
	ideal_carbs = models.IntegerField(default=40)
	ideal_weight = models.IntegerField(default=185)
	ideal_calories = models.IntegerField(default=2000)
	current_weight = models.IntegerField(default=185)
	access_food = models.BooleanField(default=False)
	access_expenses = models.BooleanField(default=False)
	access_exercise = models.BooleanField(default=False)
	trainer_email = models.EmailField(null=True, blank=True)


	def __str__(self):
		return self.email

	def allow_access_food(self):
		self.access_food = True
		self.save()

	def allow_access_expenses(self):
		self.access_expenses = True
		self.save()

	def allow_access_exercises(self):
		self.access_exercises = True
		self.save()

	def get_absolute_url(self):
		return reverse('accounts:user_detail', kwargs={'pk':self.pk})

