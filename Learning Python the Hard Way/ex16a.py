from sys import argv

script, filename = argv

#print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

#raw_input("?")

print "Open the File..."
target = open(filename, 'w')

#print "Truncateing the file. Goodbye!"
#target.truncate()

print "Type in 3 lines."

line4 = raw_input("line 4: ")
line5 = raw_input("line 5: ")
line6 = raw_input("line 6: ")

print "I'm going to write these to the file."

target.write
target.write(line4)
target.write("\n")
target.write(line5)
target.write("\n")
target.write(line6)
target.write("\n")

print "And finally, we close it."
target.close() 