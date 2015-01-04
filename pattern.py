s = 'azcbobobegghakl'
count = 0
index=-1
start=0

while True:
    index=s.find('bob',start)
    if(index==-1):
        break        
    else:
        count+=1
        start = index+1
        index=-1
        continue    

print count        
        
        