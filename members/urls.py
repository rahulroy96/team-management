from django.urls import path
from .views import (
	MemberListView, 
	MemberCreateView, 
)

urlpatterns = [
	path('', MemberListView.as_view(), name='members-list'),
	path('add/', MemberCreateView.as_view(), name='member-add')
]