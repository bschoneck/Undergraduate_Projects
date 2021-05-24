#!/usr/local/bin/python3
#compare3.py

from collections import Counter
import math
import time
import bisect

lst1 = []
lst11 = []
fin = open("DiamondResults/UMGS290.tsv", "r")
for line in fin:
    line.strip()
    temp = line.split()
    lst1.append(temp[0])
    lst11.append(temp[1][:-6])
fin.close()

#print(lst11)

lst2 = []
lst22 = []
fin = open("fromUniProt/uniprotUMGS290.tab", "r")
for line in fin:
    line.strip('\n')
    temp = line.split('\t')
    if temp[0][0] == 'y' and temp[0][1] == 'o':
        continue
    # ONLY LOOKING AT GENUS
    if len(temp) > 6:
        temp[6] = temp[6].strip('\n')
        if temp[6] != '':
            lst22.append(temp[1])
            lst2.append(temp[6])
fin.close()

#fout = open("Diamond_Out_Final.txt", "w")
current = "Hello Darknes My Old Friend"
lst3 = []
c = []
for n in range(len(lst11)):
    c.append(0)

s = set(lst22)
for i, x in enumerate(lst11):
    if x in s:
        c[i] = lst22.index(x)
    else:
        c[i] = -1

for i in range(len(lst1)):
    already_in = False
    is_in = False
    if lst1[i] != current:
        current = lst1[i]
        templst = []

    if c[i] != -1:
        temp = lst2[c[i]]
        is_in = True

    """
    for k in range(len(lst2)):
        if lst11[i] == lst22[k]:
            temp = lst2[k]
            is_in = True
            break
    """
    if is_in == True:
        for j in range(len(templst)):
            if temp == templst[j]:
                already_in = True
                break
        if already_in == False:
            templst.append(temp)
            lst3.append(temp)
            #print(temp)

z = Counter(lst3)
dict(sorted(z.items(), key=lambda item: item[1]))
#for i in range(len(Idlst)):
    #if z[i] > 4:
    #fout.write(Idlst[i])
    #fout.write("\t")
    #fout.write(str(z[i]))
    #fout.write("\n")
print(z)
#set = set(lst2)
#print(len(set))

#fout.close()
