def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    n1 = len(s1)
    n2 = len(s2)
    s = ''
    i=0
    j=0
    while i<n1 and j<n2:
        s += s1[i]
        s += s2[j]
        i+=1
        j+=1

    if(i==n1):
        while(j<n2):
            s += s2[j]
            j+=1
    elif (j==n2):
        while i<n1:
            s += s1[i]        
            i+=1
    return s        
        
        
        