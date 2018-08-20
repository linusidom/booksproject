# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
# from django.core.urlresolvers import reverse_lazy
from django.urls import reverse_lazy

# Create your views here.
from django.http import HttpResponse
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from accounts.models import UserModel
from accounts.forms import UserForm, UserUpdateForm, InviteTrainerForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from foods.models import Food

class IndexTemplateView(TemplateView):
	template_name='accounts/index.html'


class UserModelListView(LoginRequiredMixin, ListView):
	model = UserModel


	def get_queryset(self):
		user = self.request.user
		queryset = UserModel.objects.filter(user=user)
		return queryset

class UserModelDetailView(LoginRequiredMixin, DetailView):
	model = UserModel

	def get_context_data(self, **kwargs):
		context = super(UserModelDetailView, self).get_context_data(**kwargs)
		context['trainees'] = UserModel.objects.filter(trainer_email=self.request.user)
		foods = dict()
		for index,trainee in enumerate(context['trainees']):
			print('index', index)
			foods[index] = Food.objects.filter(user_id=trainee.pk)
		context['foods'] = foods
		return context

	def get_queryset(self):
		userpk = self.request.user.pk
		queryset = UserModel.objects.filter(pk=userpk)
		return queryset


# class SignUpCreateView(CreateView):
# 	success_url = reverse_lazy('accounts:user_login')
# 	template_name = 'accounts/signup.html'
# 	model = UserModel
# 	form_class = UserForm

# class UserModelUpdateView(LoginRequiredMixin, UpdateView):
# 	model = UserModel
#
# 	form_class = UserUpdateForm

class UserModelDeleteView(LoginRequiredMixin, DeleteView):
	model = UserModel
	success_url = reverse_lazy('index')




def signup(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			usermodel = form.save(commit=False)
			usermodel.username = usermodel.email
			usermodel.save()
			return redirect('accounts:user_login')
		else:
			return HttpResponse(form.errors)
	else:
		form = UserForm()
	return render(request, 'accounts/signup.html', {'form': form})


@login_required
def update(request, pk):
	if request.method == 'POST':
		form = UserUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			usermodel = form.save(commit=False)
			usermodel.username = usermodel.email
			usermodel.save()
			return redirect('accounts:user_detail', pk=pk)
	else:

		form = UserUpdateForm(instance=request.user)
	return render(request, 'accounts/signup.html', {'form': form})

@login_required
def invite_trainer(request, pk):
	if request.method == 'POST':
		form = InviteTrainerForm(request.POST, instance=request.user)
		if form.is_valid():
			usermodel = form.save(commit=False)
			usermodel.save()
			return redirect('accounts:user_detail', pk=pk)
		else:
			return HttpResponse(forms.errors)
	else:
		form = InviteTrainerForm(instance = request.user)
	return render(request, 'accounts/invite_trainer_form.html', {'form':form})











