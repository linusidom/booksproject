from django.conf.urls import url
from django.urls import path, re_path
from profile import views
from django.contrib.auth import views as auth_views
# from django.core.urlresolvers import reverse_lazy
from django.urls import reverse_lazy
from profile.forms import CustomAuthForm

app_name='profile'

urlpatterns=[
	path('',views.ProfileListView.as_view(), name = 'index'),
	re_path('invite_trainer/(?P<pk>\d+)',views.invite_trainer, name = 'invite_trainer'),
	# re_path(r'^signup/$',views.signup, name = 'signup'),

	re_path('detail/(?P<pk>\d+)',views.ProfileDetailView.as_view(), name = 'profile_detail'),
	# path('create/',views.ProfileCreateView.as_view(), name = 'profile_create'),
	re_path('update/(?P<pk>\d+)/',views.ProfileUpdateView.as_view(), name = 'profile_update'),
	re_path('delete/(?P<pk>\d+)/',views.ProfileDeleteView.as_view(), name = 'profile_delete'),	
]