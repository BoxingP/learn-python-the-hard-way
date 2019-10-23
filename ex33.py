def add_number_to_list(limit, increment):
    i = 0
    numbers = []
    while i < limit:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    return numbers

print "Input the numbers limit which numbers are less than it"
limit = raw_input("> ")
print "Input the increment between numbers"
increment = raw_input("> ")

numbers = add_number_to_list(int(limit), int(increment))

print "The numbers: "

for num in numbers:
    print num
