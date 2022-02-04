from django.http import HttpResponse


def list(request):
    return HttpResponse("<h1>Team Members</h1>")

def edit(request):
    return HttpResponse("<h1>Edit Team Member</h1>")

def add(request):
    return HttpResponse("<h1>Add Team Member</h1>")