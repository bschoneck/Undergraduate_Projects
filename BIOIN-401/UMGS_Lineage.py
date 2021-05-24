#!/usr/local/bin/python3
#compare3.py

from collections import Counter
import math

filename_in_1 = "num_proteins.txt"
filename_in_2 = ["DiamondResults/UMGS", " ", ".tsv"]
filename_in_3 = ["fromUniProt/uniprotUMGS", " ", ".tab"]

filename_out = "UniProtReport(F).txt"

UMGS = ['1038', '1059', '1073', '1092', '118', '1189', '121', '1233', '1256', '126', '1268', '1287', '1316', '1322', '1329', '1338', '1355', '136', '1403', '141', '1414', '144', '15', '1500', '151', '1535', '1552', '158', '17', '170', '1745', '175', '1753', '1764', '177', '1774', '181', '1812', '1817', '183', '1857', '1884', '1894', '1912', '1926', '1956', '1959', '199', '2003', '201', '2025', '2035', '205', '2076', '2079', '208', '220', '225', '227', '248', '255', '26', '269', '282', '29', '304', '328', '33', '347', '351', '369', '38', '380', '39', '4', '41', '410', '411', '422', '426', '43', '437', '463', '47', '475', '479', '480', '488', '504', '52', '54', '561', '564', '566', '572', '573', '59', '6', '63', '65', '672', '676', '682', '691', '74', '744', '760', '766', '774', '776', '78', '795', '813', '816', '89', '90', '908', '920', '923', '93', '935', '94', '971', '987']

#UMGS = ['1038', '1059']

separator = ""

file_in = open(filename_in_1, "r")
num_proteins = []
for line in file_in:
    line = line.strip('\n')
    temp = line.split()
    templst = []
    templst.append(temp[0][4:])
    templst.append(temp[1])
    num_proteins.append(templst)
file_in.close()
#print(num_proteins)

file_out = open(filename_out, "w")

for file_num in range(len(UMGS)):
    print("Working on UMGS", UMGS[file_num], sep='', end='', flush=True)
    filename_in_2_temp = filename_in_2
    filename_in_2_temp[1] = UMGS[file_num]
    filename_in_2_temp = separator.join(filename_in_2_temp)

    file_in = open(filename_in_2_temp, "r")

    lst1 = []
    lst11 = []

    for line in file_in:
        line.strip()
        temp = line.split()
        lst1.append(temp[0])
        lst11.append(temp[1][:-6])
    file_in.close()

    filename_in_3_temp = filename_in_3
    filename_in_3_temp[1] = UMGS[file_num]
    filename_in_3_temp = separator.join(filename_in_3_temp)

    file_in = open(filename_in_3_temp, "r")

    lst2 = []
    lst22 = []

    for line in file_in:
        line.strip()
        temp = line.split('\t')
        if temp[0][0] == 'y' and temp[0][1] == 'o':
            continue
        # ONLY LOOKING AT GENUS
        if len(temp) > 6:
            temp[6] = temp[6].strip('\n')
            if temp[6] != '':
                lst22.append(temp[1])
                lst2.append(temp[6])
    file_in.close()

    print(".", end='', flush=True)

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

    print(".", end='', flush=True)

    for i in range(len(lst1)):
        already_in = False
        is_in = False
        if lst1[i] != current:
            current = lst1[i]
            templst = []

        if c[i] != -1:
            temp = lst2[c[i]]
            is_in = True

        if is_in == True:
            for j in range(len(templst)):
                if temp == templst[j]:
                    already_in = True
                    break
            if already_in == False:
                templst.append(temp)
                lst3.append(temp)

    print(".", end='', flush=True)

    z = Counter(lst3)
    dict(sorted(z.items(), key=lambda item: item[1]))

    for i in range(len(num_proteins)):
        if num_proteins[i][0] == UMGS[file_num]:
            popped = num_proteins.pop(i)
            half_p = math.floor(int(popped[1]) / 2)
            break

    file_out.write("UMGS")
    file_out.write(UMGS[file_num])
    file_out.write("\t")
    file_out.write("50%=")
    file_out.write(str(half_p))
    file_out.write("\t")

    for i in range(len(list(z))):
        if z[list(z)[i]] >= half_p:
            file_out.write(list(z)[i])
            file_out.write("=")
            file_out.write(str(z[list(z)[i]]))
            file_out.write("\t")
    file_out.write("\n")
    print("Finished ", end='', flush=True)
    print(file_num + 1, "/", len(UMGS), sep='')
file_out.close()
