from django.urls import path, re_path
from . import views
import re

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^shorten$', views.shorten, name='shorten'),
    re_path(r'^shorten/$', views.shorten, name='shorten'),
    re_path(r'^(?P<short_string>[a-zA-Z0-9]{7})$', views.resolve, name='resolve'),
    re_path(r'^(?P<short_string>[a-zA-Z0-9]{7})/$', views.resolve, name='resolve'),
]