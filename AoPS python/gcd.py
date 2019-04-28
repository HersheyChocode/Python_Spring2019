def gcd(a,b):
    
    if b==0:
        return a
        
    return(gcd(a-b,b))
print(gcd(20,45))
