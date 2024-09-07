def binary_subtract(bin1, bin2):
    # check bin1 is the larger or equal-length binary string
    if len(bin2) > len(bin1):
        bin1, bin2 = bin2, bin1
    
    # Pad bin2 with leading zeroes to match the length of bin1
    bin2 = bin2.zfill(len(bin1))

    result = []
    borrow = 0
    
    # Perform subtraction from right to left
    for i in range(len(bin1) - 1, -1, -1):
        digit1 = int(bin1[i])
        digit2 = int(bin2[i])
        
        # Perform the subtraction with borrowing if necessary
        if digit1 - borrow < digit2:
            result.append(str(digit1 + 2 - borrow - digit2))
            borrow = 1
        else:
            result.append(str(digit1 - borrow - digit2))
            borrow = 0

    # Reverse the result to get the correct order
    result = result[::-1]
    
    # Remove leading zeroes, but leave at least one digit (i.e., '0' if result is zero)
    result_str = ''.join(result).lstrip('0')
    
    return result_str if result_str else '0'


print(binary_subtract('1011', '1001'))  
print(binary_subtract('1110', '1011'))  
print(binary_subtract('1101', '1101'))  
print(binary_subtract('10000', '1'))    
