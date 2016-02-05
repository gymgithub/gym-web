from dieta import Dieta
from optimizer import optimizer
from finder import finder
from compute import compute

if __name__ == "__main__":
    
    test = "overall"
    
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
        case = 1
        if case == 1:
            inst = {"day":"monday", "meal":"breakfast", "button":"compute", "food_list": food_list, "quant_list": quant_list}
        elif case == 2:
            inst = {"day":"monday", "meal":"breakfast", "button":"optimize", "food_list": food_list}
        elif case == 3:
            inst = {"day":"monday", "meal":"breakfast", "button":"find", "combo": combo}
        
        # Perform the demanded instructions
        if inst["day"] == "monday":
            if inst["meal"] == "breakfast":
                dieta_JM.monday.breakfast.execute(inst)
                print (dieta_JM.monday.breakfast.P)
                print (dieta_JM.monday.breakfast.C)
                print (dieta_JM.monday.breakfast.G)
                print (dieta_JM.monday.breakfast.food_list)
                print (dieta_JM.monday.breakfast.quant_list)
    
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
        print (nutrients)
        print (food_list)
        print (quant_list)
        
    # RANDOM food example
    if test == "finder":
        finder_settings = {"breakfast": "PCG","lunch": "PPC","appetizers": "PC", "dinner": "PC"}
    
        found = finder(finder_settings,dieta_JM.goals,dieta_JM.foodDB)
        food_list  = found[0]
        quant_list = found[1]
        nutrients  = compute(food_list,quant_list,dieta_JM.foodDB.food_total_list)
        
        print (nutrients)
        print (food_list)
        print (quant_list)
    



