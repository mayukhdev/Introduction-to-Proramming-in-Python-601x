import math

def genPrimes():
    temp = 1
    while True:
        temp+=1
        if temp==2:
            yield temp
            continue        
        flag = False            
        squrt = int(math.sqrt(temp))                                
        
        for i in range(2,squrt+1):
            if temp%i==0:
                flag = True
                break
        if flag:
            continue
        else:
            yield temp     
                   
        