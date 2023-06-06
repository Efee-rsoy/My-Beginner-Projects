# Max moisture level is 100


def water_plant(moisture_level = int(input()),temperature = int(input())):
    if moisture_level > 50 or moisture_level < 70 and temperature > 30:
        value = True
        return value 
    elif temperature < 10 and moisture_level >= 30 and moisture_level <= 40:
        value = False
        return value 
    elif moisture_level < 50:
        value = True
        return value 
    elif moisture_level >= 50:
        value = False
        return value 
    
    
        
x = water_plant()
print(x)