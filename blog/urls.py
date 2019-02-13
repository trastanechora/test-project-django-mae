from django.urls import path
from . import views

urlpatterns = [
   path('blog', views.db_blog, name='blog'),
]
