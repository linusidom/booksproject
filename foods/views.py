# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from django.core.urlresolvers import reverse_lazy
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import (TemplateView, ListView, DetailView,
									CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin

from foods.models import Food
from foods.forms import FoodForm
from expenses.models import Expense

class IndexTemplateView(TemplateView):
	template_name='foods/index.html'

class FoodListView(LoginRequiredMixin, ListView):
	model = Food
	
	def get_queryset(self):
		user = self.request.user
		queryset = Food.objects.filter(user = user)
		return queryset

class FoodDetailView(LoginRequiredMixin, DetailView):
	model = Food

	def get_queryset(self):
		user = self.request.user
		queryset = Food.objects.filter(user = user)
		return queryset

class FoodCreateView(LoginRequiredMixin, CreateView):
	model = Food
	# fields = ['item','servings','calories','create_date']
	form_class = FoodForm
	success_url = reverse_lazy('reports:index')

	# Filter by User
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(FoodCreateView, self).form_valid(form)

class FoodUpdateView(LoginRequiredMixin, UpdateView):
	model = Food
	form_class = FoodForm
	success_url = reverse_lazy('reports:index')

class FoodDeleteView(LoginRequiredMixin, DeleteView):
	model = Food
	success_url = reverse_lazy('reports:index')




