from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome! Kindly read the README file for more information.")