from sys import exit

def straight_ahead():
	print "You've chosen the straight path."
	print "You see a giant pile of food!"
	print "What do you do?"
	
	food = raw_input("> ")
	
	if food == "eat":
		print "You eat a banana."
		print "A wild baby baboon appears!"
		print "He looks MAD."
		print "1. Engage him in hand to hand combat."
		print "2. Run!"
		print "3. Apologise."
		
	baboon = raw_input("> ")
	if baboon == "1":
		print "You engage the baboon in hand to hand combat."
		print "He beats you into submission."
		print "You limp away battered and bloodied, with several teeth marks and broken limbs."
		print "Where do you go now?"
	elif baboon == "2":
		print "You get away."
		print "Barely."
	elif baboon == "3":
		print "The baboon excepts your apology."
		print "He's a very well mannered baboon."
		print "He gives you a banana."
		food == True
	else:
		print "The baboon decides you don't look appetizing."
		print "You decide to leave."
		print "You leave."
	print "This road is done."
	straight_ahead = True
	
	
def left_road():
	print "You feel h
		
