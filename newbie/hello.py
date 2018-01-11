#!/usr/bin/python
#A Byte of Python v 1.92 (for Python 3.0)
#Filename: hello.py

import py_compile; py_compile.compile('hello.py')
#make .pyc file in same directories

import os; print(os.getcwd())
#print the directories

print("Hello World\n"); #printing a line
print('Hello World\n');
print('"Hello World\n"');
print 'hello world'
r"Newlines are indicated by \n";

comment = raw_input("Enter a comment --> ")#for python 2.x to take string input
#comment = input("Enter a comment --> ")#for python 2.x to take string input

print comment




