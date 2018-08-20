# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, reverse

# Create your views here.
from django.views.generic import (TemplateView, ListView, DetailView,
									CreateView, UpdateView, DeleteView)


from tagr.models import Post, UserModel
from tagr.forms import PostForm

# from django.core.urlresolvers import reverse_lazy
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class IndexTemplateView(TemplateView):
	template_name='tagr/index.html'

class PostListView(LoginRequiredMixin, ListView):
	model = Post
	login_url = 'accounts:user_login'

	def get_queryset(self):
		user = self.request.user
		queryset = Post.objects.filter(user=user)
		return queryset

class PostDetailView(LoginRequiredMixin, DetailView):
	model = Post
	login_url = 'accounts:user_login'

	def get_queryset(self):
		user = self.request.user
		queryset = Post.objects.filter(user=user)
		return queryset


class PostUpdateView(LoginRequiredMixin, UpdateView):
	model = Post
	fields = ['message']

	def get_queryset(self):
		base_qs = super(PostUpdateView, self).get_queryset()
		return base_qs.filter(user=self.request.user)

@login_required
def post_publish(self, pk):
	post = get_object_or_404(Post, pk = pk)
	post.publish_post()
	return reverse('tagr:post_detail', kwargs={'pk':post.pk})

