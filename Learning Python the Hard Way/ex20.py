# use with argument test.txt

from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0)
	
def print_a_line(line_count, f):
	print line_count, f.readline()
	
current_file = open(input_file)

print "First let's print the whole file.\n"

# prints whole file
print_all(current_file)

print "Now let's rewind, kind of like a tape.\n"

# this rewinds python reading the file
# Without it, it prints out 1 2 3 and no line from the file
rewind(current_file)

print "Let's print three lines:\n"

current_line = 1 # this makes the number 1 at beginning of line
print_a_line(current_line, current_file)

current_line = current_line + 1 # this makes a 2
print_a_line(current_line, current_file)

current_line = current_line + 1 #this makes a 3 (if you use a 2 it makes a 4)
print_a_line(current_line, current_file)