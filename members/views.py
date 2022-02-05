from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Member


class MemberListView(ListView):
	model = Member
	template_name = 'members/members_list.html'
	context_object_name = 'members'
	ordering = ['-f_name']


class MemberCreateView(CreateView):
    model = Member
    fields = ['f_name', 'l_name', 'email', 'phone_number', 'role']
    template_name = 'members/member_add.html'
    success_url = '/'


class MemberUpdateView(UpdateView):
    model = Member
    fields = ['f_name', 'l_name', 'email', 'phone_number', 'role']
    template_name = 'members/member_edit.html'
    success_url = '/'


class MemberDeleteView(DeleteView):
    model = Member
    context_object_name = 'member'
    success_url = '/'


