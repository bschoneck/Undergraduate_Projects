#test8.py

from collections import Counter
from os import listdir, rename
from os.path import isfile, join

onlyfiles = [f for f in listdir("totals") if isfile(join("totals", f))]
count = 1
for file in onlyfiles:
    temp = file[7:-10]
    if temp != "":
        print(temp)
    if (count % 100) == 0 :
        print(count)
    count += 1

#print(len(onlyfiles))
