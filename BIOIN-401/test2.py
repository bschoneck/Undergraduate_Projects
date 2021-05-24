#!/usr/local/bin/python3
#compare3.py

from collections import Counter
import math
import time

filename_in_1 = "num_proteins.txt"
filename_in_2 = ["DiamondResults/", " "]
filename_in_3 = "UniProtRef.tab"

filename_out = "UniProtReport2_2(F).txt"

# UMGS1128 missing
#UMGS = "UMGS479,UMGS1189,UMGS1817,UMGS2041,UMGS74,UMGS6,UMGS94,UMGS104,UMGS164,UMGS204,UMGS256,UMGS284,UMGS289,UMGS290,UMGS292,UMGS293,UMGS294,UMGS295,UMGS296,UMGS297,UMGS298,UMGS299,UMGS300,UMGS301,UMGS302,UMGS303,UMGS305,UMGS306,UMGS307,UMGS308,UMGS309,UMGS310,UMGS311,UMGS312,UMGS313,UMGS314,UMGS315,UMGS316,UMGS317,UMGS318,UMGS319,UMGS320,UMGS321,UMGS322,UMGS323,UMGS324,UMGS325,UMGS326,UMGS327,UMGS334,UMGS358,UMGS375,UMGS376,UMGS377,UMGS378,UMGS379,UMGS381,UMGS382,UMGS383,UMGS384,UMGS385,UMGS386,UMGS387,UMGS388,UMGS389,UMGS390,UMGS391,UMGS393,UMGS394,UMGS395,UMGS396,UMGS397,UMGS398,UMGS399,UMGS414,UMGS425,UMGS427,UMGS428,UMGS429,UMGS430,UMGS441,UMGS442,UMGS443,UMGS445,UMGS446,UMGS447,UMGS448,UMGS449,UMGS450,UMGS466,UMGS467,UMGS481,UMGS485,UMGS487,UMGS498,UMGS506,UMGS510,UMGS511,UMGS512,UMGS513,UMGS514,UMGS515,UMGS516,UMGS517,UMGS518,UMGS519,UMGS545,UMGS582,UMGS585,UMGS586,UMGS587,UMGS588,UMGS589,UMGS590,UMGS595,UMGS616,UMGS623,UMGS633,UMGS639,UMGS640,UMGS641,UMGS642,UMGS643,UMGS644,UMGS645,UMGS649,UMGS651,UMGS652,UMGS653,UMGS666,UMGS674,UMGS684,UMGS701,UMGS704,UMGS714,UMGS716,UMGS719,UMGS720,UMGS721,UMGS722,UMGS723,UMGS724,UMGS727,UMGS741,UMGS742,UMGS745,UMGS751,UMGS753,UMGS779,UMGS783,UMGS784,UMGS787,UMGS788,UMGS789,UMGS790,UMGS801,UMGS804,UMGS806,UMGS817,UMGS819,UMGS820,UMGS825,UMGS833,UMGS844,UMGS850,UMGS851,UMGS852,UMGS853,UMGS876,UMGS877,UMGS878,UMGS888,UMGS892,UMGS909,UMGS912,UMGS919,UMGS921,UMGS925,UMGS938,UMGS943,UMGS955,UMGS959,UMGS962,UMGS969,UMGS972,UMGS988,UMGS989,UMGS994,UMGS996,UMGS1009,UMGS1013,UMGS1022,UMGS1023,UMGS1026,UMGS1030,UMGS1031,UMGS1047,UMGS1074,UMGS1075,UMGS1077,UMGS1082,UMGS1086,UMGS1089,UMGS1094,UMGS1095,UMGS1100,UMGS1112,UMGS1117,UMGS1131,UMGS1139,UMGS1146,UMGS1152,UMGS1154,UMGS1160,UMGS1161,UMGS1165,UMGS1166,UMGS1173,UMGS1174,UMGS1183,UMGS1184,UMGS1190,UMGS1200,UMGS1203,UMGS1207,UMGS1209,UMGS1219,UMGS1220,UMGS1242,UMGS1252,UMGS1262,UMGS1270,UMGS1274,UMGS1277,UMGS1278,UMGS1282,UMGS1300,UMGS1309,UMGS1319,UMGS1321,UMGS1333,UMGS1336,UMGS1339,UMGS1341,UMGS1349,UMGS1354,UMGS1376,UMGS1378,UMGS1380,UMGS1386,UMGS1401,UMGS1409,UMGS1417,UMGS1420,UMGS1421,UMGS1424,UMGS1439,UMGS1442,UMGS1444,UMGS1465,UMGS1475,UMGS1480,UMGS1482,UMGS1483,UMGS1489,UMGS1497,UMGS1499,UMGS1501,UMGS1530,UMGS1542,UMGS1545,UMGS1546,UMGS1549,UMGS1558,UMGS1565,UMGS1567,UMGS1586,UMGS1589,UMGS1597,UMGS1606,UMGS1608,UMGS1627,UMGS1631,UMGS1638,UMGS1667,UMGS1680,UMGS1683,UMGS1695,UMGS1701,UMGS1706,UMGS1720,UMGS1721,UMGS1724,UMGS1726,UMGS1729,UMGS1732,UMGS1742,UMGS1743,UMGS1747,UMGS1755,UMGS1763,UMGS1767,UMGS1779,UMGS1790,UMGS1800,UMGS1816,UMGS1834,UMGS1836,UMGS1841,UMGS1853,UMGS1862,UMGS1873,UMGS1874,UMGS1879,UMGS1905,UMGS1910,UMGS1913,UMGS1920,UMGS1921,UMGS1928,UMGS1935,UMGS1936,UMGS1937,UMGS1943,UMGS1949,UMGS1967,UMGS1969,UMGS1970,UMGS1985,UMGS2002,UMGS2006,UMGS2021,UMGS2029,UMGS2043,UMGS2047,UMGS2050,UMGS2052,UMGS2058,UMGS2059,UMGS2064,UMGS2066,UMGS93,UMGS1745,UMGS26,UMGS33,UMGS190,UMGS235,UMGS272,UMGS417,UMGS431,UMGS468,UMGS675,UMGS854,UMGS1046,UMGS1142,UMGS1371,UMGS1381,UMGS1632,UMGS1861,UMGS1948,UMGS1963,UMGS1991,UMGS304,UMGS380,UMGS634,UMGS1080,UMGS1121,UMGS1629,UMGS774,UMGS1926,UMGS63,UMGS65,UMGS148,UMGS149,UMGS223,UMGS418,UMGS170,UMGS1894,UMGS118,UMGS1414,UMGS1922,UMGS1753,UMGS561,UMGS480,UMGS579,UMGS648,UMGS654,UMGS857,UMGS1292,UMGS1837,UMGS328,UMGS422,UMGS540,UMGS552,UMGS933,UMGS1093,UMGS1213,UMGS1265,UMGS1505,UMGS227,UMGS816,UMGS29,UMGS971,UMGS1130,UMGS1896,UMGS208,UMGS282,UMGS332,UMGS407,UMGS647,UMGS984,UMGS1005,UMGS1064,UMGS1137,UMGS1201,UMGS1511,UMGS1514,UMGS908,UMGS1073,UMGS572,UMGS410,UMGS1912,UMGS676,UMGS1956,UMGS1233,UMGS41,UMGS220,UMGS939,UMGS935,UMGS1268,UMGS1552,UMGS175,UMGS177,UMGS1055,UMGS1974,UMGS2079,UMGS351,UMGS682,UMGS961,UMGS1328,UMGS1639,UMGS1825,UMGS2030,UMGS4,UMGS920,UMGS1687,UMGS158,UMGS1287,UMGS1406,UMGS17,UMGS52,UMGS79,UMGS80,UMGS82,UMGS88,UMGS101,UMGS138,UMGS152,UMGS169,UMGS229,UMGS438,UMGS453,UMGS578,UMGS600,UMGS681,UMGS725,UMGS786,UMGS803,UMGS849,UMGS866,UMGS944,UMGS960,UMGS1027,UMGS1238,UMGS1288,UMGS1314,UMGS1356,UMGS1423,UMGS1425,UMGS1438,UMGS1440,UMGS1476,UMGS1516,UMGS1531,UMGS1543,UMGS1553,UMGS1563,UMGS1570,UMGS1576,UMGS1594,UMGS1604,UMGS1609,UMGS1612,UMGS1630,UMGS1640,UMGS1642,UMGS1650,UMGS1652,UMGS1660,UMGS1663,UMGS1666,UMGS1672,UMGS1673,UMGS1677,UMGS1681,UMGS1689,UMGS1699,UMGS1711,UMGS1734,UMGS1740,UMGS1754,UMGS1781,UMGS1782,UMGS1788,UMGS1796,UMGS1843,UMGS1852,UMGS1864,UMGS1897,UMGS1901,UMGS1917,UMGS1925,UMGS1933,UMGS1968,UMGS1983,UMGS1988,UMGS1994,UMGS1995,UMGS2011,UMGS2019,UMGS2053,UMGS2056,UMGS43,UMGS1059,UMGS1067,UMGS1127,UMGS2033,UMGS488,UMGS566,UMGS985,UMGS39,UMGS59,UMGS127,UMGS173,UMGS192,UMGS458,UMGS508,UMGS562,UMGS574,UMGS631,UMGS660,UMGS758,UMGS809,UMGS812,UMGS891,UMGS965,UMGS1096,UMGS1157,UMGS1258,UMGS1269,UMGS1437,UMGS1441,UMGS1462,UMGS1488,UMGS1529,UMGS1550,UMGS1637,UMGS1822,UMGS90,UMGS183,UMGS184,UMGS253,UMGS1404,UMGS1738,UMGS1756,UMGS2067,UMGS463,UMGS987,UMGS1857,UMGS504,UMGS564,UMGS1329,UMGS126,UMGS426,UMGS638,UMGS683,UMGS709,UMGS728,UMGS737,UMGS906,UMGS1091,UMGS1273,UMGS1308,UMGS1325,UMGS1448,UMGS1717,UMGS1987,UMGS744,UMGS151,UMGS248,UMGS271,UMGS1833,UMGS573,UMGS2025,UMGS78,UMGS89,UMGS1053,UMGS1759,UMGS199,UMGS38,UMGS136,UMGS185,UMGS186,UMGS197,UMGS340,UMGS456,UMGS526,UMGS1778,UMGS1846,UMGS1882,UMGS923,UMGS1355,UMGS1362,UMGS795,UMGS475,UMGS1403,UMGS225,UMGS1316,UMGS1322,UMGS1338,UMGS1535,UMGS1774,UMGS1812,UMGS2003,UMGS437,UMGS347,UMGS205,UMGS201,UMGS2076,UMGS1256,UMGS47,UMGS54,UMGS970,UMGS1895,UMGS144,UMGS1092,UMGS1560,UMGS15,UMGS269,UMGS270,UMGS1038,UMGS766,UMGS1500,UMGS1764,UMGS1959,UMGS760,UMGS255,UMGS411,UMGS470,UMGS706,UMGS717,UMGS733,UMGS791,UMGS983,UMGS1385,UMGS1431,UMGS1456,UMGS1554,UMGS1568,UMGS1712,UMGS2001,UMGS2024,UMGS121,UMGS369,UMGS663,UMGS1228,UMGS672,UMGS2035,UMGS776,UMGS1884,UMGS691,UMGS813,UMGS141,UMGS181,UMGS750,"

