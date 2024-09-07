def decimal_sub(num1, num2):
    negative = False
    # Check if num1 is less than num2
    if int(num1) < int(num2):
        num1, num2 = num2, num1
        negative = True
    
    # Convert numbers to list of digits
    num1 = list(map(int, num1))
    num2 = list(map(int, num2))
    
    # Pad num2 with leading zeros to match the length of num1
    while len(num2) < len(num1):
        num2.insert(0, 0)
    
    result = []
    borrow = 0
    
    # Perform the subtraction from right to left
    for i in range(len(num1) - 1, -1, -1):
        digit1 = num1[i] - borrow
        digit2 = num2[i]
        
        if digit1 < digit2:
            # Borrow from the next digit
            digit1 += 10
            borrow = 1
        else:
            borrow = 0
        
        result.insert(0, digit1 - digit2)
    
    # Remove leading zeros from the result
    while result[0] == 0 and len(result) > 1:
        result.pop(0)
    
    # Convert result list back to string
    result_string = ''.join(map(str, result))
    
    # Return negative result if necessary
    if negative:
        return '-' + result_string
    else:
        return result_string

# Test cases
print(decimal_sub("1", "5"))            
print(decimal_sub("0", "5"))              
print(decimal_sub("7", "5"))              
print(decimal_sub("4", "5"))              
print(decimal_sub("5", "5"))            
print(decimal_sub("45", "5"))          
print(decimal_sub("8454545454", "787878545454545445"))  
print(decimal_sub("1111", "111"))       
