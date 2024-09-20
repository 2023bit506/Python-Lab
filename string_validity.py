def check_validity(text):
    if len(text) == 0:
        return True  # Valid

    if len(text) == 1 or text.isalpha():
        return False  # Invalid

    valid_start = ['(', '[', '{', '<']
    invalid_start = [')', ']', '}', '>']

    if text[0] in invalid_start:
        return False  # Invalid

    stack = []
    
    for char in text:
        if char in valid_start:
            stack.append(char)
        elif char in invalid_start:
            if len(stack) == 0:
                return False  
            if stack[-1] == valid_start[invalid_start.index(char)]:
                stack.pop()            
            else:
                return False  

    return len(stack) == 0  

def count_valid_invalid(texts):
    valid_count = 0
    invalid_count = 0
    
    for text in texts:
        if isinstance(text, str):  
            if check_validity(text):
                valid_count += 1
            else:
                invalid_count += 1
        elif isinstance(text, (list, tuple)):  
            inner_valid, inner_invalid = count_valid_invalid(text)  
            valid_count += inner_valid
            invalid_count += inner_invalid

    return (valid_count, invalid_count)

# Example usage
print(count_valid_invalid(['({)', [45, ("()")], ""]))  
