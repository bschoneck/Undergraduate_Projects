#!/usr/local/bin/python3
#compare3.py

from collections import Counter

fout = open("Diamond_Out_Best.txt", "w")
fin = open("DiamondResults/UMGS290.tsv", "r")
Idlst = []
lst2 = []
temp2 = "Hello Darknes My Old Friend"


for line in fin:
    line.strip()
    temp = line.split()
    if temp2 != temp[0]:
        temp2 = temp[0]
        Idlst.append(temp[1])
    lst2.append(temp[0])

#z = Counter(Idlst)
#dict(sorted(z.items(), key=lambda item: item[1]))
for i in range(len(Idlst)):
    #if z[i] > 4:
    fout.write(Idlst[i])
    fout.write("\t")
    #fout.write(str(z[i]))
    #fout.write("\n")
#print(z)
set = set(lst2)
print(len(set))

fout.close()
