# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.core.mail import send_mail, EmailMessage

class IndexTemplateView(generic.TemplateView):
	template_name='index.html'

class IntroTemplateView(generic.TemplateView):
	template_name='intro.html'


class LoggedInTemplateView(generic.TemplateView):
	template_name='loggedin.html'

class LoggedOutTemplateView(generic.TemplateView):
	template_name='loggedout.html'

class APIInfoTemplateView(generic.TemplateView):
	template_name='apiinfo.html'


def contactform(request):
	if request.method == 'POST':

		name = request.POST.get('name')
		subject = 'Inquiry from Website'
		message = request.POST.get('message')
		email = request.POST.get('email')
		message = name + ' has sent you a message:\n\n' + message + '\n\n' + email

		send_mail(
			subject,
			message,
			'siliconvalleyenglishthailand@gmail.com',
			['siliconvalleyenglishthailand@gmail.com'],
			fail_silently=False,)
		return render(request, 'thankyou.html')
	else:
		return render(request,'index.html')

