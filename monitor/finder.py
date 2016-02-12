# -*- coding: utf-8 -*-

import csv
import numpy as np
from scipy.optimize import minimize
from operator import itemgetter
from optimizer import optimizer
import random

def finder (settings,goals,foodDB):
    
    Prot_rich_soft   = foodDB.Prot_rich_soft
    Prot_rich_heavy  = foodDB.Prot_rich_heavy
    Carbo_rich_soft  = foodDB.Carbo_rich_soft
    Carbo_rich_heavy = foodDB.Carbo_rich_heavy
    Grasa_rich_soft  = foodDB.Grasa_rich_soft
    Grasa_rich_heavy = foodDB.Grasa_rich_heavy

    # Randon choices (for now, it can be repeated food)
    food_list  = []
    const_list = []
    if "breakfast" in settings:
        breakfast_list = []
        food_settings = settings["breakfast"]
        nfood = len(food_settings)
        for i in range(0,nfood):
            letter = food_settings[i]
            if letter == "P":
                temp_list = random.choice(Prot_rich_soft)
            elif letter == "C":
                temp_list = random.choice(Carbo_rich_soft)
            else:
                temp_list = random.choice(Grasa_rich_soft)
            breakfast_list.append(temp_list[0])
        food_list.append(breakfast_list)
        breakfast_const = []
        breakfast_const.append(goals.P_break)
        breakfast_const.append(goals.C_break)
        breakfast_const.append(goals.G_break)
        const_list.append(breakfast_const)
    
    if "lunch" in settings:
        lunch_list = []
        food_settings = settings["lunch"]
        nfood = len(food_settings)
        for i in range(0,nfood):
            letter = food_settings[i]
            if letter == "P":
                temp_list = random.choice(Prot_rich_heavy)
            elif letter == "C":
                temp_list = random.choice(Carbo_rich_heavy)
            else:
                temp_list = random.choice(Grasa_rich_heavy)
            lunch_list.append(temp_list[0])
        food_list.append(lunch_list)
        lunch_const = []
        lunch_const.append(goals.P_lunch)
        lunch_const.append(goals.C_lunch)
        lunch_const.append(goals.G_lunch)
        const_list.append(lunch_const)          

    if "appetizers" in settings:
        appetizers_list = []
        food_settings = settings["appetizers"]
        nfood = len(food_settings)
        for i in range(0,nfood):
            letter = food_settings[i]
            if letter == "P":
                temp_list = random.choice(Prot_rich_soft)
            elif letter == "C":
                temp_list = random.choice(Carbo_rich_soft)
            else:
                temp_list = random.choice(Grasa_rich_soft)
            appetizers_list.append(temp_list[0])
        food_list.append(appetizers_list)
        appetizers_const = []
        appetizers_const.append(goals.P_appetizers)
        appetizers_const.append(goals.C_appetizers)
        appetizers_const.append(goals.G_appetizers)
        const_list.append(appetizers_const)
    
    if "dinner" in settings:
        dinner_list = []
        food_settings = settings["dinner"]
        nfood = len(food_settings)
        for i in range(0,nfood):
            letter = food_settings[i]
            if letter == "P":
                temp_list = random.choice(Prot_rich_heavy)
            elif letter == "C":
                temp_list = random.choice(Carbo_rich_heavy)
            else:
                try:
                    temp_list = random.choice(Grasa_rich_heavy)
                except IndexError:
                    print "petaaaaa", "--> ", Grasa_rich_heavy
            dinner_list.append(temp_list[0])
        food_list.append(dinner_list)
        dinner_const = []
        dinner_const.append(goals.P_dinner)
        dinner_const.append(goals.C_dinner)
        dinner_const.append(goals.G_dinner)
        const_list.append(dinner_const) 
        
    quant_list = optimizer (food_list,const_list,foodDB.food_total_list)
    found = []
    found.append(food_list)
    found.append(quant_list)
    
    return found
                
                
