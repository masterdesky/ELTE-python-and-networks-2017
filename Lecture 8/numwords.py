import re, sys
inFile = sys.argv[0]
with open(inFile, "r") as f:
    string = f.read()
    #print(re.findall(r"\w+", string))
    stringSet = set(re.findall((r"\w+", string)))
    #print(stringSet)
    num2str = sorted(stringSet)
    str2num = {num2str[_]:_ for _ in range(len(num2str))}