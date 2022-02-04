from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. You're at the team members home page.")