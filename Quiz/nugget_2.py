def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    6a+9b+20c=n
    """  
    def check(n):
        if n%6==0 or n%9==0 or n%20==0:
            return True
    
    def all(n):
        for i in (6,9,20):
            if (n-i)>0 and check(n-i):
                return True
                    
    while n>0:
        #print n
        if check(n):
            return True                
        if all(n):
            return True
        if n>=20:
            n-=20
        elif n>=9:
            n-=9
        else:
            n-=6
                    
    #print n
    
    if n==0:
        return True
    else:
        return False    
                    