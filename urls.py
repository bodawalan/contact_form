from django.conf.urls import url,include
from django.contrib import admin

from . import views

app_name='user'
urlpatterns = [
    url(r'^form_view', views.form_view,name='form_view'),
    url(r'^showform/',views.showform,name='showform'),
]