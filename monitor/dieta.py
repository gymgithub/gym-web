# -*- coding: utf-8 -*-

import csv
from compute import compute
from optimizer import optimizer
from finder import finder

class User:
    def __init__(self,name,weight,height):
        self.name   = name
        self.weight = weight
        self.height = height

# Dieta constants
class Dieta_const:
    def __init__(self):
        self.gr2cal_P       = 4
        self.gr2cal_C       = 4
        self.gr2cal_G       = 9
        self.gr_IMCless_P   = 2.5
        self.gr_IMCless_C   = 4
        self.gr_IMClmore_P  = 3
        self.gr_IMClmore_C  = 2

# Dieta nutrients day distribution constants
class Dieta_dist:
    def __init__(self):
        self.P_break      = 30
        self.P_lunch      = 25
        self.P_appetizers = 20
        self.P_dinner     = 25
        self.C_break      = 50
        self.C_lunch      = 30
        self.C_appetizers = 15
        self.C_dinner     =  5
        self.G_break      = 20
        self.G_lunch      = 25
        self.G_appetizers = 40
        self.G_dinner     = 15

# Dieta food data base
class Dieta_foodDB(object):
    def __init__ (self):
        # Import food database
        with open('alimentosDB.csv', 'r') as f:
            reader = csv.reader(f)
            food_total_list = list(reader)
            
        # Clasifying w.r.t main nutrient
        nfood = len(food_total_list)
        Prot_rich  = []
        Carbo_rich = []
        Grasa_rich = []
        for i in range(0,nfood):
            if food_total_list[i][6] == "P" :
                Prot_rich.append(food_total_list[i][0:6])
            elif food_total_list[i][6] == "C" :
                Carbo_rich.append(food_total_list[i][0:6])
            else :
                Grasa_rich.append(food_total_list[i][0:6])    
        
        # Clasifying w.r.t type of meal
        nPfood = len(Prot_rich)
        nCfood = len(Carbo_rich)
        nGfood = len(Grasa_rich)
        Prot_rich_soft   = []
        Prot_rich_heavy  = []
        Carbo_rich_soft  = []
        Carbo_rich_heavy = []
        Grasa_rich_soft  = []
        Grasa_rich_heavy = []
        for i in range(0,nPfood):
            if Prot_rich[i][5] == "1" :
                Prot_rich_soft.append(Prot_rich[i][0:4])
            else:
                Prot_rich_heavy.append(Prot_rich[i][0:4])
        for i in range(0,nCfood):
            if Carbo_rich[i][5] == "1" :
                Carbo_rich_soft.append(Carbo_rich[i][0:4])
            else:
                Carbo_rich_heavy.append(Carbo_rich[i][0:4])
        for i in range(0,nGfood):
            if Grasa_rich[i][5] == "1" :
                Grasa_rich_soft.append(Grasa_rich[i][0:4])
            else:
                Grasa_rich_heavy.append(Grasa_rich[i][0:4]) 
         
        self.food_total_list  =  food_total_list
        self.Prot_rich        =  Prot_rich
        self.Prot_rich_soft   =  Prot_rich_soft
        self.Prot_rich_heavy  =  Prot_rich_heavy
        self.Carbo_rich       =  Carbo_rich
        self.Carbo_rich_soft  =  Carbo_rich_soft
        self.Carbo_rich_heavy =  Carbo_rich_heavy
        self.Grasa_rich       =  Grasa_rich
        self.Grasa_rich_soft  =  Grasa_rich_soft
        self.Grasa_rich_heavy =  Grasa_rich_heavy
           

class Dieta_goals(object):
    def __init__(self,const,dist,Kcal,P,C,G):
        self.Kcal_goal     = Kcal
        self.P_goal_perc   = P
        self.P_goal_cal    = P/100*Kcal
        self.P_goal_gr     = self.P_goal_cal/const.gr2cal_P
        self.C_goal_perc   = C
        self.C_goal_cal    = C/100*Kcal
        self.C_goal_gr     = self.C_goal_cal/const.gr2cal_C
        self.G_goal_perc   = G        
        self.G_goal_cal    = G/100*Kcal
        self.G_goal_gr     = self.G_goal_cal/const.gr2cal_G        
        self.P_break       = dist.P_break/100*self.P_goal_gr
        self.P_lunch       = dist.P_lunch/100*self.P_goal_gr
        self.P_appetizers  = dist.P_appetizers/100*self.P_goal_gr
        self.P_dinner      = dist.P_dinner/100*self.P_goal_gr
        self.C_break       = dist.C_break/100*self.C_goal_gr
        self.C_lunch       = dist.C_lunch/100*self.C_goal_gr
        self.C_appetizers  = dist.C_appetizers/100*self.C_goal_gr
        self.C_dinner      = dist.C_dinner/100*self.C_goal_gr
        self.G_break       = dist.G_break/100*self.G_goal_gr
        self.G_lunch       = dist.G_lunch/100*self.G_goal_gr
        self.G_appetizers  = dist.G_appetizers/100*self.G_goal_gr
        self.G_dinner      = dist.G_dinner/100*self.G_goal_gr

