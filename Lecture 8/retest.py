import re
string = "apple pen pineapple"
pattern = "\w+"
print("match eredmeny:")
if re.match(pattern, string): #MATCH CSAK AZ ELEJET NEZI A FUGGVENYNEK!!!!!!
    print("string = %s, pattern = %s, match OK" % (string,pattern))
    print('\n')
print("search eredmeny:")
if re.search(pattern, string):
    print("string = %s, pattern = %s, match OK" % (string,pattern))
    print('\n')
print("findall eredmenye:")
if re.search(pattern, string):
    print(re.findall(string,pattern))