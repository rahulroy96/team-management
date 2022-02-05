from django.views.generic import (
    ListView,

)
from .models import Member
# from .forms import MemberForm

class MemberListView(ListView):
	model = Member
	template_name = 'members/members_list.html'
	context_object_name = 'members'
	ordering = ['-f_name']




