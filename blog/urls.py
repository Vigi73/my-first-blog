from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list_url'),
    path('post/<pk>/', views.post_detail, name='post_detail_url'),
]
