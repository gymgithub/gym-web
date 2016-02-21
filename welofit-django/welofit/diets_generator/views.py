from django.shortcuts import render

from django.http import HttpResponse
from diets_generator.models import Foods
from scripts import main
import json


def dashboard_generator(request):
    list_foods = Foods.objects.all()
    output = []

    list_args = ['compute', 'monday', 'breakfast']
    food_list = [["Pistachos", "Clara de huevo", "Cereales granola"]]
    quant_list = [["32", "75", "250"]]
    combo = ['PGC']
    output_str = json.dumps(main.main(list_args, food_list, quant_list,
                                      combo, 2800, 30, 10, 20))

    return HttpResponse(output_str)


def compute(request):
    return HttpResponse("Hola mundo. Esta es la vista de Compute")


def optimize(request):
    return HttpResponse("Esta es la vista de optimizer")


def find(request):
    return HttpResponse("esta es la vista de find")

