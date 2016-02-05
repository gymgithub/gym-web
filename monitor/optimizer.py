import numpy as np
from scipy.optimize import minimize
from operator import itemgetter

def optimizer (food_list,const_list,food_total_list):
    

    # Get required food nutrients data
    nmeals = len(food_list)
    Prot   = []
    Carbo  = []
    Grasa  = []
    for i in range(0,nmeals):
        # Loop each meal
        nfoods = len(food_list[i]) 
        for j in range (0,nfoods):
            # Loop each food
            food           = food_list[i][j]
            food_nutrients = next(food_nutrients for food_nutrients in food_total_list if food in food_nutrients)
            Prot.append(float(food_nutrients[1])/100)
            Carbo.append(float(food_nutrients[2])/100)
            Grasa.append(float(food_nutrients[3])/100)
            
    # Setting Cost Function
    def func(x):
        #f  = np.zeros(nmeals)
        ind = 0
        f = 0
        for i in range(0,nmeals):
            nfoods = len(food_list[i])
            
            P_cons = const_list[i][0]
            C_cons = const_list[i][1]
            G_cons = const_list[i][2]
            
            termP = 0
            termC = 0
            termG = 0
            for j in range (0,nfoods):
                
                
                termP = termP + x[ind + j]*Prot[ind + j]
                termC = termC + x[ind + j]*Carbo[ind + j]
                termG = termG + x[ind + j]*Grasa[ind + j]
        
            f = f + (P_cons - termP)**2 + (C_cons - termC)**2 + (G_cons - termG)**2
            
            ind =  ind + nfoods
        return f
    
    # Setting Constraints (No way to input jacobian within a loop)
    total_food = 0
    for i in range(0,nmeals):
        nfoods = len(food_list[i])
        total_food =total_food + nfoods
    lst = [{'type': 'ineq', 'fun': itemgetter(j)} for j in range(total_food)]
    cons = tuple(lst)
    
    #Calling the optimizer
    initial_guess = np.ones(total_food)
    res = minimize(func, initial_guess,method='SLSQP',constraints = cons, options={'disp': True})  
    
    quant_list = []
    ind = 0
    for i in range(0,nmeals):
        quant_meal = []
        nfoods = len(food_list[i]) 
        
        for j in range (0,nfoods):
            quant_meal.append(res.x[ind + j])
        
        ind = ind + nfoods
        quant_list.append(quant_meal)

    return quant_list


