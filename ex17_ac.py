from sys import argv
script, from_file, to_file = argv
in_file= open(from_file); out_file = open(to_file,'w')
indata = in_file.read(); out_file.write(indata)