# Filename: method.py

class Person:
	def sayHi(self):
		print('Hello, how are you?')

p = Person()
p.sayHi()
# This short example can also be written as Person().sayHi()

class Person:
	def __init__(self, name):
		self.name = name
	def sayHi(self):
		print 'Hello, my name is', self.name

p = Person('Swaroop')
p.sayHi()
