from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^users/new$', views.new_user),
	url(r'^session/new$', views.new_session),
	url(r'^session/delete$', views.logout),
	url(r'^quotes$', views.quotes), 
	url(r'^quotes/add$', views.add),
]