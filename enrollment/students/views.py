from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.

def student_list(request):
    return HttpRequest('List of Student:')

def student_details(request):
    return HttpRequest('Student Details')