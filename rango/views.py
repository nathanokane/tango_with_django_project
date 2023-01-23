from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    hyperlink_format = '<a href=/rango/about/>About</a>'
    response = hyperlink_format.format(link="/rango/about/", text='about')
    '<a href="/rango/about/">About</a>'
    return HttpResponse(response)

def about(request):
    return HttpResponse("This is the about page")
