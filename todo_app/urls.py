from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('list_view/', views.list_view, name='list_view'),
    path('delete/<int:i>/', views.delete ,name='delete'),
]