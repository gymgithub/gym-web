from django.shortcuts import render

from django.http import HttpResponse
from diets_generator.models import Foods
from scripts import main


def dashboard_generator(request):
    list_foods = Foods.objects.all()
    print dir(main)
    output = []
    for i in list_foods:
        output.append(i.food_name)

    output_str = ", ".join(output)

    return HttpResponse(output_str)


def compute(request):
    return HttpResponse("Hola mundo. Esta es la vista de Compute")


def optimize(request):
    return HttpResponse("Esta es la vista de optimizer")


def find(request):
    return HttpResponse("esta es la vista de find")

