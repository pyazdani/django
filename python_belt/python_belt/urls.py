from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.login.urls')),
    url(r'^', include('apps.quotes.urls'))
]