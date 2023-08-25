from django.http import HttpResponse

def hello(request):
    return HttpResponse("hey, I LOVE YOU!!!!")
from django.shortcuts import render

# Create your views here.
