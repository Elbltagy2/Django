from django.shortcuts import render
from django.http import HttpResponse 
from main.models import TodoList,memeber
from django.template import loader

def index(request): 
    members=memeber.objects.all()
    template = loader.get_template('myfirst.html')
    contex={
        'members':members
    }
    return HttpResponse(template.render(contex,request))

def index1(response,id): 
    ls=TodoList.objects.get(id=id)
    return HttpResponse("<h1>%s</h1>"%ls.name)

def details(request,id):
    m=memeber.objects.get(id=id)
    templet=loader.get_template('details.html')
    context={
        'memeber':m
    }
    return HttpResponse(templet.render(context,request))
# Create your views here.
