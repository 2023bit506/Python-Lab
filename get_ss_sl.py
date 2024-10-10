def get_SL_SS(L):
    temp = []
    
    # Recursive extraction of integers
    for i in L:
        if isinstance(i, int):
            temp.append(i)
        elif isinstance(i, (list, tuple, set)):
            temp += get_SL_SS(i)
        elif isinstance(i, dict):
            temp.extend(i.keys())
            temp.extend(i.values())
    
    # Remove non-integer from the temp list
    temp = [i for i in temp if isinstance(i, int)]
    
    # Sort the list
    temp = bubble_sort(temp)

    # checking for the all the edge cases 
    if len(temp) == 0:
        return None
    elif len(temp) == 1:
        return temp[0]
    
    return temp[-2], temp[1]

print(get_SL_SS([-10,-20,[40,50]]))  
print(get_SL_SS(["SG",(4,3),{0:'SG',2:1}]))  
print(get_SL_SS([10]))  # Expected: 10
print(get_SL_SS([10, "test", 20]))  
print(get_SL_SS([])) 
