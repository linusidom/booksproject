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
from django.conf.urls import url, include
from django.contrib import admin
from booksproject import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^books/',include('books.urls', namespace='books')),
    url(r'^api_books/',include('books.api.urls', namespace = 'api_books')),
    url(r'^albums/',include('albums.urls', namespace='albums')),
    url(r'^api_albums/',include('albums.api.urls', namespace = 'api_albums')),
    url(r'^$', views.IndexTemplateView.as_view(), name ='index'),
    url(r'^intro/$', views.IntroTemplateView.as_view(), name ='intro'),


    url(r'^tagr/',include('tagr.urls', namespace='tagr')),
    
    # Testing Social Login
    url(r'^accounts/',include('accounts.urls', namespace='accounts')),
    url(r'^account/', include('allauth.urls')),

    url(r'^api_tagr/',include('tagr.api.urls', namespace = 'api_tagr')),
    url(r'^api_accounts/',include('accounts.api.urls', namespace = 'api_accounts')),
    url(r'^loggedin/$', views.LoggedInTemplateView.as_view(), name='loggedin'),
    url(r'^loggedout/$', views.LoggedOutTemplateView.as_view(), name='loggedout'),
    url(r'^contact/$', views.contactform, name='contactform'),
    url(r'^apiinfo/', views.APIInfoTemplateView.as_view(), name='apiinfo'),

    url(r'^foods/', include('foods.urls',namespace = 'foods')),
    url(r'^expenses/', include('expenses.urls',namespace = 'expenses')),
    url(r'^exercises/', include('exercises.urls',namespace = 'exercises')),
    url(r'^reports/', include('reports.urls',namespace = 'reports')),

    # API
    url(r'^api_foods/', include('foods.api.urls',namespace = 'api_foods')),
    url(r'^api_expenses/', include('expenses.api.urls',namespace = 'api_expenses')),
    url(r'^api_exercises/', include('exercises.api.urls',namespace = 'api_exercises')),

    # Password Reset
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html', email_template_name = 'accounts/password_reset_email.html', subject_template_name='accounts/password_reset_subject.txt', domain='modisidom.herokuapp.com'), name='password_reset'),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),


]


