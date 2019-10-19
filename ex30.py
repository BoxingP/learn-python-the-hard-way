# define people value
people = 30
# define cars value
cars = 40
# define buses value
buses = 15

# if cars is bigger than people, will print "take the cars"
if cars > people:
    print "We should take the cars."
# if cars is less than people, will print "not take the cars"
elif cars < people:
    print "We should not take the cars."
# otherwise will print "can't decide"
else:
    print "We can't decide."

# if buses is bigger than cars, will print "too many buses"
if buses > cars:
    print "That's too many buses."
# if buses is less than cars, will print "take the buses"
elif buses < cars:
    print "Maybe we could take the buses."
# otherwise will print "can't decide"
else:
    print "We still can't decide."

# if people is bigger than buses, will print "take the buses"
if people > buses:
    print "Alright, let's just take the buses."
# otherwise will print "stay home"
else:
    print "Fine, let's stay home then."
