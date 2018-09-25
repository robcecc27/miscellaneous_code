cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available." # print the string and 100 from the cars variable 
print "There are only", drivers, "drivers available."  #print the string and 30 from the drivers variable
print "There will be", cars_not_driven, "empty cars today."  #prints string and 70
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

