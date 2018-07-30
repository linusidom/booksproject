from __future__ import unicode_literals

from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
import datetime
User = get_user_model()
# Create your models here.

class Expense(models.Model):
	BILLS = 'Bills'
	FOOD = 'Food'
	PERSONAL = 'Personal Care'
	MISC = 'Misc'

	CATEGORY = (
		('Food','Food'),
		('Bills','Bills'),
		('Personal Care','Personal Care'),
		('Misc','Misc'),
		)

	user = models.ForeignKey(User, related_name='exp_user')
	amount = models.IntegerField()
	expense_item = models.CharField(max_length= 50)
	expense_type = models.CharField(max_length =15, choices=CATEGORY, default=FOOD)
	create_date = models.DateField(default=datetime.datetime.now)
	
	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return reverse('expenses:expense_detail', kwargs={'pk':self.pk})

	class Meta():
		ordering = ['-create_date']
