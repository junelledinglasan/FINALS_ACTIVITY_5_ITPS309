from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.

def courses(request):
    return HttpRequest('Name of Courses:')

def courses_name(request):
    return HttpRequest('BSIT')


