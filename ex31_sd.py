print "You enter a dark room with two doors."
print "1. Go to room #1."
print "2. Go to room #2."
print "3. Stay put."


door = raw_input(">")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	print "3. Engage the bear in hand to hand combat."
	
	bear = raw_input(">")
	
	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	elif bear == "3":
		print "After a long a bloody battle, you emerge victorious."
		print "CHEESE CAKE"
	else:
		print "Well doing %s is probably better. Bear runs away." % bear
		
elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input(">")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
		
	else:
		print "The instanity rots your eyes into a pool of muck. Good job!"
		
elif door == "3":
	print "Your mind begins to wander."
	print "CHEESE?"
	print "YES"
	print "NO"
	
	cheese = raw_input(">")
	
	if cheese == "YES" or cheese == "NO":
		print "It's too late, no cheese can save you now."
		
else:
	print "You stumble around and fall on a knife and die. Good job!"