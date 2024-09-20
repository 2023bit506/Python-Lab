def check_validity(text):
	if len(text)==0:
		return "Valid"

	if len(text)==1:
		return "Invalid"

	if text.isalpha():
		return "Invalid"

	valid_start = ['(','[','{','<']
	invalid_start = [')',']','}','>']

	if text[0] in invalid_start:
		return "Invalid" 

	stack = []
	
	for char in text:
		if char in valid_start:
			stack.append(char)
		elif char in invalid_start:
			if len(stack)==0:
				return "Invalid"
			if stack[-1] == valid_start[invalid_start.index(char)]:
				stack.pop()			
			else:
				return "Invalid"


	return "valid"
		



#print(check_validity("abc"))
#print(check_validity("[]"))
#print(check_validity("[]}"))
print(check_validity("{[(<>)]}"))
print(check_validity("{"))
print(check_validity("{[<]>}"))





















'''else:
				#stack[-1] == valid_start(invalid_start.index(char))
				if stack[-1] == valid_start[0] and char in invalid_start[0]: stack.pop()
				if stack[-1] == valid_start[1] and char in invalid_start[1]: stack.pop()
				if stack[-1] == valid_start[2] and char in invalid_start[2]: stack.pop()
				if stack[-1] == valid_start[3] and char in invalid_start[3]: stack.pop()
				#stack.pop()'''