#!/usr/local/bin/python3
# GENERATE FIGURE 2B

from collections import Counter
from operator import itemgetter
import time

UMGS = "UMGS179,UMGS183,UMGS84,UMGS264,UMGS470,UMGS2067,UMGS90,UMGS86,UMGS125,UMGS463,UMGS39,UMGS759,UMGS1710,UMGS365,UMGS132,UMGS184,UMGS537,UMGS137,UMGS762,UMGS160"
UMGS = UMGS.split(",")

lst1 = []
fin = open("taxonomy_umgs.tab", "r")
for line in fin:
    line.strip('\n')
    temp = line.split('\t')
    templst = []
    if temp[0] == "UMGS_ID":
        continue
    if len(temp) < 2:
        continue
    templst.append(temp[0])
    templst.append(temp[1])
    for i in range(1,len(temp)):
        if temp[(len(temp) - i)].strip('\n') != "NA":
            templst.append(temp[(len(temp) - i)].strip('\n'))
            break
    lst1.append(templst)
fin.close()

lst = []
fin = open("bwa_presence-absence_t4.csv", "r")
fout = open("prevalence_t4.txt", "w")
for line in fin:
    line.strip('\n')
    temp = line.split(',')
    templst = []
    count = 0
    if temp[0] == "Genome":
        continue
    #if temp[0][0] == 'E' or temp[0][0] == 'S' or temp[0][0] == 'D': # for their results
    #if temp[0][0] == 'U' or temp[0][0] == 'S' or temp[0][0] == 'D': # for our results
    if temp[0] in UMGS: # for cloud results
        templst.append(temp[0])
        for i in range(1, len(temp)):
            if temp[i] == "1":
                count += 1
        templst.append(count)
        lst.append(templst)

"""
sortedlst = sorted(lst, key=itemgetter(1))
print(sortedlst[len(sortedlst)-1][0])
print(lst1[0][1])
for i in range(1,21):
    temp = sortedlst.pop()
    for j in range(len(lst1)):
        if temp[0] == lst1[j][1]:
            fout.write(lst1[j][0])
            fout.write("(")
            fout.write(lst1[j][2])
            fout.write(")")
            fout.write("\t")
            fout.write(str(temp[1]))
            fout.write("\n")
            break
"""
for i in range(len(lst)):
    temp = lst.pop()
    fout.write(temp[0])
    fout.write("\t")
    fout.write(str(temp[1]))
    fout.write("\n")




"""
for i in range(1,21):
    fout.write(sortedlst[len(sortedlst)-i][0])
    fout.write("\t")
    fout.write(str(sortedlst[len(sortedlst)-i][1]))
    fout.write("\n")
#time.sleep(1)
"""


fout.close()
