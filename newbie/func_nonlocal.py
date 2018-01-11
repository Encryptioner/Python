# Filename: func_nonlocal.py
#nonlocal x gives error 
x=50

def func_outer():
	
	global x 
	x = 2
	print('x is', x)
	def func_inner():
		global x  #without this line in  func_inner x=5 but in func_outer x=2
		x=5
		print('Changed  inner x to', x)
	#end func_inner
	
	func_inner()
	print('Changed outer x to', x)
#end func_outer
func_outer()

print('Changed main x to', x)
