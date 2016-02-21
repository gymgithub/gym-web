# -*- coding: utf-8 -*-
from dieta import Dieta
import sys


def main(list_inputs, food_list, quant_list, combo, calories,
         proteins, carbs, fats):
    output = {}
    week_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    meals_list = ["breakfast", "lunch", "appetizers", "dinner"]
    # Starting a Dieta object
    dieta_jm = Dieta(calories, proteins, carbs, fats)
    # food_list and quant_list need to be always a list of list (although sometimes we have only one element)

    button = list_inputs[0]
    inst = {"day": week_list, "meal": meals_list, "button": button}
        
    if button == "compute":
        inst.update({"food_list": food_list, "quant_list": quant_list})
    elif button == "optimize":
        inst.update({"food_list": food_list})
    else:
        inst.update({"combo": combo})

    # Perform the demanded instructions
    for day in range(len(inst["day"])):
        if inst["day"][day] == list_inputs[1]:
            for meal in range(len(inst["meal"])):
                if inst['meal'][meal] == list_inputs[2]:
                    dieta_jm.list_days[day].list_meals[meal].execute(inst)
                    output['Proteins'] = dieta_jm.list_days[day].list_meals[meal].P
                    output['Carbohydrates'] = dieta_jm.list_days[day].list_meals[meal].C
                    output['Fats'] = dieta_jm.list_days[day].list_meals[meal].G
                    output['Food list'] = dieta_jm.list_days[day].list_meals[meal].food_list
                    output['Quantity list'] = dieta_jm.list_days[day].list_meals[meal].quant_list
    return output

if __name__ == "__main__":
    sys.exit(main(list_inputs))
    
    



