ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not ten items in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
print "printing stuff: ", stuff

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)
	
print "There we go: ", stuff

print "Let's do some stuff with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
print stuff
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) # super stellar