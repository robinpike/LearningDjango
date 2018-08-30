"""
Definition of urls for BasicProject.
"""

from datetime import datetime
from django.conf.urls import include, url
import django.contrib.auth.views
import HelloDjangoApp.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

#Djnago processes patterns in the order in which they appear in the array
urlpatterns = [
    url(r'^$', HelloDjangoApp.views.index, name='index'),
    url(r'^about$', HelloDjangoApp.views.about, name='about'),
    url(r'^$', app.views.home, name='home')
]
