from django.contrib import admin
from diets_generator.models import Foods


# Register your models here.
class FoodsAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['food_name']}), ('Nutricional information', {'fields': ['gr_proteins', 'gr_carbs',
                                                                                         'gr_fats', 'calories']}),
                 ('Diet utilities', {'fields': ['food_weight', 'nutrient_highlight']}), ]

admin.site.register(Foods, FoodsAdmin)
