import sys
import numpy as np
import matplotlib.pyplot as plt

app = []
values = []
ind = 0

# OPEN FILE AND WRITE VALUES INTO LIST
with open("Atlantic16.txt") as f:
    for lines in f:                         # READ THE FILE LINE BY LINE
        lines = f.readline()                # READ THE ACTUAL LINE INTO A LIST
        for i in range(439,447,1):
            app.append(lines[i])            # PUT THE NUMBERS INTO AN ARRAY
        #print(app)
        #print("".join(app))
        values.append("".join(app))         # MADE A STRING OUT OF AN ARRAY
        app[:] = []                         # CLEAR THE LIST
        #ind = ind+1                        # REPEAT
        #print(ind)                         # GIVE "STRING INDEX OUT
    #print(values)                          # OF RANGE" AT LINE 79662

# X AND Y ARE MARKING THE AXES OF THE COORDINATE SYSTEM
#y, x = np.histogram(data_sorted, bins = 1000)

# USING NUMPY TO CALCULATE THE NEEDED VALUES                #THEN HERE SAY
#cumulative = np.cumsum(y)                                   #NO. JUST NO TO
                                                            #THE PLOTTING
# PLOT THE CCH (CDF) USING MATPLOT
#plt.plot(x[:-1], cumulative, c='red')
#plt.show()                                                  


#SORT DATAS
sorted_data = np.sort(values)

#CALCULATE SOMETHING THAT WAS WRITTEN IN THE CCH CALCULATION TUTORIAL
some_data = 1. * np.arange(len(values)) / (len(values) - 1)

#PLOT THE CCH (CDF) USING MATPLOT                   #HEY IT'S ACTUALLY WORKS!
plt.plot(sorted_data, some_data)                   #BUT CANT PLOT DATA
plt.xlabel('$n$')                                  #BEAUTY ENOUGH... :(
plt.ylabel('$above$')
plt.show()
