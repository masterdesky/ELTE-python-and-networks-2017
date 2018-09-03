import sys
_,name,num = sys.argv
num = int(num)
def nameMult(name,num):
	#print(type(num))
	name = name*num
	print("a name = %s" % name)
	#return name
#print(nameMult(name,num))
nameMult(name,num)
print("b name = %s" % name)
