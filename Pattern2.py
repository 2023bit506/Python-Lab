#only last line is -
def Q1(l):
	len = l*2+1
	for i in range(0,(len//2)+1):
		for j in range(0,len):
			if j==(len//2)-i:
				print("+",end="")
			elif j==(len//2)+i:
				print("+",end="")	
			else:
				print(" ",end="")
		print("")
		
	for i in range(0,(len//2)-1):
		for j in range(0,len):
			if j==i+1:
				print("+",end="")
			elif j==(len-1)-i-1:
				print("+",end="")
				break	
			else:
				print(" ",end="")
			
		print("")
	for i in range(1):
		for j in range(0,len):
			if(j==len//2):
				print("-",end="")
			else:
				print(" ",end="")
		print("")

	return ""
#lower tringle is -
def Q2(l):
	len = l*2+1
	for i in range(0,(len//2)+1):
		for j in range(0,len):
			if j==(len//2)-i:
				print("+",end="")
			elif j==(len//2)+i:
				print("+",end="")	
			else:
				print(" ",end="")
		print("")
		
	for i in range(0,(len//2)-1):
		for j in range(0,len):
			if j==i+1:
				print("-",end="")
			elif j==(len-1)-i-1:
				print("-",end="")
				break	
			else:
				print(" ",end="")
			
		print("")
	for i in range(1):
		for j in range(0,len):
			if(j==len//2):
				print("-",end="")
			else:
				print(" ",end="")
		print("")

	return ""
#main program-->
def print_pattern(len):
    if len<1:
        return "Enter a number greater than equals to 1"
    if len%1!=0:
        return "Provide positive integer value greater than equal to 1"
    else:
        return Q1(len) 
	


print(Q1(2.00))
# print(Q2(2))
