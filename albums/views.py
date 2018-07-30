# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views import generic

from albums.models import Album

class IndexTemplateView(generic.TemplateView):
	template_name='albums/index.html'

class AlbumListView(generic.ListView):
	model = Album

class AlbumAPITemplateView(generic.TemplateView):
	template_name='albums/albumapi.html'

