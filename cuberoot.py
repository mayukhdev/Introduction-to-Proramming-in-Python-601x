#cube root
x =(int)(raw_input('enter integer: '))
ans =0
while(ans**3 < x):
    ans+=1
if(ans**3 != x):
    print (str(x)+" not cube of 3")
    #less = ans**3-x
    #print (str(x)+" should be "+str(less)+" much more to be a perfect cube.")
else:
    print (str(x)+" is a perfect cube")                