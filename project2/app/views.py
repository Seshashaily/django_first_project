from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
# Create your views here.
def sesha(request):
    return HttpResponse('<marquee><h2>sesha selected in tcs company!............</h2></marquee>')
def sneha(request):
    return HttpResponse('<h1>sneha is my best sis</h1>')