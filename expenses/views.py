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
from accounts.models import UserModel

class IndexTemplateView(TemplateView):
	template_name='expenses/index.html'

# Expenses

class ExpenseListView(LoginRequiredMixin, ListView):
	model = Expense
	login_url = 'accounts:user_login'

	def get_queryset(self):
		user = self.request.user
		queryset = Expense.objects.filter(user=user)
		return queryset

class ExpenseDetailView(LoginRequiredMixin, DetailView):
	model = Expense
	login_url = 'accounts:user_login'

	def get_queryset(self):
		user = self.request.user
		queryset = Expense.objects.filter(user=user)
		return queryset


class ExpenseCreateView(LoginRequiredMixin, CreateView):
	model = Expense
	login_url = 'accounts:user_login'
	form_class = ExpenseForm
	success_url = reverse_lazy('expenses:expense_list')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(ExpenseCreateView, self).form_valid(form)

class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
	model = Expense
	form_class = ExpenseForm
	login_url = 'accounts:user_login'
	success_url = reverse_lazy('expenses:expense_list')

class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
	model = Expense
	success_url = reverse_lazy('expenses:expense_list')
	login_url = 'accounts:user_login'

# @login_required
# def expense_create(request):
# 	if request.method == 'POST':
# 		expense_form = ExpenseForm(request.POST)
# 		food_form = FoodForm(request.POST)
# 		print 'After Post'
# 		if food_form.is_valid() and expense_form.is_valid():
# 			print 'After Valid'
# 			expense = expense_form.save(commit=False)
# 			food = food_form.save(commit=False)
# 			food.food_item = expense.expense_item
# 			expense.user = request.user
# 			food.user = request.user
# 			expense.save()
# 			food.save()

# 			return redirect('expenses:expense_list')
# 		else:
# 			return HttpResponse(food_form.errors, expense_form.errors)
# 	else:
# 		expense_form = ExpenseForm()
# 		food_form = FoodForm()
# 		return render(request, 'expenses/expense_form.html', {'expense_form':expense_form,
# 																'food_form':food_form})
