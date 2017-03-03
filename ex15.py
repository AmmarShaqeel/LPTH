# normal usage of sys and import to get script and file name
from sys import argv

sript, filename = argv

# new stuff, opening file (creating a file object) then assigning it to a variable
txt = open(filename)

# printing name of file
print "Here's your file %r:" % filename
# printing contents of file with "read" command
print txt.read()

# asking for name of file
print "Type the filename again:"
# inputting name of file
file_again = raw_input(">")

# opening file again then assigning variable to it again
txt_again = open(file_again)

# printing contents of file from the txt_again variable with the "read" command
print txt_again.read()