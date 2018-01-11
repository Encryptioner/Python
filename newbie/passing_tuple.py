#passing tuple

def get_error_details():
	return (2,'second error details')
#end

errnum, errstr = get_error_details()

print(errnum)
print(errstr)

#If you want to interpret the results as (a, <everything else>), then you just need to star it just like you would in function parameters:
#gives error
'''
a, *b = [1, 2, 3, 4]
print(a)
print(b)
'''

a=5; b=8;
a,b = b,a

print(a)
print(b)
