

print("This is a BMI Calculating App!")
again_bool = True
while again_bool:
    unitInput = input("Would you like to use metric units or standard? (1 = metric, 2 = standard)")
    
    try:
        unitInput  = eval(unitInput)                    
                    
    except:
        some_bool = True
                    
    if str != type(unitInput):   
        some_bool = False
        
        2
        
    again_bool = False
    if unitInput.lower() == "metric":
        new_bool = True
        while new_bool:
            
            some_bool = True
            while some_bool:
                weightInpt  = input("What is your weight in kilograms?")
                heightInput = input("What is your height in meters?")

                try:
                    weightInpt  = eval(weightInpt)
                    heightInput = eval(heightInput)
                    
                    
                except:
                    print("That is a string please input an integer.")
                    some_bool = True
                    
                if str != type(weightInpt) and str != type(heightInput):   
                    some_bool = False
                    
            bmi = (weightInpt) / (heightInput**2)
            print("Your BMI based on your height of", heightInput, " meters and weight of", weightInpt, "kgs is ", bmi)
            
            if bmi<= 18.5:
                print("This have an underweight weight.")
                new_bool = False
            elif bmi>= 18.5 and bmi<= 24.9:
                print("You have a normal weight.")
                new_bool = False
            elif bmi>= 25 and bmi <= 29.9:
                print("You have an overweight weight.")
                new_bool = False
            elif bmi >= 30:
                print("You have an obese weight.")
                new_bool = False
            else:
                print("Something went wrong in your calculations.")
                new_bool = True
            
        
        
    elif unitInput.lower() == "standard":
        new_bool = True
        while new_bool:
            
            some_bool = True
            while some_bool:
                weightInpt  = input("What is your weight in lbs?")
                heightInput = input("What is your height in inches?")

                try:
                    weightInpt  = eval(weightInpt)
                    heightInput = eval(heightInput)
                    
                    
                except:
                    print("That is a string please input an integer.")
                    some_bool = True
                    
                if str != type(weightInpt) and str != type(heightInput):   
                    some_bool = False
                    
            bmi = (weightInpt / (heightInput**2)) * 703
            print("Your BMI based on your height of", heightInput, "inches and weight of", weightInpt, "lbs is ", bmi)
            
            if bmi<= 18.5:
                print("This have an underweight weight.")
                new_bool = False
            elif bmi>= 18.5 and bmi<= 24.9:
                print("You have a normal weight.")
                new_bool = False
            elif bmi>= 25 and bmi <= 29.9:
                print("You have an overweight weight.")
                new_bool = False
            elif bmi >= 30:
                print("You have an obese weight.")
                new_bool = False
            else:
                print("Something went wrong in your calculations.")
                new_bool = True
        
    else:
        print("That is not a valid input please try again.")
        again_bool = True
    