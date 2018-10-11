#ER Giant Componient
import sys
import random
#+ matplotlib

#S_1 = (# of nodes in largest comp. / N)
# 1| --------------------------------
#  |                      $
#  |                  $
#  |               $       Veges
#  |             $       N eseten
#  |           $
#  |__________$___________________
#             1                 <k> = pN
# N -> inf eseten <k> = 1-nel tores
# <k> < 1-nrel S_1 = 0

#READ ARGUMENTS
_,n,e = sys.argv

#CONVERT ARGUMENT TO INT
n = int(n)
e = int(e)
# S_1| ---------------------------
#    |                 $
#    |             $
#    |           $
#    |          $
#    |         $
#    |$_$_$__$___________________
#                                 E

#ket nyilvantartas:
#Minden csucshoz a komponens idnexet (akar list is)
#Valamint minden komponens indexe ot a
#node2comp = {i:i for i in range(n)}
node2comp = [_ for _ in range(n)]
#comp2nidelisz[i] is the list of nodes of component i
comp2nodelist = {_:[_] for _ in range(n)}

#node2neiSet[i] os the set of neighborg of node i
node2neiSet = {}
#we assume that p = 2e/(n^2) << 1 && <k> = 2e/n
#eNow is the current number of links in the network
eNow = 0
while eNow < e:
    #try to insert new link -> make sure A and B are not yet connected
        #select new link -> select A != B node
    #IF A and B belong to different components,
        #3 steps: update component index book-keeping
    #insert eedge to the network