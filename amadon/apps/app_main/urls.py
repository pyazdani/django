from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^buy$', views.buy),
    url(r'^amadon/checkout$', views.amadon_checkout)
]

    # url(r'^buy/(?P<item_id>\d+)', views.buy),