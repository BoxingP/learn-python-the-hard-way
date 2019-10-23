def add_number_to_list(limit, increment):
    scope = range(0, limit, increment)
    numbers = []
    for i in scope:
        print "Add %d to list" % i
        numbers.append(i)
    return numbers

print "Input the numbers limit which numbers are less than it"
limit = raw_input("> ")
print "Input the increment between numbers"
increment = raw_input("> ")

numbers = add_number_to_list(int(limit), int(increment))

print "The numbers: "

for num in numbers:
    print num
