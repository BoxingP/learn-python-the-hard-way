def add_number_to_list(limit):
    i = 0
    numbers = []
    while i < limit:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    return numbers

print "Input how many numbers do you want to add"
limit = raw_input("> ")
numbers = add_number_to_list(int(limit))

print "The numbers: "

for num in numbers:
    print num
