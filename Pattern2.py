#only last line is -
def Q1(l):
	length = l*2+1
	for i in range(0,(length//2)+1):
		for j in range(0,length):
			if j==(length//2)-i:
				print("+",end="")
			elif j==(length//2)+i:
				print("+",end="")	
			else:
				print(" ",end="")
		print("")
		
	for i in range(0,(length//2)-1):
		for j in range(0,length):
			if j==i+1:
				print("+",end="")
			elif j==(length-1)-i-1:
				print("+",end="")
				break	
			else:
				print(" ",end="")
			
		print("")
	for i in range(1):
		for j in range(0,length):
			if(j==length//2):
				print("-",end="")
			else:
				print(" ",end="")
		print("")

	return ""
#lower tringle is -
def Q2(l):
	length = l*2+1
	for i in range(0,(length//2)+1):
		for j in range(0,length):
			if j==(length//2)-i:
				print("+",end="")
			elif j==(length//2)+i:
				print("+",end="")	
			else:
				print(" ",end="")
		print("")
		
	for i in range(0,(length//2)-1):
		for j in range(0,length):
			if j==i+1:
				print("-",end="")
			elif j==(length-1)-i-1:
				print("-",end="")
				break	
			else:
				print(" ",end="")
			
		print("")
	for i in range(1):
		for j in range(0,length):
			if(j==length//2):
				print("-",end="")
			else:
				print(" ",end="")
		print("")

	return ""
#main program-->
def print_pattern(length):
    if length<1:
        return "Enter a number greater than equals to 1"
    if length%1!=0:
        return "Provide positive integer value greater than equal to 1"
    else:
        return Q1(length) 
	


print(Q1(2))
# print(Q2(2))
