from django.shortcuts import render

from django.http import HttpResponse
from diets_generator.models import Foods
from scripts import main
import json


def dashboard_generator(request):
    list_foods = Foods.objects.all()
    ua = request.META['HTTP_USER_AGENT']



    list_args = ['compute', 'monday', 'breakfast']


    complete_food_list = []
    complete_quant_list = []
    quant_list = []
    food_list = []
    combo = []
    calories = request.POST['calories']
    proteins = request.POST['proteins']
    carbs = request.POST['carbs']
    fats = request.POST['fats']
    for i, v in request.POST.items():
        if i == "protein_food":
            food_list.append(v)
        elif i == "carbs_food":
            food_list.append(v)
        elif i == "fats_food":
            food_list.append(v)
        elif i == "gr_protein":
            quant_list.append(v)
        elif i == "gr_carbs":
            quant_list.append(v)
        elif i == "gr_fats":
            quant_list.append(v)

    complete_quant_list.append(quant_list)
    complete_food_list.append(food_list)
    print complete_food_list
    print complete_quant_list
    combo.append(request.POST['combo'])

    #output_str = json.dumps(main.main(list_args, complete_food_list, complete_quant_list, combo, calories,
    #                                  proteins, carbs, fats))

    #print output_str

    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        foods = Foods.objects.filter(food_name__icontains=q)
        for i in foods:
            if request.GET['q'] == i.food_name:
                mensaje = request.GET['q'] + " has " + str(i.gr_proteins) + " gr of proteins"
                break
            else:
                mensaje = "papafrita"
    else:
        mensaje = 'Has subido un formulario vacio.'

    context = {'list_foods': list_foods, 'UA': ua, 'mensaje': mensaje}

    return render(request, 'diets_generator/index.html', context)

