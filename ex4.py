# declare cars number to be 100
cars = 100
# declare car seats to be 4
space_in_a_car = 4.0
# declare drivers number to be 30
drivers = 30
# declare passengers number to be 90
passengers = 90
# get the cars number which don't have driver
cars_not_driven = cars - drivers
# get the cars number which have driver
cars_driven = drivers
# get the people number cars which have driver can take
carpool_capacity = cars_driven * space_in_a_car
# calculate the average passengers per car
average_passengers_per_car = passengers / cars_driven

# print the results
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
