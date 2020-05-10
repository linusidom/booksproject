# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Album(models.Model):
	title = models.CharField(max_length = 255, null=True, blank=True)
	artist = models.CharField(max_length = 255, null=True, blank=True)
	year = models.CharField(max_length = 255, null=True, blank=True)
	occurrences = models.IntegerField(null=True, blank=True)
	wikilink = models.CharField(max_length = 255, null=True, blank=True)
	amazonlink = models.CharField(max_length = 255, null=True, blank=True)

	def __str__(self):
		return self.title

	