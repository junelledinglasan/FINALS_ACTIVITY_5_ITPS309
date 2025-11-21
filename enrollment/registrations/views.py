from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.

def registration_list(request):
    return HttpRequest('List of Registration:')

def registration_details(request):
    return HttpRequest('Registration Details')


