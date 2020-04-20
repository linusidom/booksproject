# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
# from django.core.urlresolvers import reverse_lazy
from django.urls import reverse_lazy

# Create your views here.
from django.http import HttpResponse
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from profile.models import Profile
from profile.forms import ProfileForm, ProfileUpdateForm, InviteTrainerForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from foods.models import Food
from django.contrib.auth import get_user_model

User = get_user_model()

class IndexTemplateView(TemplateView):
	template_name='profile/index.html'


class ProfileListView(LoginRequiredMixin, ListView):
	model = Profile
	# template_name = 'profile/profile_list.html'
	# context_object_name = 'user_list'
	def get_queryset(self):
		user = self.request.user
		queryset = Profile.objects.filter(user=user)
		return queryset

class ProfileDetailView(LoginRequiredMixin, DetailView):
	model = Profile
	template_name = 'profile/profile_detail.html'
	
	# def get_context_data(self, **kwargs):
	# 	context = super(ProfileDetailView, self).get_context_data(**kwargs)
	# 	context['trainees'] = Profile.objects.filter(trainer_email=self.request.user)
	# 	foods = dict()
	# 	for index,trainee in enumerate(context['trainees']):
	# 		foods[index] = Food.objects.filter(user_id=trainee.pk)
	# 	context['foods'] = foods
	# 	context['range'] = str(len(context['trainees']) + 10)
	# 	return context

	def get_queryset(self):
		user = self.request.user
		queryset = Profile.objects.filter(user=user)
		return queryset

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
	model = Profile
	form_class = ProfileUpdateForm

class ProfileDeleteView(LoginRequiredMixin, DeleteView):
	model = Profile
	success_url = reverse_lazy('index')

@login_required
def invite_trainer(request, pk):
	if request.method == 'POST':
		form = InviteTrainerForm(request.POST, instance=request.user)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.save()
			return redirect('profile:user_detail', pk=pk)
		else:
			return HttpResponse(forms.errors)
	else:
		form = InviteTrainerForm(instance = request.user)
	return render(request, 'profile/invite_trainer_form.html', {'form':form})



# @login_required
# def update(request, pk):
# 	if request.method == 'POST':
# 		form = ProfileUpdateForm(request.POST, instance=request.user)
# 		if form.is_valid():
# 			profile = form.save(commit=False)
# 			profile.username = profile.email
# 			profile.save()
# 			return redirect('profile:user_detail', pk=pk)
# 	else:

# 		form = ProfileUpdateForm(instance=request.user)
# 	return render(request, 'profile/signup.html', {'form': form})












