# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
# Create your views here.
from django.views.generic import (TemplateView, ListView, DetailView,
									CreateView, UpdateView,DeleteView)

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from exercises.models import Exercise
from exercises.forms import ExerciseForm


class IndexTemplateView(TemplateView):
	template_name='exercises/index.html'

class ExerciseListView(LoginRequiredMixin, ListView):
	model = Exercise
	login_url = 'accounts:user_login'

	def get_queryset(self):
		user = self.request.user
		queryset = Exercise.objects.filter(user=user)
		return queryset

class ExerciseDetailView(LoginRequiredMixin, DetailView):
	model = Exercise
	login_url = 'accounts:user_login'

	def get_querysef(self):
		user = self.request.user
		queryset = Exercise.objects.filter(user=user)
		return queryset


class ExerciseCreateView(LoginRequiredMixin,CreateView):
	model = Exercise
	form_class = ExerciseForm
	login_url = 'accounts:user_login'
	success_url = reverse_lazy('exercises:exercise_list')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(ExerciseCreateView, self).form_valid(form)

class ExerciseUpdateView(LoginRequiredMixin, UpdateView):
	model = Exercise
	form_class = ExerciseForm
	login_url = 'accounts:user_login'
	success_url = reverse_lazy('exercises:exercise_list')

class ExerciseDeleteView(LoginRequiredMixin, DeleteView):
	model = Exercise
	success_url = reverse_lazy('exercises:exercise_list')
	login_url = 'accounts:user_login'		
