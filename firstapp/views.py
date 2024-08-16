from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("<h2>Главная</h2>")

def about(request):
    return HttpResponse("<h2>О нас</h2>")

def contact(request):
    return HttpResponse("<h2>О нас</h2>")

def products(request, productid):
    output = "<h2>Продукт № {0}</h2>".format(productid)
    return HttpResponse(output)
def users(request, id, name):
    output = "<h2>Пользовательн</h2><h3>id = {0}, имя - {1}</h3>".format(id, name)
    return HttpResponse(output)

def phone(request, variable_name):
   output = "<h2>You're phone number - {0}</h2>".format(variable_name)
   return HttpResponse(output)