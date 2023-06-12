def bisiesto(año):
    año=0
    while año<2023:        
        if año%4!=0:
            print(f'{año} no es año bisiesto')
        else:
            print(f'{año} es año bisiesto')  
        año+=1      
año=0
bisiesto(año)