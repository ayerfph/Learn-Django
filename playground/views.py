from django.shortcuts import render

#Import http
from django.http import HttpResponse

# Create your views here.
# Request -> Response - or called request handler to views.py


def hello_world(request):
    #return HttpResponse("Hello, World!")
    return render(request, 'hello.html',{'name': 'Jet'})