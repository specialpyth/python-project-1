from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('object/<int:object_id>/', views.detail, name='detail'),
]
