def string_count(string, substr, overlap):
    start = 0
    count = 0
    
    while True:
        start = string.find(substr, start)
        
        if start == -1 :
            break
    
        if overlap:
            start += 1
        else:
            start += len(substr)
        
        count+=1
            
    return count

a = 'aaaaaaa'
b = 'aa'

print(string_count(a,b,False))