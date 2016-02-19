from django.db import models


class Foods(models.Model):
    food_name = models.CharField(max_length=200)
    # gr x 100 gr
    gr_proteins = models.FloatField()
    gr_carbs = models.FloatField()
    gr_fats = models.FloatField()
    calories = models.FloatField()
    nutrient_highlight = models.CharField(max_length=1  )
    food_weight = models.IntegerField()

    class Meta:
        verbose_name = 'Foods'
        verbose_name_plural = 'Foods'

    def __str__(self):
        return self.food_name


class DietInputs(models.Model):
    calories = models.FloatField()
    proteins_percentage = models.FloatField()
    carbs_percentage = models.FloatField()
    fats_percentage = models.FloatField()

