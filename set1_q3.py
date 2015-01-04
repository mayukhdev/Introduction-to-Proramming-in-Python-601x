s = 'abcbcd'

count=0 
ans=0
maxc=-1

for i in range(0,len(s)-1):
    start = i
    while(i+1<len(s) and s[i]<=s[i+1]):
        i+=1
        count=i+1-start
        if (maxc==0):
            maxc=count
            ans=start
        elif(count>maxc):
            maxc = count
            ans=start
        
if(maxc==-1)    
    print s[ans]
else:
    print s[ans:ans+maxc]        


    
    

            
