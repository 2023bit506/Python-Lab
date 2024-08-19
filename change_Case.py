def change_case(text, style):
    if style in ('C', 'c'):
        return convert_to_small_case(text)
    elif style in ('S', 's'):
        return convert_to_capital_case(text)
    elif style in ('R', 'r'):
        return swap_case(text)
    elif style in ('Z', 'z'):
        return zigzag_string(text)
    else:
        return "Invalid style"

def convert_to_small_case(text):
    result = ""
    for i in text:
        if 'A' <= i <= 'Z':
            result += chr(ord(i) + 32)
        else:
            result += i
    return result

def convert_to_capital_case(text):
    result = ""
    for i in text:
        if 'a' <= i <= 'z':
            result += chr(ord(i) - 32)
        else:
            result += i
    return result

def swap_case(text):
    result = ""
    for i in text:
        if 'A' <= i <= 'Z':
            result += chr(ord(i) + 32)
        elif 'a' <= i <= 'z':
            result += chr(ord(i) - 32)
        else:
            result += i
    return result

def zigzag_string(text):
    
    #Approach 1
    result = ""
    for index, char in enumerate(text):
        if index % 2 == 0:
            if 'a' <= char <= 'z':
                result += chr(ord(char) - 32)
            else:
                result += char
        else:
            if 'A' <= char <= 'Z':
                result += chr(ord(char) + 32)
            else:
                result += char
    return result

    #Approach 2

    # result = ""
    # for index, char in enumerate(text):
    #     if index % 2 == 0:
    #         if 'a' <= char <= 'z':
    #             result += char.upper()
    #         else:
    #             result += char
    #     else:
    #         if 'A' <= char <= 'Z':
    #             result += char.lower()
    #         else:
    #             result += char
    # return result

# Example usage:
print(change_case("sHubHam", 'c'))  
print(change_case("sHubHam", 'S'))  
print(change_case("sHubHam", 'r')) 
print(change_case("sHubHam", 'Z'))  
