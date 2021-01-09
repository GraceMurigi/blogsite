from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.post, name='post'),
    path('<int:post_id>/comments/', views.comments, name='comments'),

] 