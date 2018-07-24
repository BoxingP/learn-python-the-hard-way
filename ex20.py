from sys import argv

script, input_file = argv

# define a function to print out all file content
def print_all(f):
    print f.read()

# change the file object's position to the beginning of the file
def rewind(f):
    f.seek(0)

# print out one line from the file and the line count
def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

# define current line amount as 1
current_line = 1
print_a_line(current_line, current_file)

# increase the line amount
current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
