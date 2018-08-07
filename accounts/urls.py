from django.conf.urls import url
from accounts import views
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy

app_name='accounts'

urlpatterns=[
	url(r'^$',views.IndexTemplateView.as_view(), name = 'index'),
	url(r'^signup/$',views.SignUpCreateView.as_view(), name = 'signup'),
	url(r'^user_login/$', auth_views.LoginView.as_view(template_name = 'accounts/login.html'), name='user_login'),
	url(r'^user_logout/$', auth_views.LogoutView.as_view(), name='user_logout'),
	url(r'^change_password/$', auth_views.PasswordChangeView.as_view(template_name = 'accounts/change_password_form.html', success_url=reverse_lazy('accounts:password_change_done')), name='user_change_password'),
	url(r'^password_change_done/$', auth_views.PasswordChangeDoneView.as_view(template_name = 'accounts/change_password_done.html'), name='password_change_done'),
	
	url(r'^(?P<pk>\d+)/$', views.UserModelDetailView.as_view(), name='user_detail'),
	url(r'^update/(?P<pk>\d+)/$', views.UserModelUpdateView.as_view(), name='user_update'),
	url(r'^delete/(?P<pk>\d+)/$', views.UserModelDeleteView.as_view(), name='user_delete'),
]