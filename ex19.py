# define cheese_and_crackers function with two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print info based on first argument
    print "You have %d cheeses!" % cheese_count
    # print info based on second argument
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
# use the numbers as arguments directly when using the function
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
# declare variables
amount_of_cheese = 10
amount_of_crackers = 50

# use the variables as arguments in the function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
# do math and use the result as arguments in the function
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
# do math with variables and numbers and use the result in the function
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
