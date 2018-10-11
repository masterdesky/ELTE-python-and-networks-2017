import sys
import random

#FROM INPUT READ A NUMBER. THIS WILL BE THE 
#LENGHT OF THE LIST FOR RANDOM NUMBERS
script, i = sys.argv
i = int(i)

#CREATE LISTS INSIDE LISTS WITH LOGARITMICAL LENGHTS
#THEY CONTAIN MEANS AND MEDIANS OF 10 RANDOM NMRS, 100 RANDOM NMRS,
#1000 RANDOM NMRS, ... 10**I RANDOM NMRS. (I>=1)
log_range = 10
l = []
diff = []
meanlist = []
medlist = []
for c in range(0,i,1):
	for n in range(0,log_range,1):
		l.append(random.random())
	#CALCULATE MEAN
	mean = (sum(l) / len(l))

	#CALCULATE MEDIAN
	l.sort()
	median = ((l[len(l)/2] + l[(len(l)-1)/2]) / 2)

	#PUT THEM INTO LISTS
	meanlist.append(mean)
	medlist.append(median)
	
	#LOGARITMICAL STEP
	log_range *= 2

	#CLEAR LIST OF RANDOM NUMBERS FOR NEXT STEP OF LOOP
	l[:] = []
	
#DIFFERENCE OF MEDIANS
for k in range(0,i-1,1):
	diff.append(medlist[i-k-1]-medlist[0])

#PRINT EVERYTHING
print "mean: ",meanlist
print "median: ",medlist
print "difference: ",diff
