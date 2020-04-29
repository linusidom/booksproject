# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.views.generic import (TemplateView, ListView, DetailView, CreateView,
									UpdateView, DeleteView)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from profile.models import Profile
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


# print(today, seven_days_ago)


# Calories/Dollars, Offset from Goal, Exercise Deficit
def cal_offset_func(accounts, foods, expenses, exercises, days):
	
	actual_calories = actual_expenses = actual_fat = actual_carbs = actual_protein = actual_servings = total_expenses = total_burned = 0.0

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


	abs_fat = actual_fat - (account.ideal_fat/100.0)*(account.ideal_calories * days)
	abs_prot = actual_protein - (account.ideal_protein/100.0)*(account.ideal_calories * days)
	abs_carbs = actual_carbs - (account.ideal_carbs/100.0)*(account.ideal_calories * days)

	actual_offset = (abs(abs_fat) + abs(abs_carbs) + abs(abs_prot))

	# Return Value
	offset_pct = actual_offset / ideal_calories * 100

	for expense in expenses:
		total_expenses += expense.amount
	
	# Return Value
	calories_to_dollars = float(actual_calories) / float(total_expenses)
	
	for exercise in exercises:
		total_burned += exercise.calories_burned

	off_target = (actual_calories - total_burned) - (account.ideal_calories * days)
	off_target_day = off_target / days
	
	# Return Values
	off_target_week = (off_target_day * 7 / 3500.0) + current_weight
	off_target_weeks = (off_target_day * 14 / 3500.0) + current_weight
	off_target_month = (off_target_day * 30 / 3500.0) + current_weight

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

def offset_pct(account, foods, days):
	actual_fat = actual_carbs = actual_protein = actual_servings = 0.0

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


	abs_fat = float(actual_fat) - (account.ideal_fat/100.0)*(account.ideal_calories * days)
	abs_prot = actual_protein - (account.ideal_protein/100.0)*(account.ideal_calories * days)
	abs_carbs = actual_carbs - (account.ideal_carbs/100.0)*(account.ideal_calories * days)

	actual_offset = (abs(abs_fat) + abs(abs_carbs) + abs(abs_prot))

	# Return Value
	offset_pct = actual_offset / account.ideal_calories * 100

	return offset_pct

def caloric_deficit(account, foods, exercises, days):
	actual_calories = total_burned = 0.0

	for food in foods:
		actual_servings = food.servings
		if actual_servings > 1:
			actual_calories += food.calories * food.servings
		else:
			actual_calories += food.calories

	for exercise in exercises:
		total_burned += exercise.calories_burned

	off_target = (actual_calories - total_burned) - (account.ideal_calories * days)
	off_target_day = off_target / days
	
	# Return Values
	off_target_week = (off_target_day * 7 / 3500.0) + account.current_weight
	off_target_weeks = (off_target_day * 14 / 3500.0) + account.current_weight
	off_target_month = (off_target_day * 30 / 3500.0) + account.current_weight

	return off_target_week, off_target_weeks, off_target_month

@login_required
def report_list(request):
	print(request.user)
	profile = Profile.objects.get(user=request.user)
	
	calories_to_dollars = offset = off_week = off_weeks = off_month = False
	if request.method == 'POST':
		# date = 'Blah'
		startdate = request.POST.get('startdate')
		enddate = request.POST.get('enddate')
		print('startdate and Endate\n',startdate, enddate)
		if not startdate and not enddate:
			enddate = datetime.datetime.today().strftime('%Y-%m-%d')
			startdate = (datetime.datetime.today() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
		print('startdate and Endate\n',startdate,enddate)

			
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
			offset = offset_pct(profile, foods, date_range)
		if foods and exercises:
			off_week = caloric_deficit(profile, foods, exercises, date_range)[0]
			off_weeks = caloric_deficit(profile, foods, exercises, date_range)[1]
			off_month = caloric_deficit(profile, foods, exercises, date_range)[2]

		context = {'foods':foods,
					'expenses':expenses,
					'exercises':exercises,
					'calories_to_dollars':calories_to_dollars,
					'offset':offset,
					'off_week':off_week,
					'off_weeks':off_weeks,
					'off_month':off_month,
					'test_val':'test_val',
					}

		return render(request,'reports/reports.html', context)

	else:
		default = True
		days = 7
		startdate = datetime.datetime.now() - datetime.timedelta(days=days)	
		enddate = datetime.datetime.now()

		date_range = datetime.timedelta(days=days)
		date_range = date_range.days

		foods = Food.objects.filter(user=request.user, create_date__range=[startdate,enddate])
		expenses = Expense.objects.filter(user=request.user, create_date__range=[startdate,enddate])
		exercises = Exercise.objects.filter(user=request.user, create_date__range=[startdate,enddate])

		if foods and expenses:
			calories_to_dollars = calories_dollars(foods, expenses, date_range)
		if foods:
			offset = offset_pct(profile, foods, date_range)
		if foods and exercises:
			off_week = caloric_deficit(profile, foods, exercises, date_range)[0]
			off_weeks = caloric_deficit(profile, foods, exercises, date_range)[1]
			off_month = caloric_deficit(profile, foods, exercises, date_range)[2]
		
		return render(request,'reports/reports.html', {'foods':foods,
														'expenses':expenses,
														'exercises':exercises,
														'calories_to_dollars':calories_to_dollars,
														'offset':offset,
														'default':default,
														'off_week':off_week,
														'off_weeks':off_weeks,
														'off_month':off_month})

class IndexTemplateView(LoginRequiredMixin, ListView):
	template_name='reports/reports.html'
	context_object_name = 'all_items'
	today = datetime.datetime.today().strftime('%Y-%m-%d')
	seven_days_ago = (datetime.datetime.today() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')

	def get_queryset(self):
		user = self.request.user
		queryset = User.objects.filter(username=user)
		return queryset

	def get_context_data(self, **kwargs):
		context = super(IndexTemplateView, self).get_context_data(**kwargs)
		context['foods'] = Food.objects.filter(user=self.request.user, create_date__range=[seven_days_ago,today])
		context['expenses'] = Expense.objects.filter(user=self.request.user, create_date__range=[seven_days_ago,today])
		context['exercises'] = Exercise.objects.filter(user=self.request.user, create_date__range=[seven_days_ago,today])
		return context
