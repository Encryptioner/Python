#incomplete

def is_palindrome(text):
	
	n=len(text)
	for i,j in range(0,n/2) and range(n-1,(n/2)-1,-1):
		
		if text[i]!=text[j]:
			return 0
			break
	return 1

while True:
	something = raw_input('Enter text: ')
	
	if something=='n' or something=='N':
		break
	if len(something)<=0:
		print("Please input something");
		continue
	if (is_palindrome(something)):
		print("Yes, it is a palindrome");
	else:
		print("No, it is not a palindrome")
