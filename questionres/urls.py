from django.contrib import admin
from django.urls import path,re_path
from .views import quedemo,questionEdit,questionDelete,questionDetail,allQuestions,addQuestion,questionUpdate
urlpatterns = [
    re_path('^$',quedemo,name="quedemo"),
    re_path(r'all/',allQuestions,name="AllQuestions"),
    re_path(r'edit/(?P<id>[0-9]+)',questionEdit,name="QuestionEdit"),
    re_path(r'update/(?P<id>[0-9]+)',questionUpdate,name="QuestionUpdate"),
    re_path(r'detail/(?P<id>[0-9]+)',questionDetail,name="QuestionDetail"),
    re_path(r'delete/(?P<id>[0-9]+)',questionDelete,name="QuestionDelete"),
    re_path(r'addQuestion',addQuestion,name="AddQuestion"),
]