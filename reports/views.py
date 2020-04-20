# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.views.generic import (TemplateView, ListView, DetailView, CreateView,
									UpdateView, DeleteView)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from foods.models import Food
from expenses.models import Expense
from exercises.models import Exercise
from foods.forms import FoodForm
from expenses.forms import ExpenseForm
from exercises.forms import ExerciseForm
from django.http import HttpResponse
import datetime
from django.contrib.auth import get_user_model

User = get_user_model()

class IndexTemplateView(LoginRequiredMixin, ListView):
	template_name='reports/reports.html'
	context_object_name = 'all_items'

	def get_queryset(self):
		user = self.request.user
		queryset = User.objects.filter(username=user)
		return queryset

	def get_context_data(self, **kwargs):
		context = super(IndexTemplateView, self).get_context_data(**kwargs)
		context['foods'] = Food.objects.filter(user=self.request.user, create_date__range=['2018-07-06','2018-07-10'])
		context['expenses'] = Expense.objects.filter(user=self.request.user, create_date__range=['2018-07-06','2018-07-10'])
		context['exercises'] = Exercise.objects.filter(user=self.request.user, create_date__range=['2018-07-06','2018-07-10'])
		return context

# Calories/Dollars, Offset from Goal, Exercise Deficit
def cal_offset_func(accounts, foods, expenses, exercises, days):
	
	actual_calories = actual_expenses = actual_fat = actual_carbs = actual_protein = actual_servings = total_expenses = total_burned = 0.0

	for account in accounts:
		ideal_fat = account.ideal_fat
		ideal_protein = account.ideal_protein
		ideal_carbs = account.ideal_carbs
		ideal_calories = account.ideal_calories * days
		current_weight = account.current_weight
		ideal_weight = account.ideal_weight

	for food in foods:
		actual_servings = food.servings
		if actual_servings > 1:
			actual_calories += food.calories * food.servings
			actual_fat += food.fat * food.servings
			actual_carbs += food.carbs * food.servings
			actual_protein += food.protein * food.servings
		else:
			actual_calories += food.calories
			actual_fat += food.fat
			actual_carbs += food.carbs
			actual_protein += food.protein


	abs_fat = actual_fat - (ideal_fat/100.0)*ideal_calories
	abs_prot = actual_protein - (ideal_protein/100.0)*ideal_calories
	abs_carbs = actual_carbs - (ideal_carbs/100.0)*ideal_calories

	actual_offset = (abs(abs_fat) + abs(abs_carbs) + abs(abs_prot))

	# Return Value
	offset_pct = actual_offset / ideal_calories * 100

	for expense in expenses:
		total_expenses += expense.amount
	
	# Return Value
	calories_to_dollars = float(actual_calories) / float(total_expenses)
	
	for exercise in exercises:
		total_burned += exercise.calories_burned

	off_target = (actual_calories - total_burned) - ideal_calories
	off_target_day = off_target / days
	
	# Return Values
	off_target_week = (off_target_day * 7 / 3500.0) + current_weight
	off_target_weeks = (off_target_day * 14 / 3500.0) + current_weight
	off_target_month = (off_target_day * 30 / 3500.0) + current_weight

	# print 'Total Expenses ', total_expenses
	# print 'Actuals ', actual_fat, actual_carbs, actual_protein
	# print 'Offset', actual_offset, ideal_calories, actual_calories
	# print 'Absolute', abs_fat, abs_prot, abs_carbs
	# print 'Total Deficit ', actual_calories, total_burned, ideal_calories
	# print 'Offset Pct ', offset_pct

	return calories_to_dollars, offset_pct, off_target_week, off_target_weeks, off_target_month




def calories_dollars(foods, expenses, days):
	actual_calories = total_expenses = 0.0
	for food in foods:
		actual_servings = food.servings
		if actual_servings > 1:
			actual_calories += food.calories * food.servings
		else:
			actual_calories += food.calories

	for expense in expenses:
		total_expenses += expense.amount

	calories_to_dollars = float(actual_calories) / float(total_expenses)
	return calories_to_dollars

