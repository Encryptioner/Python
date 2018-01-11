# Filename: func_default.py

def say(message, times = 3):
	#Only those parameters which are at the end of the parameter list can be given default argument values
	print(message * times)
#end say
say('Hello')
say('World', 5)


def func(a, b=5, c=10):
	'''Prints the value of a,b,c.
	
	DEFINITION func(a, b=5, c=10) : No need of all values must be integers.
	
	This is called keyword arguments - we use the name (keyword) instead of the position.'''
	print 'a is', a, 'and b is', b, 'and c is', c
#end def
func(3, 7.7)
func(25, c=24)
func(c=50, a=100)
print(func.__doc__)

def someFunction():#do nothing, indicate an empty block of statements.
	pass 
#end someFunction():
someFunction()

def total(initial=5, *numbers, **keywords):
#* takes value as list and ** prefix is used to specify the extra parameters would be considered to be key/value pairs of a dictionary.
	count = initial
	for number in numbers:
		count += number
	for key in keywords:
		count += keywords[key]
	return count
#end total
print(total(10, 1, 2, 3, vegetables=50, fruits=100))#uses initial=10
print(total(n=6, vegetables=50, fruits=100))#uses initial=5
print(total(10, 1, 2, 3))#uses initial=10

print(func.__doc__)
