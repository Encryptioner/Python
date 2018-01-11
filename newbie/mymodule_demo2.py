# Filename: mymodule_demo2.py


from mymodule import sayhi, __version__
	
sayhi()#latest sayhi() will perform

def sayhi():
	print('Hi, this is mymodule of this program speaking.')

sayhi()#latest sayhi() will perform

print('Version', __version__)
#if there is a sayhi or __version__ present allready in the program, then there will be a clash
