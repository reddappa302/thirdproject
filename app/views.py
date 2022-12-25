from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('my first application')

def second(request):
    return HttpResponse('<h1><marquee>Iam Inevitable</marquee></h1>')    
