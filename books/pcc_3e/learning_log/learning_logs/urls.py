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
    # 用户添加新的主题
    path('new_topic/', views.new_topic, name='new_topic'),
    # 添加新条目
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
    # 编辑条目
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]