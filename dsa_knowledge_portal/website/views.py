from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse('Welcome to DSA Knowledge Portal!')

def about(request):
    return HttpResponse('Hi!, my name is Shivam')
