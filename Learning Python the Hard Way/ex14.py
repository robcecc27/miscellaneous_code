# To run must provide a user name 
# command looks like  python ex14.py Rob
#Rob is the argument needed to run
from sys import argv

script, user_name = argv  
prompt = '-> ' 

#prints name and file name
print "Hi %s. I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."

print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" %(likes, lives, computer) 