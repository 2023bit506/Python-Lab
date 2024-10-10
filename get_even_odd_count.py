def even_odd(ls):
    
    #------------------------------Approach 1------------------------------------
    # even_count = 0
    # odd_count = 0
    
    # for i in ls:
    #     if i % 2 == 0:
    #         even_count += 1
    #     else:
    #         odd_count += 1
            
    # return even_count, odd_count
    
    #-------------------------------Approach 2--------------------------------------
    # even_count = 0
    # odd_count = 0
    # for i in ls:
    #     if i & 1 == 0:
    #         even_count += 1
    #     else:
    #         odd_count += 1
            
    # return even_count, odd_count
    
    #-------------------------------Approach 3--------------------------------------------
    # even_count = 0
    # odd_count = 0
    
    # even_count += sum(1  for i in ls if i&1==0 )
    # odd_count  += len(ls) - even_count
    
    # return even_count, odd_count

	#-------------------------------Approach 4--------------------------------------------
    even_count = 0
    odd_count = 0
    
    even_count += sum(1  for i in ls if i%2==0 )
    odd_count  += len(ls) - even_count
    
    return even_count, odd_count

print(even_odd([1,2,3,4,5,6,7,8,9]))























