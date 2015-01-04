def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    print 'n: '+str(n)+' start: '+str(fr) +' destnation: '+ str(to) +' aux: '+ str(spare)
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)  
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
        
Towers(2,'S','F','A')        