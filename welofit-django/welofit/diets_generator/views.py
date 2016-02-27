from django.shortcuts import render

from django.http import HttpResponse
from diets_generator.models import Foods
from scripts import main
import json
from diets_generator.forms import ListFoods


def dashboard_generator(request):
    context = {}
    list_foods = []
    day_foods = []
    list_quants = []
    day_quant = []
    list_args = []
    list_nutrients = []

    foods_objects = Foods.objects.all()

    for i in foods_objects:
        if i.nutrient_highlight == 'P':
            protein_food = i.food_name
        elif i.nutrient_highlight == 'C':
            carb_food = i.food_name
        elif i.nutrient_highlight == 'G':
            fat_food = i.food_name

    context['list_foods'] = list_foods

    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        foods = Foods.objects.filter(food_name__icontains=q)
        for i in foods:
            if request.GET['q'] == i.food_name:
                list_nutrients.append(str(i.gr_proteins) + " gr of proteins")
                list_nutrients.append(str(i.gr_carbs) + " gr of carbs")
                list_nutrients.append(str(i.gr_fats) + " gr of fats")
                break
    else:
        mensaje = 'Has subido un formulario vacio.'
        context['mensaje'] = mensaje

    if request.method == 'POST':
        for i, v in request.POST.items():
            if i == 'compute':
                list_args.append(v)
            elif i == 'optimize':
                list_args.append(v)
            elif i == 'find':
                list_args.append(v)

        form = ListFoods(request.POST)

        if form.is_valid():
            mc = form.cleaned_data
            print mc
            list_args.append(mc['day'])
            list_args.append(mc['meal'])
            day_foods.append(mc['food_proteins'])
            day_foods.append(mc['food_carbs'])
            day_foods.append(mc['food_fats'])
            day_quant.append(mc['gr_food1'])
            day_quant.append(mc['gr_food2'])
            day_quant.append(mc['gr_food3'])

            print list_args
            list_foods.append(day_foods)
            list_quants.append(day_quant)
            output_str = main.main(list_args, list_foods, list_quants, mc['combo'], mc['calories'], mc['proteins'],
                                    mc['carbs'], mc['fats'])

            output_html = json.dumps(output_str)
            context['list_args'] = list_args
            context['output_html'] = output_html
        else:
            print "no valido"

    else:

        form = ListFoods()
    context['form'] = form

    context['list_nutrients'] = list_nutrients

    return render(request, 'diets_generator/index.html', context)

