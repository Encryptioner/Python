
def get_rawtext(text):
	rawtext=''
	n=len(text)
	
	for i in range(0,n):
		
		if text[i]>='A' and text[i]<='Z':
			#text[i]+=32
			#need to convert capital to smaller
			rawtext+=text[i]
		elif text[i]>='a' and text[i]<='z':
			rawtext+=text[i]
	
	print rawtext
	return rawtext

def reverse(text):
	return text[::-1]

def is_palindrome(text):
	text=get_rawtext(text)
	return text == reverse(text)


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

