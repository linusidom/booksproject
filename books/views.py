# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views import generic

from books.models import Book

class IndexTemplateView(generic.TemplateView):
	template_name='books/index.html'

class BookListView(generic.ListView):
	model = Book

class BookAPITemplateView(generic.TemplateView):
	template_name='books/bookapi.html'

