from django.shortcuts import render
from django.http import HttpResponse

from .models import Demo

# Create your views here.

# def index(request):
#     #return HttpResponse("Hello Warsawa!")
#     return render(request, 'boilerplate/index.html')

def index(request):
    latest_demo_list = Demo.objects.all()
    context = {'latest_demo_list': latest_demo_list}
    return render(request, 'boilerplate/index.html', context)