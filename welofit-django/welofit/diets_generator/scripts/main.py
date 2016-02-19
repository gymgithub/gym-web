# -*- coding: utf-8 -*-
from dieta import Dieta
from optimizer import optimizer
from finder import finder
from compute import compute
import sys
import optparse


def parser_args(argv):
    parser = optparse.OptionParser(usage="usage: %prog -b <behavior> [options]")
    parser.add_option('-b', '--behavior', dest='behavior', nargs=1, help='overall,\
                                                                          optimize, finder')

    parser.add_option('-a', '--action', dest="action", nargs=1, help='compute, optimize, find')
    parser.add_option('-d', '--day', dest="day", nargs=1, help='monday, tuesday,...')
    parser.add_option('-m', '--meal', dest="meal", nargs=1, help='breakfast, lunch, appetizers, dinner')
    
    parser.add_option('-n', '--nutrients', dest="nutrients", nargs= 4, help='PCC, PGC, PC, PC')

    (opts, args) = parser.parse_args(argv[1:])
    if opts.behavior == "compute":
        print "hello"

    return opts


def main(argv=None):
    opts = parser_args(argv)
    test = opts.behavior

    dicc_output = {}
    week_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    meals_list = ["breakfast", "lunch", "appetizers", "dinner"]
    # Starting a Dieta object
    dieta_JM = Dieta(2800,30,50,20)
    
    # OVERALL behavior 
    if test == "overall":
        # Inputs from JS ??
        # food_list and quant_list need to be always a list of list (although sometimes we have only one element)
        # in order to be able to manage the usage of certain routines as a day rather than a meal
        food_list  = [["Pistachos","Clara de huevo","Cereales granola"]]
        quant_list = [["30","75","200"]]
        combo      = ["PCG"]
        
        # Instructions from JS??
        button = opts.action
        inst = {"day": week_list, "meal": meals_list, "button": button}
        
        if button == "compute":
            inst.update({"food_list": food_list, "quant_list": quant_list})
        elif button == "optimize":
            inst.update({"food_list": food_list})
        else:
            inst.update({"combo": combo})

        # Perform the demanded instructions
        for day in range(len(inst["day"])):
            if inst["day"][day] == opts.day:
                for meal in range(len(inst["meal"])):
                    if inst['meal'][meal] == opts.meal:
                        dieta_JM.list_days[day].list_meals[meal].execute(inst)
                        dicc_output['Proteins'] = (dieta_JM.list_days[day].list_meals[meal].P)
                        dicc_output['Carbohydrates'] = (dieta_JM.list_days[day].list_meals[meal].C)
                        dicc_output['Fats'] = (dieta_JM.list_days[day].list_meals[meal].G)
                        dicc_output['Food list'] = (dieta_JM.list_days[day].list_meals[meal].food_list)
                        dicc_output['Quantity list'] = (dieta_JM.list_days[day].list_meals[meal].quant_list)
    
    # PRESCRIBED food example
    if test == "optimizer":
        food_list  = [["Pistachos","Clara de huevo","Cereales granola"],
                 ["Pechuga de pollo","Arroz blanco","Tomate rojo"],
                 ["Atun en agua","Pan integral"],
                 ["Trucha","Patata cocida"]]
        
        const_list = [[dieta_JM.goals.P_break,dieta_JM.goals.C_break,dieta_JM.goals.G_break],
                 [dieta_JM.goals.P_lunch,dieta_JM.goals.C_lunch,dieta_JM.goals.G_lunch],
                 [dieta_JM.goals.P_appetizers,dieta_JM.goals.C_appetizers,dieta_JM.goals.G_appetizers],
                 [dieta_JM.goals.P_dinner,dieta_JM.goals.C_dinner,dieta_JM.goals.G_lunch]]
        
        quant_list = optimizer(food_list,const_list,dieta_JM.foodDB.food_total_list)
        nutrients  = compute(food_list,quant_list,dieta_JM.foodDB.food_total_list)
        
        dicc_output['nutrients'] = nutrients
        dicc_output['food_list'] = food_list
        dicc_output['quant_list'] = quant_list
        
    # RANDOM food example
    # Finder_settings example: {"breakfast": "PCG","lunch": "PPC","appetizers": "PC", "dinner": "PC"}
    if test == "finder":
        finder_settings = {}
        for i in opts.nutrients: 
            for meal in meals_list:
                finder_settings[meal] = i
        
        found = finder(finder_settings,dieta_JM.goals,dieta_JM.foodDB)
        food_list  = found[0]
        quant_list = found[1]
        nutrients  = compute(food_list,quant_list,dieta_JM.foodDB.food_total_list)
        
        dicc_output['nutrients'] = nutrients
        dicc_output['food_list'] = food_list
        dicc_output['quant_list'] = quant_list

    return dicc_output

if __name__ == "__main__":
    sys.exit(main(sys.argv))
    
    



