# generate a Scale-Free network and write its degree distribution
import sys, random
'''import matplotlib.pyplot as plt'''

# read command-line arguments
_, m, t, outFileImg = sys.argv
m = int(m)
t = int(t)
# m: parameter of the SF model
# t: total time for which the SF model should grow
# Let's start with m=2 nodes connected to each other

# Number of nodes in the Scale-Free network:
# N(t): at time t the number of nodes   N(t) = m  +  t   (Eq.1)

# Number of links is                    E(t) = m * t   (Eq.2)

# IF we know N and E, THEN what is m and what is t?
# From Eq.1 we have  m = N - t
# Substitute into Eq.2:  E = ( N - t ) * t
#
# Let's solve this:  t^2 - N * t + E = 0
#
# t = N - sqrt { N^2 - 4 E } / 2
# m = N - t
#
# Example:
# N = 2357, E = 40765
# t = { 2357 - sqrt{ 2357^2 - 4 * 40765 } } / 2
# t = 2340
# m = 17
# t^2 + 2t + 1 = 0
# t_{1,2} = { -2 +/- sqrt{4-4} } / 2

# ---- function definitions ----

def insert_node(newNode,node2neiSet):

    # insert a single node into the network
    # ! without inserting links

    # all we need to do is to make sure that the
    # neighbor set of this node is declared
    if newNode not in node2neiSet:
        node2neiSet[newNode] = set()

# ----------

def insert_link(nodeA,nodeB,node2neiSet,nodeNameList):

    # IF nodeA or nodeB receives its first neighbor,
    for myNode in nodeA, nodeB:
        if myNode not in node2neiSet:
            # THEN declare the set of neighbors of this node
            node2neiSet[myNode] = set()

    # nodeB is a neighbor of nodeA
    node2neiSet[nodeA].add(nodeB)

    # nodeA is a neighbor of nodeB
    node2neiSet[nodeB].add(nodeA)

    # the degree of nodeA and the degree of nodeB grows by 1
    for myNode in nodeA, nodeB:
        nodeNameList.append(myNode)

# ----------

# Generate a classical random graph (Erdos-Renyi network)
# with n nodes and e links
#
# !!! NOTE: we are assuming here that the network is sparse,
# in other words,  e << n ( n - 1 ) / 2

def generate_er(n,e,node2neiSet):

    # add the links one-by-one
    for e_counter in range(e):

        # we have not yet placed the new link
        placed_new_link = 0

        # try to place the new link until we succeed
        while not placed_new_link:

            # are the two nodes the same? default value: yes
            two_nodes_are_the_same = 1

            # pick two nodes at random
            # try as long as the two nodes are the same
            while two_nodes_are_the_same:
                # select the two nodes randomly
                nodeA, nodeB = random.sample(range(n),2)
                # check, if they are different
                if nodeA != nodeB:
                    two_nodes_are_the_same = 0

            # take both nodes separately
            for node in nodeA,nodeB:
                # IF there is no such key yet in the dictionary
                # in other words: if this node has no neighbor yet,
                if node not in node2neiSet:
                    # THEN declare the set of its neighbors as an empty set
                    node2neiSet[node] = set()

            # IF the two nodes are not connected,
            if nodeB not in node2neiSet[nodeA]:
                # THEN connect them both ways:
                # save both as a neighbor of the other
                node2neiSet[nodeA].add(nodeB)
                node2neiSet[nodeB].add(nodeA)
                # AND set placed_new_link = 1
                placed_new_link = 1

# ----------

def generate_sf(m,t,node2neiSet):

    # nodeNameList:
    # contains each node's name as many times as the degree of the node
    nodeNameList = []

    # initialize the network with a complete graph of m nodes
    for nodeA in range(m):
        for nodeB in range(m):
            # make sure that nodeB is larger than nodeA
            if nodeA < nodeB:
                insert_link(nodeA,nodeB,node2neiSet,nodeNameList)

    ### test
    #print(node2neiSet)
    #print(nodeNameList)

    # one-by-one insert the t new nodes into the network
    for current_time in range(t):
        # - the new node selects m of the old nodes
        # - each old node is selected with a probability
        #   proportional to its node degree
        # - intialize the set of selected nodes as an empty set
        set_of_selected_old_nodes = set()
        # select m different nodes
        while len(set_of_selected_old_nodes) < m:
            # add a single randomly selected item
            set_of_selected_old_nodes.add(random.choice(nodeNameList))
            #### test
            #sys.stderr.write("selecting at time step %d\n" % current_time)
            #sys.stderr.flush()

        # connect each of the selected old nodes to the new node
        for oldNode in set_of_selected_old_nodes:
            # connect the current old node to the new node
            insert_link(oldNode, m+current_time, node2neiSet, nodeNameList)

        ### test
        #print(node2neiSet)
        #print(nodeNameList)

        #### test
        #sys.stderr.write("Done t: %d\n" % current_time)
        #sys.stderr.flush()

# ---------

