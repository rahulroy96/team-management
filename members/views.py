from django.views.generic import (
    ListView,
    CreateView,
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


