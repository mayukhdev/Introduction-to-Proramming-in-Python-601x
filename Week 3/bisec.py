def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here 
    num= len(aStr)
    
    if(num>0):
        mid = num/2 
        if num==1:
            if aStr[num-1]==char:
                return True
            else:
                return False              
        
        if aStr[mid]==char:
            return True
        elif char < aStr[mid]:
            return isIn(char,aStr[:mid])            
        else:
            return isIn(char,aStr[mid:])
    
    return False