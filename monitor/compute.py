
def compute(food_list,quant_list,food_total_list): 
    
    # Get required food nutrients data
    nmeals  = len(food_list)
    nutrients = []
    for i in range(0,nmeals):
        # Loop each meal
        nfoods  = len(food_list[i])
        P_total = 0
        C_total = 0
        G_total = 0
        nutrients_meal = []
        for j in range(0,nfoods):
            # Loop each food
            food           = food_list[i][j]
            quantity       = float(quant_list[i][j])
            food_nutrients = next(food_nutrients for food_nutrients in food_total_list if food in food_nutrients)
            P = float(food_nutrients[1])/100
            C = float(food_nutrients[2])/100
            G = float(food_nutrients[3])/100
            
            P_total = P_total + P*quantity
            C_total = C_total + C*quantity
            G_total = G_total + G*quantity
            
        nutrients_meal.append(P_total)
        nutrients_meal.append(C_total)
        nutrients_meal.append(G_total)
        nutrients.append(nutrients_meal)
    
    return nutrients 