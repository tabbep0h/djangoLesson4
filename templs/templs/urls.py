from django.contrib import admin
from django.urls import path,include,re_path
from templsapp import views

inc = [
    re_path(r'^$', views.index),
    re_path(r"^about",views.about),
    re_path(r"^contacts",views.contacts),
    re_path(r"^form",views.form)
]
urlpatterns = [
    re_path(r"^", include(inc))
]

