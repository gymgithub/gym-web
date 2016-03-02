from django.forms import ModelForm
from django import forms
from diets_generator.models import Foods


class ListFoods(forms.Form):

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
            
    food_proteins = forms.ChoiceField(label="Proteins foods", choices=items_p, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    food_carbs = forms.ChoiceField(label="Carbs foods", choices=items_c, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    food_fats = forms.ChoiceField(label="Fats foods", choices=items_g, widget=forms.TextInput(attrs={'class' : 'form-control'}))

    combo = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))

    gr_food1 = forms.FloatField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    gr_food2 = forms.FloatField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    gr_food3 = forms.FloatField(widget=forms.TextInput(attrs={'class' : 'form-control'}))

    meal = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    day = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    prueba = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    calories = forms.FloatField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    proteins = forms.FloatField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    carbs = forms.FloatField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    fats = forms.FloatField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