UMGS = "UMGS1825,UMGS2030,UMGS4,UMGS920,UMGS1687,UMGS158,UMGS1287,UMGS1406,UMGS17,UMGS52,UMGS79,UMGS80,UMGS82,UMGS88,UMGS101,UMGS138,UMGS152,UMGS169,UMGS229,UMGS438,UMGS453,UMGS578,UMGS600,UMGS681,UMGS725,UMGS786,UMGS803,UMGS849,UMGS866,UMGS944,UMGS960,UMGS1027,UMGS1238,UMGS1288,UMGS1314,UMGS1356,UMGS1423,UMGS1425,UMGS1438,UMGS1440,UMGS1476,UMGS1516,UMGS1531,UMGS1543,UMGS1553,UMGS1563,UMGS1570,UMGS1576,UMGS1594,UMGS1604,UMGS1609,UMGS1612,UMGS1630,UMGS1640,UMGS1642,UMGS1650,UMGS1652,UMGS1660,UMGS1663,UMGS1666,UMGS1672,UMGS1673,UMGS1677,UMGS1681,UMGS1689,UMGS1699,UMGS1711,UMGS1734,UMGS1740,UMGS1754,UMGS1781,UMGS1782,UMGS1788,UMGS1796,UMGS1843,UMGS1852,UMGS1864,UMGS1897,UMGS1901,UMGS1917,UMGS1925,UMGS1933,UMGS1968,UMGS1983,UMGS1988,UMGS1994,UMGS1995,UMGS2011,UMGS2019,UMGS2053,UMGS2056,UMGS43,UMGS1059,UMGS1067,UMGS1127,UMGS2033,UMGS488,UMGS566,UMGS985,UMGS39,UMGS59,UMGS127,UMGS173,UMGS192,UMGS458,UMGS508,UMGS562,UMGS574,UMGS631,UMGS660,UMGS758,UMGS809,UMGS812,UMGS891,UMGS965,UMGS1096,UMGS1157,UMGS1258,UMGS1269,UMGS1437,UMGS1441,UMGS1462,UMGS1488,UMGS1529,UMGS1550,UMGS1637,UMGS1822,UMGS90,UMGS183,UMGS184,UMGS253,UMGS1404,UMGS1738,UMGS1756,UMGS2067,UMGS463,UMGS987,UMGS1857,UMGS504,UMGS564,UMGS1329,UMGS126,UMGS426,UMGS638,UMGS683,UMGS709,UMGS728,UMGS737,UMGS906,UMGS1091,UMGS1273,UMGS1308,UMGS1325,UMGS1448,UMGS1717,UMGS1987,UMGS744,UMGS151,UMGS248,UMGS271,UMGS1833,UMGS573,UMGS2025,UMGS78,UMGS89,UMGS1053,UMGS1759,UMGS199,UMGS38,UMGS136,UMGS185,UMGS186,UMGS197,UMGS340,UMGS456,UMGS526,UMGS1778,UMGS1846,UMGS1882,UMGS923,UMGS1355,UMGS1362,UMGS795,UMGS475,UMGS1403,UMGS225,UMGS1316,UMGS1322,UMGS1338,UMGS1535,UMGS1774,UMGS1812,UMGS2003,UMGS437,UMGS347,UMGS205,UMGS201,UMGS2076,UMGS1256,UMGS47,UMGS54,UMGS970,UMGS1895,UMGS144,UMGS1092,UMGS1560,UMGS15,UMGS269,UMGS270,UMGS1038,UMGS766,UMGS1500,UMGS1764,UMGS1959,UMGS760,UMGS255,UMGS411,UMGS470,UMGS706,UMGS717,UMGS733,UMGS791,UMGS983,UMGS1385,UMGS1431,UMGS1456,UMGS1554,UMGS1568,UMGS1712,UMGS2001,UMGS2024,UMGS121,UMGS369,UMGS663,UMGS1228,UMGS672,UMGS2035,UMGS776,UMGS1884,UMGS691,UMGS813,UMGS141,UMGS181,UMGS750,"

UMGS = UMGS.replace(",", ".tsv ")
UMGS = UMGS.split()

separator = ""

###############################################################
# Number of proteins per UMGS
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

###############################################################
# Loading reference file from UniProt
file_in = open(filename_in_3, "r")

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

###############################################################

overall_lst = []
for i in range(len(UMGS)):
    overall_lst.append(" ")

###############################################################
for file_num in range(len(UMGS)):
    print("Working on ", UMGS[file_num][:-4], sep='', end='', flush=True)
    t0 = time.time()
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
        if num_proteins[i][0] == UMGS[file_num][4:-4]:
            popped = num_proteins.pop(i)
            half_p = math.floor(int(popped[1]) / 2)
            break

    #file_out.write("UMGS")
    file_out.write(UMGS[file_num][:-4])
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
    t1 = time.time()
    total_n = t1-t0
    print("Finished ", end='', flush=True)
    print(file_num + 1, "/", len(UMGS), sep='', end='', flush=True)
    print(" Time: ", total_n, sep='')

file_out.close()
