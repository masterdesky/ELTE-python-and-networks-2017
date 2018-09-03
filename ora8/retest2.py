import re, sys
stringlist = ["apple", "pear", "orange"]
patternlist = []

'''
Usable formats in patternlist:
[o|pp]
[arekq] : user-defined
[a-f] : a-tol f-ig minden
[^ap] : nem a vagy p
\w : A-Za-z0-9_ (called word)
\W: not word
\d: digit (0-9)
\D: not digit
\s: ezek kozul valamelyik:
    \ : space
    \S: not space
    \n: uj sor
    \f: LF
    \r: CR (irogep pls)
    \t: ...
\s\s\d\s: negy karakter egymas utan
\s{4} : rogzitett szamlalo

a* : rugalmas szamlalo -> csillag: akarhany karakter
a+ : az elotte levo dologbol egy vagy tobb
a? : szamlalo de szamlalo modosito is lehet
. [^\n]: tetszoleges karakter iveve az uj sor
\w+ : szo karakterbol egy vagy tobb

kereses: digit,.,e,E,-,+:
    [\d\.eE\-\+]+ : ezeket keresi amik a []-on belul vannak

(a|b)* :
'''

for string in stringlist:
    for pattern in patternlist:
        print("Test string = %s, pattern = %s " % (string, pattern),end="") #python3
        if re.search(pattern,string):
            print("OK")
        else:
            print("NOT OK")