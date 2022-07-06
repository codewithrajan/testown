from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>hello world\nits my first django programs</h1>")   #it also be allowed