def offset_pct(accounts, foods, days):
	actual_fat = actual_carbs = actual_protein = actual_servings = 0.0

	for account in accounts:
		ideal_calories = account.ideal_calories * days
		ideal_fat = account.ideal_fat
		ideal_protein = account.ideal_protein
		ideal_carbs = account.ideal_carbs
		current_weight = account.current_weight
		ideal_weight = account.ideal_weight

	for food in foods:
		actual_servings = food.servings
		if actual_servings > 1:
			actual_fat += food.fat * food.servings
			actual_carbs += food.carbs * food.servings
			actual_protein += food.protein * food.servings
		else:
			actual_fat += food.fat
			actual_carbs += food.carbs
			actual_protein += food.protein


	abs_fat = float(actual_fat) - (ideal_fat/100.0)*ideal_calories
	abs_prot = actual_protein - (ideal_protein/100.0)*ideal_calories
	abs_carbs = actual_carbs - (ideal_carbs/100.0)*ideal_calories

	actual_offset = (abs(abs_fat) + abs(abs_carbs) + abs(abs_prot))

	# Return Value
	offset_pct = actual_offset / ideal_calories * 100

	return offset_pct

def caloric_deficit(accounts, foods, exercises, days):
	actual_calories = total_burned = 0.0

	for account in accounts:
		ideal_fat = account.ideal_fat
		ideal_protein = account.ideal_protein
		ideal_carbs = account.ideal_carbs
		ideal_calories = account.ideal_calories * days
		current_weight = account.current_weight
		ideal_weight = account.ideal_weight

	for food in foods:
		actual_servings = food.servings
		if actual_servings > 1:
			actual_calories += food.calories * food.servings
		else:
			actual_calories += food.calories

	for exercise in exercises:
		total_burned += exercise.calories_burned

	off_target = (actual_calories - total_burned) - ideal_calories
	off_target_day = off_target / days
	
	# Return Values
	off_target_week = (off_target_day * 7 / 3500.0) + current_weight
	off_target_weeks = (off_target_day * 14 / 3500.0) + current_weight
	off_target_month = (off_target_day * 30 / 3500.0) + current_weight

	return off_target_week, off_target_weeks, off_target_month

@login_required
def report_list(request):
	accounts = User.objects.filter(username=request.user)
	print('User Account', dir(accounts))
	calories_to_dollars = offset = off_week = off_weeks = off_month = False
	if request.method == 'POST':
		date = 'Blah'
		startdate = request.POST.get('startdate')
		enddate = request.POST.get('enddate')
		
		foods = Food.objects.filter(user=request.user, create_date__range=[startdate,enddate])
		expenses = Expense.objects.filter(user=request.user, create_date__range=[startdate,enddate])
		exercises = Exercise.objects.filter(user=request.user, create_date__range=[startdate,enddate])
		
		datetime_startdate = datetime.datetime.strptime(startdate, "%Y-%m-%d")
		datetime_enddate = datetime.datetime.strptime(enddate, "%Y-%m-%d")
		date_range = datetime_enddate - datetime_startdate
		date_range = int(date_range.days) + 1
		

		if foods and expenses:
			calories_to_dollars = calories_dollars(foods, expenses, date_range)
		if foods:
			offset = offset_pct(accounts, foods, date_range)
		if foods and exercises:
			off_week = caloric_deficit(accounts, foods, exercises, date_range)[0]
			off_weeks = caloric_deficit(accounts, foods, exercises, date_range)[1]
			off_month = caloric_deficit(accounts, foods, exercises, date_range)[2]

		return render(request,'reports/reports.html', {'foods':foods,
															'expenses':expenses,
															'exercises':exercises,
															'calories_to_dollars':calories_to_dollars,
															'offset':offset,
															'off_week':off_week,
															'off_weeks':off_weeks,
															'off_month':off_month})

	else:
		default = True
		days = 7
		startdate = datetime.datetime.now() - datetime.timedelta(days=days)	
		enddate = datetime.datetime.now()

		# print(startdate.strftime('%Y-%m-%d'))
		# print(enddate.strftime('%Y-%m-%d'))

		date_range = datetime.timedelta(days=days)
		date_range = date_range.days

		foods = Food.objects.filter(user=request.user, create_date__range=[startdate,enddate])
		expenses = Expense.objects.filter(user=request.user, create_date__range=[startdate,enddate])
		exercises = Exercise.objects.filter(user=request.user, create_date__range=[startdate,enddate])

		if foods and expenses:
			calories_to_dollars = calories_dollars(foods, expenses, date_range)
		if foods:
			offset = offset_pct(accounts, foods, date_range)
		if foods and exercises:
			off_week = caloric_deficit(accounts, foods, exercises, date_range)[0]
			off_weeks = caloric_deficit(accounts, foods, exercises, date_range)[1]
			off_month = caloric_deficit(accounts, foods, exercises, date_range)[2]
		
		return render(request,'reports/reports.html', {'foods':foods,
														'expenses':expenses,
														'exercises':exercises,
														'calories_to_dollars':calories_to_dollars,
														'offset':offset,
														'default':default,
														'off_week':off_week,
														'off_weeks':off_weeks,
														'off_month':off_month})



