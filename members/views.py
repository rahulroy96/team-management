from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from .models import Member
from .forms import MemberForm
from django.urls import reverse_lazy


class MemberListView(ListView):
    model = Member
    template_name = "members/members_list.html"
    context_object_name = "members"
    ordering = ["-f_name"]


class MemberCreateView(CreateView):
    model = Member
    form_class = MemberForm
    template_name = "members/member_add.html"
    success_url = reverse_lazy("members-list")


class MemberUpdateView(UpdateView):
    model = Member
    form_class = MemberForm
    template_name = "members/member_edit.html"
    success_url = reverse_lazy("members-list")


class MemberDeleteView(DeleteView):
    model = Member
    context_object_name = "member"
    success_url = reverse_lazy("members-list")
