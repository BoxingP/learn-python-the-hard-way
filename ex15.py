# import argv
from sys import argv

# unpack arguments
script, filename = argv

# open file
txt = open(filename)

# print file name
print "Here's your file %r:" % filename
# read file content and print it out
print txt.read()
txt.close()

# input file name
print "Type the filename again:"
file_again = raw_input("> ")

# open file with the name inputed
txt_again = open(file_again)

print txt_again.read()
txt_again.close()
