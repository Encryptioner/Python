# Filename: lambda.py

def make_repeater(n):
	return lambda s: s * n

twice = make_repeater(2)

print(twice('word'))
print(twice(5))

#list sorting

points = [  { 'x' : 4, 'y' : 1 }, { 'x' : 2, 'y' : 3 } ]
points.sort(lambda a, b : cmp(a['x'], b['x']))

for data in points:
	print(data)
