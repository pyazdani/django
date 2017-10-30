from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^users/new$', views.new_user),
	url(r'^session/new$', views.new_session),
	url(r'^session/delete$', views.logout),
	url(r'^travels$', views.travels), 
	url(r'^travels/add$', views.add),
	url(r'^process$', views.process),
	url(r'^travels/join/(?P<id>\d+)$', views.join),
	url(r'^travels/leave/(?P<id>\d+)$', views.leave),
	url(r'^travels/destination/(?P<id>\d+)$', views.destination),
]
