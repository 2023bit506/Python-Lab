def modula(numerator, denominator):
    if numerator < 0:
        numerator = -numerator
        sign = -1
    else:
        sign = 1
    
    while numerator >= denominator:
        numerator -= denominator
    
    return numerator * sign

# Example usage
print(modula(-24, 7))  
# print(modula(10, -3))  
# print(modula(-10, -3)) 
# print(modula(10, 3))  
