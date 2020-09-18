from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def hydjobs(request):
    s='<h1>Hyderabad jobs information</h1>'
    return HttpResponse(s)

def chennaijobsInfo(request):
    s='<h1>Chennai jobs information</h1>'
    return HttpResponse(s)

def punejobsInfo(request):
    s='<h1>Pune jobs information</h1>'
    return HttpResponse(s)

def hello(request):
    s='<h1> Hello "+" World    "+" to all   "+"  saman</h1>'
    return HttpResponse(s)
