#!/usr/local/bin/python3
#compare3.py

from collections import Counter

fout = open("Diamond_Out_Best_10.txt", "w")
fin = open("DiamondResults/UMGS290.tsv", "r")
Idlst = []
lst2 = []
temp2 = "Hello Darknes My Old Friend"


for line in fin:
    line.strip()
    temp = line.split()
    if temp2 != temp[0]:
        count = 0
        temp2 = temp[0]
    if count < 10:
        count += 1
        Idlst.append(temp[1])

    lst2.append(temp[0])

for i in range(len(Idlst)):
    fout.write(Idlst[i])
    fout.write("\t")
"""
z = Counter(Idlst)
dict(sorted(z.items(), key=lambda item: item[1]))
for i in z:
    #if z[i] > 4:
    fout.write(i)
    fout.write("\t")
    #fout.write(str(z[i]))
    #fout.write("\n")
#print(z)
"""
set = set(lst2)
print(len(set))

fout.close()
