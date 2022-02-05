from django.urls import path
from .views import MemberListView, MemberCreateView, MemberUpdateView, MemberDeleteView

urlpatterns = [
    path("", MemberListView.as_view(), name="members-list"),
    path("member/add/", MemberCreateView.as_view(), name="member-add"),
    path("member/<int:pk>/", MemberUpdateView.as_view(), name="member-edit"),
    path("member/<int:pk>/delete", MemberDeleteView.as_view(), name="member-delete"),
]
