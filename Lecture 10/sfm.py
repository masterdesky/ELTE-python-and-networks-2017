import random
import sys


# Insert link
def insertLink(i, j, node2Degree, node2NeiSet, indexList):
    # Put j into i' neighbours, and increment degree
    # Note: here I assumed that if i is in node2NeiSet,
    # then it's also in node2Degree
    if i in node2NeiSet:
        node2NeiSet[i].add(j)
        node2Degree[i] += 1
    else:
        node2NeiSet[i] = {j}
        node2Degree[i] = 1
    # Do the same in the other direction
    if j in node2NeiSet:
        node2NeiSet[j].add(i)
        node2Degree[j] += 1
    else:
        node2NeiSet[j] = {i}
        node2Degree[j] = 1
    # Add i and j to indexList
    indexList.extend((i, j))


# Measure degree maximum
def max_deg(node2Degree, t, t2dmax):
    t2dmax[t] = max(node2Degree.values())


# make SF network
def sfdmax(m, t_max, t_ratio, node2Degree, t2dmax, node2NeiSet, indexList):
    # connect all pairs among the m initial nodes
    for i in range(m):
        for j in range(i+1, m):
            insertLink(i, j, node2Degree, node2NeiSet, indexList)
    max_deg(node2Degree, 0, t2dmax)
    t_last = 1
    for t in range(1, t_max + 1):
        # new node, index = m+t-1
        newNode = m + t - 1
        # select m neighbours from the old nodes
        k = 0
        while k < m:
            # Choose an old node from indexList
            oldNode = indexList[random.randint(0, len(indexList)-1)]
            # Connect oldNode and newNode if not connected
            if newNode not in node2NeiSet[oldNode]:
                insertLink(oldNode, newNode,
                           node2Degree, node2NeiSet, indexList)
                k += 1
        if t/t_last > t_ratio:
            max_deg(node2Degree, t, t2dmax)
            t_last = t


def print_data(t2dmax):
    for k in t2dmax:
        print("%d %d" % (k, t2dmax[k]))


# main
t2dmax = {}
node2NeiSet = {}
node2Degree = {}
indexList = []
# Read variables from cmd line
# m, t_max, t_ratio   (t_ratio: only write result when t/t_last>t_ratio
_, m, t_max, t_ratio = sys.argv
m = int(m)
t_max = int(t_max)
t_ratio = float(t_ratio)
sfdmax(m, t_max, t_ratio, node2Degree, t2dmax, node2NeiSet, indexList)
print_data(t2dmax)
