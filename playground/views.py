from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def playground(request):
    return HttpResponse("This is a playground app")


def show_my_name(request):
    return render(request, 'playground/welcome.html', {'stadium': 'Stamford Bridge'})
