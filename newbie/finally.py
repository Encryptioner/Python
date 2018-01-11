# Filename: finally.py

import time

try:
	f = open('poem.txt')
	
	while True: # our usual file-reading idiom
		line = f.readline()
		
		if len(line) == 0:
			break
		print(line)
		
		time.sleep(2) # To make sure it runs for a while

except KeyboardInterrupt:#ctrl+c dircectly closs file
	print('!! You cancelled the reading from the file.')

except EOFError:#does not work until file reading is done, closes the program without showing the finally block
	print('Why did you do an EOF on me?')

finally:
	f.close()
	print('(Cleaning up: Closed the file)')

#end try..finally
