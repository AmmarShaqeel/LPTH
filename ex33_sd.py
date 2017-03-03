def loop(i, numbers, increment, limit):
	while i < limit:
		print "At the top i is %d" % i
		numbers.append(i)
			
		i += increment
		print "Numbers now: ", numbers
		print "At the bottom is %d" % i
			
	print "The numbers: "

	for num in numbers:
		print num