from django.forms import ModelForm
from django import forms
from diets_generator.models import Foods
import json
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div, Fieldset

class ListFoods:
    class SearchFoods(forms.Form):
        foods_object = Foods.objects.all()
        list_foods = []
        list_calories = []
        for i in foods_object:
            list_foods.append(i.food_name)
            list_calories.append(i.calories)
        dict_foods = tuple(zip(list_foods, list_calories))

        food_all = forms.ChoiceField(widget=forms.Select, choices=dict_foods)

    class Food(forms.Form):
        foods = Foods.objects.all()
        items_p = []
        tuple_p = ()
        items_c = []
        tuple_c = []
        items_g = []
        tuple_g = ()
        for i in range(len(foods)):
            if foods[i].nutrient_highlight == 'P':
                tuple_p = (foods[i].food_name, foods[i].food_name)
                items_p.append(tuple_p)
            elif foods[i].nutrient_highlight == 'C':
                tuple_c = (foods[i].food_name, foods[i].food_name)
                items_c.append(tuple_c)
            elif foods[i].nutrient_highlight == 'G':
                tuple_g = (foods[i].food_name, foods[i].food_name)
                items_g.append(tuple_g)   

        food_proteins = forms.ChoiceField(label="Proteins foods", choices=items_p, widget=forms.Select(attrs={'class' : 'form-control'}))
        food_carbs = forms.ChoiceField(label="Carbs foods", choices=items_c, widget=forms.Select(attrs={'class' : 'form-control'}))
        food_fats = forms.ChoiceField(label="Fats foods", choices=items_g, widget=forms.Select(attrs={'class' : 'form-control'}))
        combo = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
        gr_food1 = forms.FloatField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
        gr_food2 = forms.FloatField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
        gr_food3 = forms.FloatField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
        meal = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
        day = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
        calories = forms.FloatField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
        proteins = forms.FloatField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
        carbs = forms.FloatField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
        fats = forms.FloatField(widget=forms.TextInput(attrs={'class' : 'form-control'})) 
        
        helper = FormHelper()
        helper.layout = Layout(
            Fieldset(
                'Foods',
                Div(
                    'food_proteins',
                    css_class="col-sm-4"
                ),
                Div(
                    'food_carbs',
                    css_class="col-sm-4"
                ),
                Div(
                    'food_fats',
                    css_class="col-sm-4"
                )                
            ),
            Fieldset(
                'Food Settings',
                Div(
                    'combo',
                    css_class="col-sm-3"
                ),
                Div(
                    'gr_food1',
                    css_class="col-sm-3"
                ),
                Div(
                    'gr_food2',
                    css_class="col-sm-3"
                ),
                Div(
                    'gr_food3',
                    css_class="col-sm-3"
                )
            ),
            Fieldset(
                'Food Time',
                Div(
                    'meal',
                    css_class="col-sm-3 col-sm-offset-2"
                ),
                Div(
                    'day',
                    css_class="col-sm-3 col-sm-offset-2"
                )
            ),
            Fieldset(
                'Food Attributes',
                Div(
                    'calories',
                    css_class="col-sm-3"
                ),
                Div(
                    'proteins',
                    css_class="col-sm-3"
                ),
                Div(
                    'carbs',
                    css_class="col-sm-3"
                ),
                Div(
                    'fats',
                    css_class="col-sm-3"
                )
            )
        )


