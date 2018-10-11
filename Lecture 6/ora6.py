import sys
import numpy as np
#print(np.arange(0,5)) # Ennek az outputja: [0,1,2,3,4]. Ezt jelenti: [0,5)
# Írjunk egy listát, amiben minden szám annyiszor szerepel, amennyi az ő fokszáma
# === read variables from terminal ===
script, m, tmax, tratio = sys.argv
m = int(m)
tmax = int(tmax)
tratio = float(tratio)


# === make SF-network ===
def stdmax(m,tmax,tratio,node2degree,t2dmax,node_neighbours,index_list):
    # connect all pairs among the m initial nodes
    for i in range(0,m):
        for j in range(i+1,m):
            insertLink(i,j,node2degree,node_neighbours,index_list)
    for t in np.arange(1,1+tmax):
        # new node index: m+t-1
        # select m neighbours from the old nodes

    return valami


# === MAIN ===
node2degree = []
t2dmax = {}
node_neighbours = {}
index_list = []