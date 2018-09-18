# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.test import Client
from django.urls import reverse
from accounts.models import UserModel
client = Client()
# Create your tests here.

class AccountTest(TestCase):

	def setUp(self):
		print('setup')
		self.user = Profile.objects.create_user(username='testuser@aol.com', password='12345')

	def test_login(self):
		login = self.client.login(username='testuser', password='12345')

	def test_pages_not_logged_in(self):
		response = self.client.get(reverse('accounts:index'))
		self.assertEqual(response.status_code, 200)

		response = self.client.get(reverse('accounts:signup'))
		self.assertEqual(response.status_code, 200)

		response = self.client.get(reverse('accounts:user_login'))
		self.assertEqual(response.status_code, 200)

		response = self.client.get(reverse('accounts:user_logout'))
		self.assertEqual(response.status_code, 302)

		response = self.client.get(reverse('accounts:user_change_password'))
		self.assertEqual(response.status_code, 302)
		
		response = self.client.get(reverse('accounts:password_change_done'))
		self.assertEqual(response.status_code, 302)



		
		
		


	def test_detail_update_delete(self):
		pass

	def test_logout(self):
		pass
	def test_login(self):
		pass