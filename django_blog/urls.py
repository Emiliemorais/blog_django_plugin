"""
	Urls for blog plugin
"""

from django.conf.urls import url
from views import PostView

urlpatterns = [
    url(r'^new_post/', PostView.as_view(), name="new_post"),
]
