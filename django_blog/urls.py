"""
	Urls for blog plugin
"""

from django.conf.urls import url
import django_blog.views as views

app_name = 'django_blog'
urlpatterns = [
    url(r'^$', views.PostView.as_view(), name='post'),
]
