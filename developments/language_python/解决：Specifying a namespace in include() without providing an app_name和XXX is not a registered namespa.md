是在app中urls.py加那一行，
from django.urls import path, include, re_path
from . import views
app_name = 'blog'
urlpatterns = [
path('index/', views.index),
#path('article/', views.article_page),
path('article/<int:article_id>/', views.article_page, name='article_id'),

] 
