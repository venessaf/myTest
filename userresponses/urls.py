from django.contrib import admin
from django.urls import path,re_path
from .views import uresdemo,allResponses
urlpatterns = [
    re_path('^$',uresdemo,name="uresdemo"),
    re_path('all',allResponses,name="AllResponses"),
]