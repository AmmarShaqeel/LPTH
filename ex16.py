# importing argv module
from sys import argv

#defining names for argv module
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want to do that, hit CTRL-C (^C)."
print "If you do want to do that hit RETURN."

# getting you to press enter
raw_input("?")

# opening the file with the option to write
print "Opening the file..."
target = open(filename, 'w')

# deleting? the file
print "Truncating the file. Goodbye!"
target.truncate()

print "Now  I'm going to ask you for three lines."

#setting variable to each of 3 raw_inputs
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to a file."

# writing the the three variable to the target file
target.write(line1 + "\n" +  line2 + "\n" + line3)

# closing file
print "And finally, we close it."
target.close()

