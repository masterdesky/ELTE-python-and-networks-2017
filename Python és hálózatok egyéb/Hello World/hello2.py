import sys
script, infile = sys.argv
_,infile = sys.argv
with open(infile,"r") as f: #with-el nem kell külön bezárni
	name = f.readline().rstrip()
	#print(name)
	#name = name.rstrip() #/n-t leszedi
	#print(">%s<\n" % name)
	print("Hello, %s!" % name)
