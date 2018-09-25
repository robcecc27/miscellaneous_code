def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man That's enough for a party!"
	print "Get a blanket. \n"
	
#wont work until this line
#takes 20 and 30 and filles in %d spaces above
#prints line below and then prints 4 lines above 
#beneath it
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# same as above but uses 10 and 50 
print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#same as above but uses equations below
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#uses variables from line 16 and 17 then adds 
#the 100 and 1000 to it. 
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)