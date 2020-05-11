# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView
from django.core.mail import send_mail, EmailMessage

class IndexTemplateView(TemplateView):
	template_name='index.html'

class IntroTemplateView(TemplateView):
	template_name='intro.html'


class LoggedInTemplateView(TemplateView):
	template_name='loggedin.html'

class LoggedOutTemplateView(TemplateView):
	template_name='loggedout.html'

class APIInfoTemplateView(TemplateView):
	template_name='apiinfo.html'

class ThankYou(TemplateView):
	template_name = 'thankyou.html'

def about_contact(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		subject = 'Inquiry from Website'
		message = request.POST.get('message')
		email = request.POST.get('email')
		message = name + ' has sent you a message:\n\n' + message + '\n\n' + email
		print('Message', message)
		send_mail(
			subject,
			message,
			'siliconvalleyenglishthailand@gmail.com',
			['siliconvalleyenglishthailand@gmail.com'],
			fail_silently=False,)
		return redirect('thankyou')
	else:
		return render(request,'about_contact.html')

