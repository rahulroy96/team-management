from django.urls import path
from . import views

urlpatterns = [
	path('', views.list, name='members-list'),
	path('edit/', views.edit, name='members-edit'),
	path('add/', views.add, name='members-add')
]