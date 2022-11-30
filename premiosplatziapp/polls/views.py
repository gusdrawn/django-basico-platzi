from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")

def detail(request, question_id):
    return HttpResponse("Hello World")

def results(request, question_id):
    return HttpResponse("Hello World")

def vote(request, question_id):
    return HttpResponse("Hello World")