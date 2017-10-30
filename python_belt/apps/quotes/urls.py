from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^quotes$', views.quotes),
    url(r'^quotes/add$', views.add),
    url(r'^users/(?P<user_name>\d+)$', views.library),
    url(r'^quotes/fav/(?P<quote_id>\d+)$', views.fav),
    url(r'^quotes/remove/(?P<quote_id>\d+)$', views.remove)
]