def insertNodes_saveSmax(node2neiSet_all,nodeList,order_how,nodeNum2sMax):

    # --- initializing the order in which nodes should be inserted ---

    # the list of all nodes in sorted order
    nodeList_ord = nodeList

    # order nodes randomly or in the ascending order of their degrees
    if order_how == 'rnd':
        random.shuffle(nodeList_ord)
    elif order_how == 'deg':
        # the degree of each node
        node2deg = { _:len(node2neiSet_all[_]) for _ in node2neiSet_all }
        ### test: print the node degrees
        #print(node2deg)
        # the list of nodes in the ascending order of their degrees
        nodeList_ord = sorted(nodeList,key=node2deg.get)
    else:
        print("Error (insertNodes_saveSmax), no such order: '%s'" % order_how)

    ### test: print the sorted list of nodes
    #print(nodeList_ord)

    # --- initializing sMax and the book-keeping of graph components ---

    # initially all nodes are isolated and are separate graph components
    # for each node: initialize its component index as the index of the node
    node2comp = { _:_ for _ in nodeList }
    # for each component: initialize the list of the nodes it contains
    comp2nodeList = { _:[_] for _ in nodeList }

    # node2neiSet_all: the full network
    # node2neiSet_now: the network as we are building it up
    #                  by inserting nodes and links
    node2neiSet_now = {}
    # nodeNameList: the number of times that this list contains the
    #               name of a node is the degree of that node
    nodeNameList = []

    # with 0 nodes in the system: the largest component has size=0
    # in other words: nodeNum2sMax[0] = 0
    nodeNum2sMax.append(0)

    # --- inserting nodes, following sMax ---

    # insert nodes in the selected order
    for newNode in nodeList_ord:

        ### test: print the size of the largest component
        #sys.stdout.write("%s %d, " % (order_how,newNode)); print(nodeNum2sMax);
        #print(node2neiSet_all)
        ### test: print the current network
        #print("nw: ",node2neiSet_now)

        # default value of the largest component size
        # after inserting the new node:
        # same size as before inserting this node
        nodeNum2sMax.append(nodeNum2sMax[-1])

        # insert the new node into the network
        insert_node(newNode,node2neiSet_now)
        # loop through the list of links of this new node
        # and insert those that connect it to already inserted nodes
        for neighborNode in node2neiSet_all[newNode]:
            # check if the neighbor node is already inserted
            if neighborNode in node2neiSet_now.keys():
                # connect the two nodes
                insert_link(newNode,neighborNode,node2neiSet_now,nodeNameList)
                # IF the two connected nodes have a different component index,
                # THEN merge these two graph components
                if node2comp[newNode] != node2comp[neighborNode]:
                    # get the higher and the lower of the two component indexes
                    cLO, cHI = sorted([node2comp[newNode], node2comp[neighborNode]])
                    # for each node that belongs to the component cHI
                    for node_cHI in comp2nodeList[cHI]:
                        # set the component index of this node to cLO
                        node2comp[node_cHI] = cLO
                        # append this node to the list of the nodes
                        # of the component cLO
                        comp2nodeList[cLO].append(node_cHI)
                    # delete the list of the nodes of component cHI
                    del comp2nodeList[cHI]
                    # set size of largest component by checking if cLO has become the largest
                    if nodeNum2sMax[-1] < len(comp2nodeList[cLO]):
                        nodeNum2sMax[-1] = len(comp2nodeList[cLO])

        ### test: print the current network and the size of the largest component
        #print(node2neiSet_now)
        #print(nodeNum2sMax)

    ### test: print the network
    #print(node2neiSet_now)

    ### test: print the current network and the size of the largest component
    #print(node2neiSet_now)
    #print(' '.join([str(_) for _ in nodeNum2sMax]))

# ---- main ----

# node2neiSet{node} is the set of the neighbors of "node"
# "er": Erdos-Renyi network model, "sf": scale-free network model
node2neiSet_er = {}
node2neiSet_sf = {}

# generate an ER network with m+t nodes and m*t links
generate_er(m+t,m*t,node2neiSet_er)

# generate a Scale-Free network with parameter m, grown for time t
generate_sf(m,t,node2neiSet_sf)

# Starting from an empty graph:
# insert nodes and their links to already inserted nodes
# (1) in a random order of the nodes
# (2) in the ascending order of node degrees
# During this process: save the size of the largest component
# as a function of the number of nodes

nodeNum2sMax_er_rnd = []
insertNodes_saveSmax(node2neiSet_er,list(node2neiSet_er.keys()),"rnd",nodeNum2sMax_er_rnd)
nodeNum2sMax_er_deg = []
insertNodes_saveSmax(node2neiSet_er,list(node2neiSet_er.keys()),"deg",nodeNum2sMax_er_deg)

nodeNum2sMax_sf_rnd = []
insertNodes_saveSmax(node2neiSet_sf,list(node2neiSet_sf.keys()),"rnd",nodeNum2sMax_sf_rnd)
nodeNum2sMax_sf_deg = []
insertNodes_saveSmax(node2neiSet_sf,list(node2neiSet_sf.keys()),"deg",nodeNum2sMax_sf_deg)
'''
# --- output: print the four graphs ---
fig, ax = plt.subplots()
# set axis limits
ax.set_xlim(left=0,right=m+t)
ax.set_ylim(bottom=0,top=m+t)
# set axis labels and plot title
ax.set_xlabel("Number of nodes in the network")
ax.set_ylabel("Size of largest component")
plt.title("ER - Erdos-Renyi, SF - Scale-Free (m=%d, t=%d, n=m+t, e=m*t)\nNode removal order: rnd - random, deg - desc. by degree" % (m,t),fontsize=12)
# plot four graphs
plt.plot(nodeNum2sMax_er_rnd,label="ER rnd",ls='dotted')
plt.plot(nodeNum2sMax_er_deg,label="ER deg",ls='dashed')
plt.plot(nodeNum2sMax_sf_rnd,label="SF rnd",ls='dashdot')
plt.plot(nodeNum2sMax_sf_deg,label="SF deg",ls='solid')
# set the legend
plt.legend(loc='upper left')
# save the figure and close it
fig.savefig(outFileImg)
plt.close(fig)
'''