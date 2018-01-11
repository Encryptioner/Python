
bri=set(['brazil','russia','india'])

if 'india' in bri:
	print 'true'
else:
	print 'false'

if 'usa' in bri:
	print 'true'
else:
	print 'false'

bric=bri.copy()
bric.add('china')

if bric.issuperset(bri):
	print 'true'
else:
	print 'false'

bri.remove('russia')

print bri&bric #bri.intersection(bric)
print bri|bric
print bri-bric
print bric-bri


