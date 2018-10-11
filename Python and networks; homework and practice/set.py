import sys
_,infile = sys.argv

with open(infile,"r") as f:
	#my_str = f.read()
	my_set = set()
	[my_set.add(char) for char in f.read()]
	#for char in my_str:
	#	my_set.add(char)
	print(my_set)
