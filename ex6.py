# set a string with an integer variable
x = "There are %d types of people." % 10
# set two strings
binary = "binary"
do_not = "don't"
# set a string with two string variables
y = "Those who know %s and those who %s." % (binary, do_not)

# print the two strings out
print x
print y

# print two strings with string set before
print "I said: %r." % x
print "I also said: '%s'." % y

# set a boolean value
hilarious = False
# set a string with variable
joke_evaluation = "Isn't that joke so funny?! %r"

# print the string out with a variable convert from boolean to string
print joke_evaluation % hilarious

# set two strings
w = "This is the left side of..."
e = "a string with a right side."

# append one string to another and print the result out
print w + e
