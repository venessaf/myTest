from django.contrib import admin
from django.urls import path,re_path
from .views import accdemo,userEdit,userDelete,userDetail,allUsers,addUser,userUpdate
urlpatterns = [
    re_path(r'^$',accdemo,name="accdemo"),
    re_path(r'all/',allUsers,name="AllUsers"),
    re_path(r'edit/(?P<id>[0-9]+)',userEdit,name="UserEdit"),
    re_path(r'update/(?P<id>[0-9]+)',userUpdate,name="UserUpdate"),
    re_path(r'detail/(?P<id>[0-9]+)',userDetail,name="UserDetail"),
    re_path(r'delete/(?P<id>[0-9]+)',userDelete,name="UserDelete"),
    re_path(r'adduser',addUser,name="AddUser"),
]