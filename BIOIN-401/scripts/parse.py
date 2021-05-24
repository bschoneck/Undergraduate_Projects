from collections import Counter

file1 = open("treeqaOut.txt", "r")
file2 = open("CheckM_Out_temp.txt", "w")
lst = []
kingdomlst = []
phylumlst = []
classlst = []
orderlst = []
familylst = []
genuslst = []
count = 0
for line in file1:
    if line[0] == '-':
        continue
    line.strip()
    #temp = line.split('\n')
    temp = line.split()
    temp2 = temp[3].split("__")
    """
    for name in range(1, len(temp2)):
        temp3 = temp2[name].split(";")
        file2.write(temp3[0])
        file2.write("\t")
        lst.append(temp3[0])
        if name == 1:
            kingdomlst.append(temp3[0])
        elif name == 2:
            phylumlst.append(temp3[0])
        elif name == 3:
            classlst.append(temp3[0])
        elif name == 4:
            orderlst.append(temp3[0])
        elif name == 5:
            familylst.append(temp3[0])
        elif name == 6:
            genuslst.append(temp3[0])
    """
    if len(temp2) > 3 and len(temp2) < 7:
        count += 1
        file2.write(temp[0])
        """
        file2.write("\t")
        for name in range(1, len(temp2)):
            temp3 = temp2[name].split(";")
            file2.write(temp3[0])
            file2.write("\t")
            lst.append(temp3[0])
        """
        file2.write("\n")
print(count)

    #print(temp2)
    #try:
    #    lst.append(temp2[3])
    #except:
    #    continue
"""
file2.write("\n")
print("\n")
for i in range(1,7):
    if  i == 1:
        lst = kingdomlst
    elif i == 2:
        lst = phylumlst
    elif i == 3:
        lst = classlst
    elif i == 4:
        lst = orderlst
    elif i == 5:
        lst = familylst
    elif i == 6:
        lst = genuslst


    z = Counter(lst)
    dict(sorted(z.items(), key=lambda item: item[1]))
    for i in z:
        file2.write(i)
        file2.write("\t")
        file2.write(str(z[i]))
        file2.write("\n")
    print(z)
    file2.write("\n")
    print("\n")
"""
"""
z = Counter(lst)
dict(sorted(z.items(), key=lambda item: item[1]))
for i in z:
    file2.write(i)
    file2.write("\t")
    file2.write(str(z[i]))
    file2.write("\n")
print(z)
"""
file2.close()
