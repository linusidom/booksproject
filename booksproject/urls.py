"""booksproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include, reverse_lazy
from django.contrib import admin
from booksproject import views
from django.contrib.auth import views as auth_views
# from accounts.forms import CustomAuthForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.IndexTemplateView.as_view(), name ='index'),

    # Book and Albums
    path('books/',include('books.urls', namespace='books')),
    path('api_books/',include('books.api.urls', namespace = 'api_books')),
    path('albums/',include('albums.urls', namespace='albums')),
    path('api_albums/',include('albums.api.urls', namespace = 'api_albums')),
    
    # TAGR App
    path('tagr/',include('tagr.urls', namespace='tagr')),
    
    path('profile/',include('profile.urls', namespace='profile')),

    path('contact/', views.contactform, name='contactform'),
    path('apiinfo/', views.APIInfoTemplateView.as_view(), name='apiinfo'),

    # Foods Apps
    path('foods/', include('foods.urls',namespace = 'foods')),
    path('expenses/', include('expenses.urls',namespace = 'expenses')),
    path('exercises/', include('exercises.urls',namespace = 'exercises')),
    path('reports/', include('reports.urls',namespace = 'reports')),

    # path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=CustomAuthForm, redirect_authenticated_user=True), name = 'user_login'),
    # path('logout/', auth_views.LogoutView.as_view(), name = 'user_logout'),
    
    # path('change-password/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('user_logout')), name='password_change'),
    # path('change-password-done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z](1, 13)-[0-9A-Za-z](1, 20))/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


]


