#PDF
#histogram and pdf of char occurence numbers
#-------------FUNCTIONS-------------
import sys
scriptFile, outFile = sys.argv
def file2charHist(inFile, h):
    with open(inFile, "r") as f:
        for char in f.read():
            #TEST 1
            #print char
            #ff we have not seen the key "char"
            if char not in h:
                h[char] = 0
            #in all cases
            h[char] += 1
    #TEST 2
    #print(h)
def list2pdf(list):
    #count number of occurences from list
    #h[n] is the number of times that "n" appears in list
    #assumption: h.values are int
    h = {}
    for n in list:
        #if we have not seen n
        if n not in h:
            #set its usage number to 0
            h[n] = 0
        #in all cases h[n] grows
        h[n] += 1

    #TEST 3
    print(h)
    return{int(_):1.0*h[_]/len(list) for _ in h}

#-------------MAIN-------------
#h[a] is the number of "a" characters in the input file
h = {}
file2charHist(scriptFile, h)
#pfd[h] is the probabiliyty of using a character n times
pdf = list2pdf(h.values())

#-------------TEST PRINTS-------------
print(pdf)
#print(h)



#HÁZI: legalább 1MB txt file, nézzük meg hány 3as karaktercsoport van benne
#pld: ABCDEFGHIJKLMNOPQRSTUVWXYZ
#ABC-DEF #hogy egy ilyennek hány szomszédja van az a fokszáma: ABC fokszáma 1
#BCD-EFG #BCD fokszáma 1
#CDE-FGH #CDE fokszáma 1
#ABC-DEF-GHI #DEF fokszáma 2
#stb stb stb
#konkrétan a CCDF a házi