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
    food_proteins = forms.ChoiceField(label="Proteins foods", choices=items_p)
    food_carbs = forms.ChoiceField(label="Carbs foods", choices=items_c)
    food_fats = forms.ChoiceField(label="Fats foods", choices=items_g)

    combo = forms.CharField()

    gr_food1 = forms.FloatField()
    gr_food2 = forms.FloatField()
    gr_food3 = forms.FloatField()

    meal = forms.CharField()
    day = forms.CharField()
    calories = forms.FloatField()
    proteins = forms.FloatField()
    carbs = forms.FloatField()
    fats = forms.FloatField()
