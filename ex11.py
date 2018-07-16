print "How old are you?",
age = int(raw_input('--> '))
print "How tall are you?",
height = raw_input('--> ')
print "How much do you weight?",
weight = raw_input('--> ')
print "Where do you come from?",
address = raw_input('--> ')

print "So, you're %r old, %r tall and %r heavy. And you come from %r." % (
    age, height, weight, address)
