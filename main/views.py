from django.shortcuts import render
from django.http import HttpResponse 
from main.models import TodoList

def index(response): 
    return HttpResponse("hello world")
def index1(response,id): 
    ls=TodoList.objects.get(id=id)
    return HttpResponse("<h1>%s</h1>"%ls.name)

# Create your views here.
