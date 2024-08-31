def slice(object, slicing_parameter):
    resultList = []
    object_list = [str, list, tuple]
    len_slicing_parameter = len(slicing_parameter)
    n = len(object)  # Length of the object
    
    # Check if the slicing parameter has more than 3 elements
    if len_slicing_parameter > 3:
        return "Invalid Parameters, it should contain only three parameters"
    
    # Check if all slicing parameters are integers
    if not all(isinstance(element, int) for element in slicing_parameter):
        return "Slicing parameters should be integers"
    
    # Check if slicing is applicable for the given object type
    if type(object) not in object_list:
        return "TypeError: Slice is not applicable for " + str(type(object))
    
    # If the step is 0, return error
    if len_slicing_parameter == 3 and slicing_parameter[2] == 0:
        return "Slice step cannot be zero"
    
    # Determine start, end, and step based on provided parameters
    if len_slicing_parameter == 1:
        start = slicing_parameter[0]
        end = n
        step = 1
    elif len_slicing_parameter == 2:
        start = slicing_parameter[0]
        end = slicing_parameter[1]
        step = 1
    else:  # len_slicing_parameter == 3
        start = slicing_parameter[0]
        end = slicing_parameter[1]
        step = slicing_parameter[2]
    
    # for negative indices
    if start < 0:
        start += n
    if end < 0:
        end += n

    # start and end are within bounds
    start = max(0, start)
    end = min(n, end)

    #slicing
    for i in range(start, end, step):
        resultList.append(object[i])
    
    # correct type of the result
    if isinstance(object, str):
        return ''.join(resultList)
    else:
        return type(object)(resultList)

# Example
object = 'shubham'
start = -7
end = -1
step = 2
slicing_parameter = (start, end, step)
print(slice(object, slicing_parameter)) 
