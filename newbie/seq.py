# Filename: seq.py

shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# Indexing or 'Subscription' operation
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# Slicing on a list
print '\nItem 1 to 3 is', shoplist[1:3]
print 'Item 2 to end is', shoplist[2:]
print 'Item 1 to -1 is', shoplist[1:-1]
print 'Item 1 to -2 is', shoplist[1:-2]
print 'Item 1 to -3 is', shoplist[1:-3]
print 'Item 1 to -4 is', shoplist[1:-4]
print 'Item start to end is', shoplist[:]


# Slicing on a string
print '\ncharacters 1 to 3 is', name[1:3]#print item 1&2, stops before 3
print 'characters 2 to end is', name[2:]
print 'characters 1 to -1 is', name[1:-1]
print 'start to end is', name[:]

#using step size in list
print '\nwih step 1',shoplist[::1]
print 'wih step 2',shoplist[::2]
print 'wih step 3',shoplist[::3]
print 'wih step -1',shoplist[::-1]
print 'wih step -2 staring  at -2',shoplist[-2::-2]
