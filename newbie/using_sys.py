#!/usr/bin/python
# Filename: using_sys.py

import sys

print('The command line arguments are:\n')
for i in sys.argv:
	print(i)
	
print'hello\n'
print'\n\nThe PYTHONPATH is', sys.path, '\n'


