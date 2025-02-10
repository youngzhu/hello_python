"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # 所有主题
    path('topics/', views.topics, name='topics'),
    # 指定主题
    path('topics/<int:topic_id>', views.topic, name='topic'),
]