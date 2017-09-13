# Copyright 2017 Zisen Zhou jason826@bu.edu

import sys
if len(sys.argv) < 5:
	for x in range(1,len(sys.argv)):
		print (sys.argv[x])
else:
	for x in range(1,5):
		print (sys.argv[x])
	for x in range(5,len(sys.argv)):
		sys.stderr.write(sys.argv[x])
		sys.stderr.write('\n')