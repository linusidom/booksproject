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
	trainer_email = models.EmailField(null=True, blank=True)


	def __str__(self):
		return self.email

	def get_absolute_url(self):
		return reverse('accounts:user_detail', kwargs={'pk':self.pk})

