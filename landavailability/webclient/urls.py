from django.conf.urls import url
from webclient import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^login/$', views.HomePageView.as_view(), name='login'),
]
