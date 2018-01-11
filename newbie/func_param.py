# Filename: func_param.py


def printMax(a, b):
	
	a=10 #change value of a in local 
	
	if a > b:
		print a, 'is maximum'
		
	elif a == b:
		print a, 'is equal to', b
		
	else:
		print b, 'is maximum'
	print 'value of a inside printMax function (local variable)', a

#end of function

printMax(3, 12) # directly give literal values

a = 5
b = 7
printMax(a, b) # give variables as arguments

print 'value of a outside printMax function (variable)', a


#receiving list in function as parameter
def powersum(power,*args):
	total=0
	for i in args:
		total+=pow(i,power)
		print power," ",i," ",total
	return total

print(powersum(2,3,4))
print(powersum(2,10))



