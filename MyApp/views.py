from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello World')

def login(request):
    return HttpResponse('this is login page..')

def signup(request):
    return HttpResponse('Sign Up Here') 