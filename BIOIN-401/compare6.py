#!/usr/local/bin/python3
#compare3.py

from collections import Counter

fout = open("Diamond_Out_List.txt", "w")
fin = open("DiamondResults/UMGS290.tsv", "r")
Idlst = []
lst2 = []
lst_first = []
lst_second = []
temp2 = "Hello Darkness My Old Friend"


for line in fin:
    line.strip()
    temp = line.split()
    tempbest = temp[1]
    tempbest = tempbest[:5]
    if temp2 != temp[0]:
        lst_first = []
        temp2 = temp[0]
    not_in = True
    for i in range(len(lst_first)):
        if tempbest == lst_first[i]:
            not_in = False
    if not_in == True:
        lst_first.append(tempbest)
        lst_second.append(tempbest)

    lst2.append(temp[0])


z = Counter(lst_second)
dict(sorted(z.items(), key=lambda item: item[1]))
for i in z:
    if z[i] > 4:
        fout.write(i)
        fout.write("\t")
        fout.write(str(z[i]))
        fout.write("\n")
print(z)

set = set(lst2)
print(len(set))

fout.close()
