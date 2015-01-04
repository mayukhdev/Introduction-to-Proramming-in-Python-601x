import random

def mySort(L):
    clear = False
    while not clear:
        print L
        clear = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                clear = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
                
L=[]
for i in range(10):
    L.append(random.randrange(0,100))
                