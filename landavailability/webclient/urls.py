from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from webclient import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(
        r'^login/$',
        auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]
