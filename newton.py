ep =0.01
y = 24.0
g = y/2.0

while abs(g*g-y)>=ep:
    g = g - (((g**2)-y)/(2*g))
    print g
print ("Sq root of "+str(y)+" is "+str(g))    