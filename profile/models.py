# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.shortcuts import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

User = get_user_model()

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	ideal_fat = models.IntegerField(default=20)
	ideal_protein = models.IntegerField(default=40)
	ideal_carbs = models.IntegerField(default=40)
	ideal_weight = models.IntegerField(default=185)
	ideal_calories = models.IntegerField(default=2000)
	current_weight = models.IntegerField(default=185)
	trainer_email = models.EmailField(null=True, blank=True)


	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return reverse('profile:profile_detail', kwargs={'pk':self.pk})


def post_add_trainer_email(sender, instance, *args, **kwargs):
	if not instance.trainer_email:
		instance.trainer_email = instance.user.email

post_save.connect(post_add_trainer_email, sender=Profile)



