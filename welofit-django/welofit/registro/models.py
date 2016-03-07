from __future__ import unicode_literals

from django.db import models

class user_data_model(models.Model):
    GENDER_CHOICES = (
        ('M', 'male'),
        ('F', 'female')
    )
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=300)
    birthdate = models.DateField
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    country = models.CharField
    city = models.CharField

class fitness_data_model(models.Model):
    PLACE_CHOICES = (
        ('0', 'Gym'),
        ('1', 'Out'),
        ('2', 'Home')
    )
    EQUIP_CHOICES = (
        ('0', 'Dumbbell'),
        ('1', 'Bench')
    )
    CHAT_CHOICES = (
        ('0', '10:00 ~ 12:00'),
        ('1', '12:00 ~ 14:00'),
        ('2', '14:00 ~ 16:00'),
        ('3', '16:00 ~ 18:00'),
        ('4', '18:00 ~ 20:00'),
        ('5', '20:00 ~ 22:00'),
    )  
    BIO_CHOICES = (
        ('0', 'No'),
        ('1', 'Yes')
    )    
    training_place = models.CharField(max_length = 1, choices=PLACE_CHOICES)
    food_intolerance = models.CharField(max_length = 1000)
    equipment = models.CharField(max_length = 1, choices=EQUIP_CHOICES)
    chat_availability = models.CharField(max_length = 1, choices=CHAT_CHOICES)
    fitness_bio = models.CharField(max_length = 1, choices=BIO_CHOICES)
    
class body_data_model(models.Model):
    GOALS_CHOICES = (
        ('0', 'build muscle'),
        ('1', 'lose weight'),
        ('2', 'muscle tone')
    )
    ACTIVITY_CHOICES = (
        ('0', 'Office worker getting little or no exercise'),
        ('1', 'Construction worker or person running one hour daily'),
        ('2', 'Agricultural worker (non mechanized) or person swimming two hours daily'),
        ('3', 'Competitive cyclist')
    )
    height = models.FloatField
    weight = models.FloatField
    goals = models.CharField(max_length = 1, choices=GOALS_CHOICES)
    activity_level = models.CharField(max_length = 1, choices=ACTIVITY_CHOICES)
    