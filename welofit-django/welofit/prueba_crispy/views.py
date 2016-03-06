from django.shortcuts import render
from prueba_crispy.forms import SimpleForm, CartForm, CreditCardForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.http import HttpResponseBadRequest, HttpResponse, HttpRequest
import json
from django.contrib.auth.models import User
from django.core import serializers
import re
from diets_generator.models import Foods

def prueba(request):
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
            list_args.append(mc['prueba'])
            list_args.append(mc['meal'])
            day_foods.append(mc['food_proteins'])
            day_foods.append(mc['food_carbs'])
            day_foods.append(mc['food_fats'])
            day_quant.append(mc['gr_food1'])
            day_quant.append(mc['gr_food2'])
            day_quant.append(mc['gr_food3'])

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
        form = SimpleForm()

    context['form'] = form

    
    return render(request, 'prueba_crispy/index.html', context)