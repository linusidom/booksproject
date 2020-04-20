# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse, redirect
# from django.core.urlresolvers import reverse_lazy
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import (TemplateView, ListView, DetailView,
									CreateView, UpdateView, DeleteView)

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from expenses.models import Expense
from expenses.forms import ExpenseForm
from foods.models import Food
from foods.forms import FoodForm
from django.http import HttpResponse
# from accounts.models import UserModel

class IndexTemplateView(TemplateView):
	template_name='expenses/index.html'

# Expenses

class ExpenseListView(LoginRequiredMixin, ListView):
	model = Expense

	def get_queryset(self):
		user = self.request.user
		queryset = Expense.objects.filter(user=user)
		return queryset

class ExpenseDetailView(LoginRequiredMixin, DetailView):
	model = Expense

	def get_queryset(self):
		user = self.request.user
		queryset = Expense.objects.filter(user=user)
		return queryset


class ExpenseCreateView(LoginRequiredMixin, CreateView):
	model = Expense
	form_class = ExpenseForm
	success_url = reverse_lazy('expenses:index')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(ExpenseCreateView, self).form_valid(form)

class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
	model = Expense
	form_class = ExpenseForm
	success_url = reverse_lazy('expenses:index')
	

class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
	model = Expense
	success_url = reverse_lazy('expenses:index')
