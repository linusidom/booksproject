# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	pubdate = models.CharField(max_length = 100, null=True)
	wikilink = models.CharField(max_length = 255, null=True)
	occurrences = models.IntegerField(null=True)
	amazonlink = models.CharField(max_length = 255, null=True)
	
	def __str__(self):
		return self.title

	