@login_required
def reports_list(request):

	accounts = User.objects.filter(username=request.user)

	if request.method == 'POST':
		date = 'Blah'
		startdate = request.POST.get('startdate')
		enddate = request.POST.get('enddate')
		
		foods = Food.objects.filter(user=request.user, create_date__range=[startdate,enddate])
		expenses = Expense.objects.filter(user=request.user, create_date__range=[startdate,enddate])
		exercises = Exercise.objects.filter(user=request.user, create_date__range=[startdate,enddate])
		
		if not foods or not expenses:
			nodata = True
			return render(request,'reports/reports.html', {'nodata':nodata})
		else:

			# Format Date Time Format to find delta of query
			datetime_startdate = datetime.datetime.strptime(startdate, "%Y-%m-%d")
			datetime_enddate = datetime.datetime.strptime(enddate, "%Y-%m-%d")
			date_range = datetime_enddate - datetime_startdate
			date_range = int(date_range.days) + 1

			calories_and_offset = cal_offset_func(accounts, foods, expenses, exercises, date_range)
			calories_to_dollars = calories_and_offset[0]
			offset = calories_and_offset[1]
			off_week = calories_and_offset[2]
			off_weeks = calories_and_offset[3]
			off_month = calories_and_offset[4]

			return render(request,'reports/reports.html', {'foods':foods,
															'expenses':expenses,
															'exercises':exercises,
															'calories_to_dollars':calories_to_dollars,
															'offset':offset,
															'off_week':off_week,
															'off_weeks':off_weeks,
															'off_month':off_month})
	

	else:
		default = True
		days = 3
		startdate = datetime.datetime.now() - datetime.timedelta(days=days)	
		enddate = datetime.datetime.now()

		# print(startdate.strftime('%Y-%m-%d'))
		# print(enddate.strftime('%Y-%m-%d'))

		date_range = datetime.timedelta(days=days)

		foods = Food.objects.filter(user=request.user, create_date__range=[startdate,enddate])
		expenses = Expense.objects.filter(user=request.user, create_date__range=[startdate,enddate])
		exercises = Exercise.objects.filter(user=request.user, create_date__range=[startdate,enddate])

		# foods = Food.objects.filter(user=request.user, create_date__range=['2016-07-01','2016-07-03'])
		# expenses = Expense.objects.filter(user=request.user, create_date__range=['2016-07-01','2016-07-03'])
		# exercises = Exercise.objects.filter(user=request.user, create_date__range=['2016-07-01','2016-07-03'])


		if not foods or not expenses:
			nodata = True
			return render(request,'reports/reports.html', {'nodata':nodata})

		calories_and_offset = cal_offset_func(accounts, foods, expenses, exercises, date_range.days)
		calories_to_dollars = calories_and_offset[0]
		offset = calories_and_offset[1]
		off_week = calories_and_offset[2]
		off_weeks = calories_and_offset[3]
		off_month = calories_and_offset[4]
		
		
		return render(request,'reports/reports.html', {'foods':foods,
														'expenses':expenses,
														'exercises':exercises,
														'calories_to_dollars':calories_to_dollars,
														'offset':offset,
														'default':default,
														'off_week':off_week,
														'off_weeks':off_weeks,
														'off_month':off_month})


@login_required
def create_new_entry(request):
	account = User.objects.filter(username=request.user)

	if request.method == 'POST':
		food_form = FoodForm(request.POST)
		expense_form = ExpenseForm(request.POST)
		exercise_form = ExerciseForm(request.POST)
		print(request.POST.get('food_item'))
		if request.POST.get('food_item') and request.POST.get('servings') and request.POST.get('calories'):
			food = food_form.save(commit=False)
			food.user = request.user
			food.save()

		if expense_form.is_valid():
			expense = expense_form.save(commit=False)
			expense.user = request.user
			expense.save()
			
		if exercise_form.is_valid():
			exercise = exercise_form.save(commit=False)
			exercise.user = request.user
			exercise.save()

		return redirect('reports:report_list')
		

	else:
		expense_form = ExpenseForm()
		food_form = FoodForm()
		exercise_form = ExerciseForm()
		return render(request,'reports/create.html', {'expense_form':expense_form,
													'exercise_form':exercise_form,
													'food_form':food_form})
















