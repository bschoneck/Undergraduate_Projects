#!/usr/local/bin/python3
#compare3.py

from collections import Counter

fout = open("Diamond_Out_List_Out.txt", "w")
fin = open("Downloads/uniprot-out.tab", "r")
Idlst = []
lst2 = []
lst_first = []
lst_second = []
phylumlst = []
classlst = []
orderlst = []
familylst = []
genuslst = []
temp2 = "Hello Darknes My Old Friend"


for line in fin:
    line = line.replace('\n', '')
    #line.translate({ord('\n'): None})
    line.strip()
    temp = line.split('\t')
    if len(temp) == 1:
        continue
    if temp[0] == "Entry":
        continue
    temp.pop(0)
    for name in range(len(temp)):
        if name == 0:
            phylumlst.append(temp[0])
        elif name == 1:
            classlst.append(temp[1])
        elif name == 2:
            orderlst.append(temp[2])
        elif name == 3:
            familylst.append(temp[3])
        elif name == 4:
            genuslst.append(temp[4])

    lst2.append(temp[0])


for i in range(5):
    if i == 0:
        lst = phylumlst
    elif i == 1:
        lst = classlst
    elif i == 2:
        lst = orderlst
    elif i == 3:
        lst = familylst
    elif i == 4:
        lst = genuslst


    z = Counter(lst)
    dict(sorted(z.items(), key=lambda item: item[1]))
    for i in z:
        fout.write(i)
        fout.write("\t")
        fout.write(str(z[i]))
        fout.write("\n")
    print(z)

set = set(lst2)
print(len(set))

fout.close()