class Dieta_days(object):
    def __init__(self,goals,foodDB):
        self.list_meals = []
        const_list_break      = [goals.P_break,goals.C_break,goals.G_break]
        const_list_lunch      = [goals.P_lunch,goals.C_lunch,goals.G_lunch]
        const_list_appetizers = [goals.P_appetizers,goals.C_appetizers,goals.G_appetizers]
        const_list_dinner     = [goals.P_dinner,goals.C_dinner,goals.G_dinner]
        
        self.breakfast  = Dieta_meals(goals,foodDB,const_list_break,"breakfast")
        self.lunch      = Dieta_meals(goals,foodDB,const_list_lunch,"lunch")
        self.appetizers = Dieta_meals(goals,foodDB,const_list_appetizers,"appetizers")
        self.dinner     = Dieta_meals(goals,foodDB,const_list_dinner,"dinner")

        self.list_meals.append(self.breakfast)
        self.list_meals.append(self.lunch)
        self.list_meals.append(self.appetizers)
        self.list_meals.append(self.dinner)


class Dieta_meals(object):
    def __init__(self,goals,foodDB,const_list, name):
        self.food_list  = []
        self.quant_list = []
        self.name       = name
        self.const_list = const_list
        self.goals      = goals
        self.foodDB     = foodDB
        self.P          = 0
        self.C          = 0
        self.G          = 0
        
    def execute(self,inst):
        if inst["button"] == "compute":
            nutrients = compute(inst["food_list"],inst["quant_list"],self.foodDB.food_total_list)
            
            self.food_list  = inst["food_list"][0]
            self.quant_list = inst["quant_list"][0]
        
            self.P = float(nutrients[0][0])
            self.C = float(nutrients[0][1])
            self.G = float(nutrients[0][2])
            
        elif inst["button"] == "optimize":
            const_list = [self.const_list]
            quant_list = optimizer(inst["food_list"],const_list,self.foodDB.food_total_list)
            nutrients  = compute(inst["food_list"],quant_list,self.foodDB.food_total_list)
            
            self.food_list  = inst["food_list"]
            self.quant_list = quant_list[0]
            
            self.P = float(nutrients[0][0])
            self.C = float(nutrients[0][1])
            self.G = float(nutrients[0][2])
         
        elif inst["button"] == "find":
            finder_settings = {self.name: inst["combo"][0]}
            found = finder(finder_settings, self.goals,self.foodDB)
            nutrients  = compute(found[0],found[1],self.foodDB.food_total_list)
            
            self.food_list  = found[0][0]
            self.quant_list = found[1][0]
            
            self.P = float(nutrients[0][0])
            self.C = float(nutrients[0][1])
            self.G = float(nutrients[0][2])           

# Dieta object
class Dieta(object):    
    def __init__(self,Kcal,P,C,G):    
        self.list_days = []
        const  = Dieta_const()    
        dist   = Dieta_dist()
        foodDB = Dieta_foodDB()                     
        goals  = Dieta_goals(const,dist,Kcal,P,C,G)
        
        self.foodDB = foodDB
        self.goals  = goals
        
        # Notices that objects foodDB and goals are instantiated here, and are further
        # stored as attributes in the Dieta_meals object
        self.monday    = Dieta_days(goals,foodDB)
        self.tuesday   = Dieta_days(goals,foodDB)
        self.wednesday = Dieta_days(goals,foodDB)
        self.thursday  = Dieta_days(goals,foodDB)
        self.friday    = Dieta_days(goals,foodDB)
        self.saturday  = Dieta_days(goals,foodDB)
        
        self.list_days.append(self.monday)
        self.list_days.append(self.tuesday)
        self.list_days.append(self.wednesday)
        self.list_days.append(self.thursday)
        self.list_days.append(self.friday)
        self.list_days.append(self.saturday)
        
        
        