#!python2

D = {'a' : 1, 'b' : 2, 'c' : 3} # Dictionary

D['e'] = 5 # Assigning new keys grows dictionary


if not 'f' in D: # python's sole selection statement
	print 'Missing\n'
	
if not 'e' in D:  # If else... because I could!
	print 'Missing'
else:
	print "Here it is:"
	print D

raw_input("")