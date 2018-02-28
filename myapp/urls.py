from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='myapp'

urlpatterns=[
	#/home/
	url(r'^$', views.home, name='home'),
	url(r'^home/$', views.home, name='home'),
	url(r'^view_notifications/$', views.view_notifications, name='view_notifications'),
	url(r'^twitter/$', views.twitter, name='twitter'),
	# url(r'^facebook/$', views.facebook, name='facebook'),
	url(r'^branches/$', views.branches, name='branches'),
	url(r'^branch_data/$',views.branch_data,name='branch_data'),
	url(r'^submit/$', views.submit, name='submit'),
	url(r'^analysis/$', views.analysis, name='analysis'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
