# Filename: versioncheck.py

import sys, warnings

print (sys.version_info[0])


if sys.version_info[0] < 3:
	warnings.warn("Need Python 3.0 for this program to run",RuntimeWarning)
else:
	print('Proceed as normal')
