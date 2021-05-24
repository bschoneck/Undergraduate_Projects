import os


#names = ['UMGS179', 'UMGS183', 'UMGS84', 'UMGS264', 'UMGS470', 'UMGS2067', 'UMGS90', 'UMGS86', 'UMGS125', 'UMGS463', 'UMGS39', 'UMGS759', 'UMGS1710', 'UMGS365', 'UMGS132', 'UMGS184', 'UMGS537', 'UMGS137', 'UMGS762', 'UMGS160']

names = ['UMGS1']

names = "UMGS1,UMGS2,UMGS3,UMGS4,UMGS6,UMGS7,UMGS8,UMGS9,UMGS11,UMGS12,UMGS13,UMGS14,UMGS15,UMGS16,UMGS17,UMGS18,UMGS20,UMGS21,UMGS22,UMGS24,UMGS26,UMGS27,UMGS29,UMGS30,UMGS31,UMGS32,UMGS33,UMGS34,UMGS35,UMGS36,UMGS37,UMGS38,UMGS39,UMGS40,UMGS41,UMGS42,UMGS43,UMGS44,UMGS45,UMGS46,UMGS47,UMGS48,UMGS49,UMGS50,UMGS51,UMGS52,UMGS53,UMGS54,UMGS55,UMGS56,UMGS57,UMGS59,UMGS61,UMGS62,UMGS63,UMGS64,UMGS65,UMGS66,UMGS68,UMGS69,UMGS70,UMGS71,UMGS73,UMGS74,UMGS75,UMGS77,UMGS78,UMGS79,UMGS80,UMGS81,UMGS82,UMGS83,UMGS84,UMGS85,UMGS86,UMGS87,UMGS88,UMGS89,UMGS90,UMGS91,UMGS92,UMGS93,UMGS94,UMGS95,UMGS96,UMGS97,UMGS98,UMGS99,UMGS100,UMGS101,UMGS104,UMGS106,UMGS107,UMGS108,UMGS109,UMGS110,UMGS111,UMGS112,UMGS113,UMGS115,UMGS116,UMGS117,UMGS118,UMGS119,UMGS120,UMGS121,UMGS122,UMGS124,UMGS125,UMGS126,UMGS127,UMGS128,UMGS129,UMGS130,UMGS131,UMGS132,UMGS133,UMGS134,UMGS135,UMGS136,UMGS137,UMGS138,UMGS141,UMGS142,UMGS143,UMGS144,UMGS145,UMGS146,UMGS147,UMGS148,UMGS149,UMGS151,UMGS152,UMGS153,UMGS154,UMGS155,UMGS156,UMGS157,UMGS158,UMGS159,UMGS160,UMGS161,UMGS162,UMGS163,UMGS164,UMGS165,UMGS166,UMGS167,UMGS168,UMGS169,UMGS170,UMGS171,UMGS172,UMGS173,UMGS174,UMGS175,UMGS176,UMGS177,UMGS178,UMGS179,UMGS181,UMGS182,UMGS183,UMGS184,UMGS185,UMGS186,UMGS187,UMGS188,UMGS190,UMGS192,UMGS193,UMGS194,UMGS196,UMGS197,UMGS198,UMGS199,UMGS200,UMGS201,UMGS203,UMGS204,UMGS205,UMGS206,UMGS207,UMGS208,UMGS209,UMGS211,UMGS212,UMGS213,UMGS214,UMGS215,UMGS216,UMGS218,UMGS219,UMGS220,UMGS221,UMGS222,UMGS223,UMGS225,UMGS227,UMGS228,UMGS229,UMGS230,UMGS231,UMGS232,UMGS233,UMGS234,UMGS235,UMGS236,UMGS237,UMGS238,UMGS239,UMGS240,UMGS241,UMGS242,UMGS243,UMGS244,UMGS245,UMGS247,UMGS248,UMGS249,UMGS250,UMGS251,UMGS252,UMGS253,UMGS254,UMGS255,UMGS256,UMGS257,UMGS258,UMGS259,UMGS260,UMGS261,UMGS262,UMGS263,UMGS264,UMGS268,UMGS269,UMGS270,UMGS271,UMGS272,UMGS273,UMGS274,UMGS275,UMGS276,UMGS277,UMGS278,UMGS279,UMGS280,UMGS281,UMGS282,UMGS283,UMGS284,UMGS285,UMGS286,UMGS287,UMGS288,UMGS289,UMGS290,UMGS291,UMGS292,UMGS293,UMGS294,UMGS295,UMGS296,UMGS297,UMGS298,UMGS299,UMGS300,UMGS301,UMGS302,UMGS303,UMGS304,UMGS305,UMGS306,UMGS307,UMGS308,UMGS309,UMGS310,UMGS311,UMGS312,UMGS313,UMGS314,UMGS315,UMGS316,UMGS317,UMGS318,UMGS319,UMGS320,UMGS321,UMGS322,UMGS323,UMGS324,UMGS325,UMGS326,UMGS327,UMGS328,UMGS329,UMGS331,UMGS332,UMGS333,UMGS334,UMGS335,UMGS337,UMGS338,UMGS339,UMGS340,UMGS341,UMGS342,UMGS343,UMGS344,UMGS346,UMGS347,UMGS349,UMGS351,UMGS352,UMGS353,UMGS354,UMGS355,UMGS356,UMGS357,UMGS358,UMGS359,UMGS360,UMGS361,UMGS362,UMGS363,UMGS364,UMGS365,UMGS366,UMGS367,UMGS368,UMGS369,UMGS370,UMGS372,UMGS373,UMGS375,UMGS376,UMGS377,UMGS378,UMGS379,UMGS380,UMGS381,UMGS382,UMGS383,UMGS384,UMGS385,UMGS386,UMGS387,UMGS388,UMGS389,UMGS390,UMGS391,UMGS393,UMGS394,UMGS395,UMGS396,UMGS397,UMGS398,UMGS399,UMGS400,UMGS401,UMGS402,UMGS403,UMGS404,UMGS406,UMGS407,UMGS408,UMGS409,UMGS410,UMGS411,UMGS412,UMGS413,UMGS414,UMGS415,UMGS416,UMGS417,UMGS418,UMGS419,UMGS420,UMGS421,UMGS422,UMGS423,UMGS424,UMGS425,UMGS426,UMGS427,UMGS428,UMGS429,UMGS430,UMGS431,UMGS432,UMGS433,UMGS434,UMGS437,UMGS438,UMGS439,UMGS440,UMGS441,UMGS442,UMGS443,UMGS445,UMGS446,UMGS447,UMGS448,UMGS449,UMGS450,UMGS451,UMGS452,UMGS453,UMGS454,UMGS455,UMGS456,UMGS457,UMGS458,UMGS459,UMGS460,UMGS461,UMGS462,UMGS463,UMGS464,UMGS465,UMGS466,UMGS467,UMGS468,UMGS469,UMGS470,UMGS471,UMGS472,UMGS473,UMGS474,UMGS475,UMGS476,UMGS477,UMGS478,UMGS479,UMGS480,UMGS481,UMGS482,UMGS483,UMGS484,UMGS485,UMGS486,UMGS487,UMGS488,UMGS489,UMGS490,UMGS491,UMGS492,UMGS493,UMGS494,UMGS495,UMGS496,UMGS498,UMGS499,UMGS500,UMGS501,UMGS502,UMGS503,UMGS504,UMGS505,UMGS506,UMGS508,UMGS509,UMGS510,UMGS511,UMGS512,UMGS513,UMGS514,UMGS515,UMGS516,UMGS517,UMGS518,UMGS519,UMGS520,UMGS522,UMGS523,UMGS524,UMGS525,UMGS526,UMGS528,UMGS529,UMGS530,UMGS531,UMGS532,UMGS533,UMGS534,UMGS535,UMGS536,UMGS537,UMGS538,UMGS539,UMGS540,UMGS541,UMGS542,UMGS543,UMGS544,UMGS545,UMGS547,UMGS548,UMGS549,UMGS551,UMGS552,UMGS553,UMGS555,UMGS556,UMGS558,UMGS559,UMGS560,UMGS561,UMGS562,UMGS564,UMGS565,UMGS566,UMGS567,UMGS568,UMGS569,UMGS570,UMGS571,UMGS572,UMGS573,UMGS574,UMGS576,UMGS577,UMGS578,UMGS579,UMGS580,UMGS581,UMGS582,UMGS583,UMGS584,UMGS585,UMGS586,UMGS587,UMGS588,UMGS589,UMGS590,UMGS592,UMGS593,UMGS594,UMGS595,UMGS596,UMGS597,UMGS598,UMGS599,UMGS600,UMGS601,UMGS602,UMGS603,UMGS604,UMGS605,UMGS606,UMGS607,UMGS608,UMGS609,UMGS610,UMGS611,UMGS613,UMGS615,UMGS616,UMGS617,UMGS618,UMGS619,UMGS620,UMGS621,UMGS622,UMGS623,UMGS624,UMGS625,UMGS626,UMGS627,UMGS628,UMGS629,UMGS630,UMGS631,UMGS632,UMGS633,UMGS634,UMGS635,UMGS636,UMGS637,UMGS638,UMGS639,UMGS640,UMGS641,UMGS642,UMGS643,UMGS644,UMGS645,UMGS646,UMGS647,UMGS648,UMGS649,UMGS650,UMGS651,UMGS652,UMGS653,UMGS654,UMGS655,UMGS656,UMGS657,UMGS658,UMGS659,UMGS660,UMGS661,UMGS662,UMGS663,UMGS664,UMGS665,UMGS666,UMGS667,UMGS668,UMGS669,UMGS670,UMGS671,UMGS672,UMGS673,UMGS674,UMGS675,UMGS676,UMGS677,UMGS678,UMGS679,UMGS680,UMGS681,UMGS682,UMGS683,UMGS684,UMGS685,UMGS686,UMGS687,UMGS688,UMGS689,UMGS690,UMGS691,UMGS692,UMGS693,UMGS695,UMGS696,UMGS697,UMGS698,UMGS699,UMGS700,UMGS701,UMGS702,UMGS704,UMGS705,UMGS706,UMGS707,UMGS708,UMGS709,UMGS710,UMGS711,UMGS712,UMGS713,UMGS714,UMGS715,UMGS716,UMGS717,UMGS718,UMGS719,UMGS720,UMGS721,UMGS722,UMGS723,UMGS724,UMGS725,UMGS726,UMGS727,UMGS728,UMGS729,UMGS730,UMGS731,UMGS732,UMGS733,UMGS734,UMGS735,UMGS736,UMGS737,UMGS738,UMGS739,UMGS740,UMGS741,UMGS742,UMGS743,UMGS744,UMGS745,UMGS746,UMGS748,UMGS749,UMGS750,UMGS751,UMGS752,UMGS753,UMGS754,UMGS755,UMGS757,UMGS758,UMGS759,UMGS760,UMGS761,UMGS762,UMGS763,UMGS764,UMGS765,UMGS766,UMGS767,UMGS768,UMGS769,UMGS770,UMGS771,UMGS772,UMGS773,UMGS774,UMGS775,UMGS776,UMGS777,UMGS779,UMGS780,UMGS781,UMGS782,UMGS783,UMGS784,UMGS785,UMGS786,UMGS787,UMGS788,UMGS789,UMGS790,UMGS791,UMGS792,UMGS793,UMGS794,UMGS795,UMGS796,UMGS797,UMGS798,UMGS799,UMGS800,UMGS801,UMGS802,UMGS803,UMGS804,UMGS805,UMGS806,UMGS807,UMGS808,UMGS809,UMGS810,UMGS811,UMGS812,UMGS813,UMGS814,UMGS815,UMGS816,UMGS817,UMGS818,UMGS819,UMGS820,UMGS821,UMGS822,UMGS823,UMGS824,UMGS825,UMGS826,UMGS827,UMGS828,UMGS830,UMGS832,UMGS833,UMGS834,UMGS835,UMGS836,UMGS837,UMGS838,UMGS839,UMGS840,UMGS841,UMGS842,UMGS843,UMGS844,UMGS845,UMGS846,UMGS847,UMGS848,UMGS849,UMGS850,UMGS851,UMGS852,UMGS853,UMGS854,UMGS855,UMGS856,UMGS857,UMGS858,UMGS859,UMGS860,UMGS861,UMGS863,UMGS864,UMGS865,UMGS866,UMGS867,UMGS868,UMGS869,UMGS870,UMGS871,UMGS872,UMGS873,UMGS874,UMGS875,UMGS876,UMGS877,UMGS878,UMGS879,UMGS880,UMGS881,UMGS882,UMGS883,UMGS884,UMGS885,UMGS886,UMGS887,UMGS888,UMGS889,UMGS890,UMGS891,UMGS892,UMGS893,UMGS894,UMGS895,UMGS896,UMGS897,UMGS898,UMGS899,UMGS900,UMGS901,UMGS902,UMGS903,UMGS904,UMGS905,UMGS906,UMGS907,UMGS908,UMGS909,UMGS910,UMGS911,UMGS912,UMGS913,UMGS914,UMGS915,UMGS916,UMGS917,UMGS918,UMGS919,UMGS920,UMGS921,UMGS922,UMGS923,UMGS925,UMGS926,UMGS927,UMGS928,UMGS929,UMGS930,UMGS931,UMGS932,UMGS933,UMGS934,UMGS935,UMGS937,UMGS938,UMGS939,UMGS940,UMGS941,UMGS942,UMGS943,UMGS944,UMGS945,UMGS946,UMGS947,UMGS948,UMGS949,UMGS950,UMGS951,UMGS953,UMGS954,UMGS955,UMGS956,UMGS957,UMGS958,UMGS959,UMGS960,UMGS961,UMGS962,UMGS963,UMGS964,UMGS965,UMGS966,UMGS967,UMGS968,UMGS969,UMGS970,UMGS971,UMGS972,UMGS973,UMGS974,UMGS975,UMGS976,UMGS977,UMGS978,UMGS979,UMGS980,UMGS981,UMGS982,UMGS983,UMGS984,UMGS985,UMGS986,UMGS987,UMGS988,UMGS989,UMGS990,UMGS991,UMGS992,UMGS993,UMGS994,UMGS995,UMGS996,UMGS997,UMGS998,UMGS999,UMGS1001,UMGS1002,UMGS1003,UMGS1004,UMGS1005,UMGS1006,UMGS1007,UMGS1008,UMGS1009,UMGS1010,UMGS1011,UMGS1012,UMGS1013,UMGS1014,UMGS1015,UMGS1016,UMGS1017,UMGS1018,UMGS1019,UMGS1020,UMGS1021,UMGS1022,UMGS1023,UMGS1024,UMGS1025,UMGS1026,UMGS1027,UMGS1028,UMGS1029,UMGS1030,UMGS1031,UMGS1032,UMGS1033,UMGS1034,UMGS1035,UMGS1036,UMGS1037,UMGS1038,UMGS1039,UMGS1040,UMGS1041,UMGS1042,UMGS1043,UMGS1044,UMGS1045,UMGS1046,UMGS1047,UMGS1048,UMGS1049,UMGS1050,UMGS1051,UMGS1052,UMGS1053,UMGS1054,UMGS1055,UMGS1056,UMGS1057,UMGS1058,UMGS1059,UMGS1060,UMGS1061,UMGS1062,UMGS1063,UMGS1064,UMGS1065,UMGS1066,UMGS1067,UMGS1068,UMGS1069,UMGS1070,UMGS1071,UMGS1072,UMGS1073,UMGS1074,UMGS1075,UMGS1077,UMGS1078,UMGS1079,UMGS1080,UMGS1081,UMGS1082,UMGS1083,UMGS1084,UMGS1085,UMGS1086,UMGS1087,UMGS1088,UMGS1089,UMGS1091,UMGS1092,UMGS1093,UMGS1094,UMGS1095,UMGS1096,UMGS1097,UMGS1098,UMGS1099,UMGS1100,UMGS1101,UMGS1102,UMGS1103,UMGS1104,UMGS1105,UMGS1106,UMGS1107,UMGS1108,UMGS1109,UMGS1110,UMGS1111,UMGS1112,UMGS1113,UMGS1114,UMGS1115,UMGS1116,UMGS1117,UMGS1118,UMGS1119,UMGS1120,UMGS1121,UMGS1122,UMGS1123,UMGS1124,UMGS1125,UMGS1126,UMGS1127,UMGS1128,UMGS1129,UMGS1130,UMGS1131,UMGS1132,UMGS1133,UMGS1134,UMGS1135,UMGS1136,UMGS1137,UMGS1138,UMGS1139,UMGS1140,UMGS1141,UMGS1142,UMGS1143,UMGS1144,UMGS1145,UMGS1146,UMGS1147,UMGS1148,UMGS1149,UMGS1151,UMGS1152,UMGS1153,UMGS1154,UMGS1155,UMGS1156,UMGS1157,UMGS1158,UMGS1159,UMGS1160,UMGS1161,UMGS1162,UMGS1163,UMGS1164,UMGS1165,UMGS1166,UMGS1167,UMGS1168,UMGS1169,UMGS1170,UMGS1171,UMGS1172,UMGS1173,UMGS1174,UMGS1175,UMGS1177,UMGS1178,UMGS1179,UMGS1180,UMGS1181,UMGS1182,UMGS1183,UMGS1184,UMGS1185,UMGS1186,UMGS1187,UMGS1188,UMGS1189,UMGS1190,UMGS1191,UMGS1192,UMGS1193,UMGS1195,UMGS1196,UMGS1197,UMGS1198,UMGS1199,UMGS1200,UMGS1201,UMGS1202,UMGS1203,UMGS1204,UMGS1205,UMGS1206,UMGS1207,UMGS1208,UMGS1209,UMGS1210,UMGS1211,UMGS1212,UMGS1213,UMGS1214,UMGS1215,UMGS1216,UMGS1217,UMGS1219,UMGS1220,UMGS1221,UMGS1222,UMGS1224,UMGS1225,UMGS1226,UMGS1227,UMGS1228,UMGS1229,UMGS1230,UMGS1231,UMGS1232,UMGS1233,UMGS1234,UMGS1235,UMGS1236,UMGS1237,UMGS1238,UMGS1239,UMGS1241,UMGS1242,UMGS1243,UMGS1244,UMGS1245,UMGS1246,UMGS1247,UMGS1248,UMGS1249,UMGS1250,UMGS1251,UMGS1252,UMGS1253,UMGS1254,UMGS1255,UMGS1256,UMGS1257,UMGS1258,UMGS1259,UMGS1260,UMGS1262,UMGS1263,UMGS1264,UMGS1265,UMGS1266,UMGS1267,UMGS1268,UMGS1269,UMGS1270,UMGS1271,UMGS1272,UMGS1273,UMGS1274,UMGS1275,UMGS1276,UMGS1277,UMGS1278,UMGS1279,UMGS1280,UMGS1281,UMGS1282,UMGS1284,UMGS1285,UMGS1286,UMGS1287,UMGS1288,UMGS1289,UMGS1290,UMGS1291,UMGS1292,UMGS1293,UMGS1294,UMGS1295,UMGS1296,UMGS1297,UMGS1298,UMGS1300,UMGS1301,UMGS1302,UMGS1303,UMGS1304,UMGS1305,UMGS1306,UMGS1307,UMGS1308,UMGS1309,UMGS1310,UMGS1311,UMGS1312,UMGS1313,UMGS1314,UMGS1315,UMGS1316,UMGS1317,UMGS1318,UMGS1319,UMGS1320,UMGS1321,UMGS1322,UMGS1323,UMGS1324,UMGS1325,UMGS1326,UMGS1327,UMGS1328,UMGS1329,UMGS1330,UMGS1331,UMGS1332,UMGS1333,UMGS1335,UMGS1336,UMGS1337,UMGS1338,UMGS1339,UMGS1340,UMGS1341,UMGS1342,UMGS1344,UMGS1345,UMGS1346,UMGS1347,UMGS1348,UMGS1349,UMGS1350,UMGS1351,UMGS1352,UMGS1353,UMGS1354,UMGS1355,UMGS1356,UMGS1357,UMGS1358,UMGS1359,UMGS1360,UMGS1362,UMGS1364,UMGS1365,UMGS1366,UMGS1367,UMGS1368,UMGS1369,UMGS1370,UMGS1371,UMGS1372,UMGS1373,UMGS1374,UMGS1375,UMGS1376,UMGS1377,UMGS1378,UMGS1379,UMGS1380,UMGS1381,UMGS1382,UMGS1383,UMGS1384,UMGS1385,UMGS1386,UMGS1387,UMGS1388,UMGS1389,UMGS1390,UMGS1391,UMGS1392,UMGS1394,UMGS1395,UMGS1396,UMGS1397,UMGS1399,UMGS1400,UMGS1401,UMGS1402,UMGS1403,UMGS1404,UMGS1405,UMGS1406,UMGS1407,UMGS1408,UMGS1409,UMGS1410,UMGS1411,UMGS1413,UMGS1414,UMGS1415,UMGS1416,UMGS1417,UMGS1418,UMGS1419,UMGS1420,UMGS1421,UMGS1423,UMGS1424,UMGS1425,UMGS1426,UMGS1427,UMGS1428,UMGS1429,UMGS1430,UMGS1431,UMGS1432,UMGS1433,UMGS1434,UMGS1435,UMGS1436,UMGS1437,UMGS1438,UMGS1439,UMGS1440,UMGS1441,UMGS1442,UMGS1443,UMGS1444,UMGS1445,UMGS1446,UMGS1447,UMGS1448,UMGS1449,UMGS1450,UMGS1451,UMGS1452,UMGS1453,UMGS1454,UMGS1455,UMGS1456,UMGS1457,UMGS1458,UMGS1459,UMGS1461,UMGS1462,UMGS1463,UMGS1464,UMGS1465,UMGS1466,UMGS1467,UMGS1468,UMGS1469,UMGS1470,UMGS1471,UMGS1472,UMGS1473,UMGS1474,UMGS1475,UMGS1476,UMGS1477,UMGS1478,UMGS1479,UMGS1480,UMGS1481,UMGS1482,UMGS1483,UMGS1484,UMGS1485,UMGS1487,UMGS1488,UMGS1489,UMGS1490,UMGS1491,UMGS1492,UMGS1493,UMGS1494,UMGS1495,UMGS1496,UMGS1497,UMGS1498,UMGS1499,UMGS1500,UMGS1501,UMGS1502,UMGS1504,UMGS1505,UMGS1506,UMGS1508,UMGS1510,UMGS1511,UMGS1512,UMGS1513,UMGS1514,UMGS1515,UMGS1516,UMGS1517,UMGS1518,UMGS1519,UMGS1520,UMGS1521,UMGS1522,UMGS1523,UMGS1524,UMGS1525,UMGS1526,UMGS1527,UMGS1529,UMGS1530,UMGS1531,UMGS1532,UMGS1533,UMGS1534,UMGS1535,UMGS1537,UMGS1538,UMGS1539,UMGS1540,UMGS1541,UMGS1542,UMGS1543,UMGS1545,UMGS1546,UMGS1547,UMGS1548,UMGS1549,UMGS1550,UMGS1551,UMGS1552,UMGS1553,UMGS1554,UMGS1555,UMGS1556,UMGS1557,UMGS1558,UMGS1559,UMGS1560,UMGS1561,UMGS1562,UMGS1563,UMGS1564,UMGS1565,UMGS1566,UMGS1567,UMGS1568,UMGS1569,UMGS1570,UMGS1571,UMGS1572,UMGS1573,UMGS1574,UMGS1575,UMGS1576,UMGS1577,UMGS1578,UMGS1579,UMGS1580,UMGS1581,UMGS1582,UMGS1583,UMGS1584,UMGS1585,UMGS1586,UMGS1587,UMGS1589,UMGS1590,UMGS1591,UMGS1594,UMGS1595,UMGS1596,UMGS1597,UMGS1598,UMGS1600,UMGS1601,UMGS1602,UMGS1603,UMGS1604,UMGS1605,UMGS1606,UMGS1607,UMGS1608,UMGS1609,UMGS1610,UMGS1611,UMGS1612,UMGS1613,UMGS1614,UMGS1615,UMGS1616,UMGS1617,UMGS1618,UMGS1619,UMGS1620,UMGS1621,UMGS1622,UMGS1623,UMGS1624,UMGS1625,UMGS1626,UMGS1627,UMGS1628,UMGS1629,UMGS1630,UMGS1631,UMGS1632,UMGS1633,UMGS1634,UMGS1635,UMGS1636,UMGS1637,UMGS1638,UMGS1639,UMGS1640,UMGS1641,UMGS1642,UMGS1643,UMGS1644,UMGS1645,UMGS1646,UMGS1647,UMGS1648,UMGS1649,UMGS1650,UMGS1651,UMGS1652,UMGS1653,UMGS1654,UMGS1656,UMGS1657,UMGS1658,UMGS1659,UMGS1660,UMGS1661,UMGS1662,UMGS1663,UMGS1664,UMGS1665,UMGS1666,UMGS1667,UMGS1668,UMGS1669,UMGS1670,UMGS1671,UMGS1672,UMGS1673,UMGS1674,UMGS1675,UMGS1676,UMGS1677,UMGS1678,UMGS1680,UMGS1681,UMGS1682,UMGS1683,UMGS1684,UMGS1685,UMGS1686,UMGS1687,UMGS1688,UMGS1689,UMGS1690,UMGS1691,UMGS1692,UMGS1693,UMGS1694,UMGS1695,UMGS1696,UMGS1697,UMGS1698,UMGS1699,UMGS1700,UMGS1701,UMGS1702,UMGS1703,UMGS1704,UMGS1705,UMGS1706,UMGS1707,UMGS1708,UMGS1709,UMGS1710,UMGS1711,UMGS1712,UMGS1713,UMGS1714,UMGS1715,UMGS1716,UMGS1717,UMGS1718,UMGS1719,UMGS1720,UMGS1721,UMGS1722,UMGS1724,UMGS1725,UMGS1726,UMGS1727,UMGS1728,UMGS1729,UMGS1730,UMGS1731,UMGS1732,UMGS1733,UMGS1734,UMGS1735,UMGS1737,UMGS1738,UMGS1739,UMGS1740,UMGS1741,UMGS1742,UMGS1743,UMGS1744,UMGS1745,UMGS1746,UMGS1747,UMGS1748,UMGS1749,UMGS1750,UMGS1751,UMGS1752,UMGS1753,UMGS1754,UMGS1755,UMGS1756,UMGS1757,UMGS1758,UMGS1759,UMGS1760,UMGS1761,UMGS1762,UMGS1763,UMGS1764,UMGS1765,UMGS1766,UMGS1767,UMGS1768,UMGS1769,UMGS1771,UMGS1772,UMGS1773,UMGS1774,UMGS1775,UMGS1776,UMGS1777,UMGS1778,UMGS1779,UMGS1780,UMGS1781,UMGS1782,UMGS1783,UMGS1784,UMGS1785,UMGS1786,UMGS1787,UMGS1788,UMGS1789,UMGS1790,UMGS1791,UMGS1793,UMGS1794,UMGS1795,UMGS1796,UMGS1797,UMGS1798,UMGS1799,UMGS1800,UMGS1801,UMGS1802,UMGS1805,UMGS1806,UMGS1807,UMGS1808,UMGS1809,UMGS1810,UMGS1811,UMGS1812,UMGS1813,UMGS1815,UMGS1816,UMGS1817,UMGS1818,UMGS1819,UMGS1820,UMGS1821,UMGS1822,UMGS1823,UMGS1824,UMGS1825,UMGS1826,UMGS1828,UMGS1829,UMGS1831,UMGS1832,UMGS1833,UMGS1834,UMGS1835,UMGS1836,UMGS1837,UMGS1838,UMGS1839,UMGS1840,UMGS1841,UMGS1842,UMGS1843,UMGS1844,UMGS1845,UMGS1846,UMGS1847,UMGS1848,UMGS1850,UMGS1851,UMGS1852,UMGS1853,UMGS1855,UMGS1857,UMGS1858,UMGS1859,UMGS1860,UMGS1861,UMGS1862,UMGS1863,UMGS1864,UMGS1865,UMGS1867,UMGS1868,UMGS1869,UMGS1870,UMGS1871,UMGS1872,UMGS1873,UMGS1874,UMGS1875,UMGS1877,UMGS1878,UMGS1879,UMGS1880,UMGS1881,UMGS1882,UMGS1883,UMGS1884,UMGS1886,UMGS1887,UMGS1889,UMGS1890,UMGS1891,UMGS1892,UMGS1893,UMGS1894,UMGS1895,UMGS1896,UMGS1897,UMGS1898,UMGS1899,UMGS1900,UMGS1901,UMGS1902,UMGS1903,UMGS1904,UMGS1905,UMGS1906,UMGS1907,UMGS1908,UMGS1909,UMGS1910,UMGS1911,UMGS1912,UMGS1913,UMGS1914,UMGS1915,UMGS1916,UMGS1917,UMGS1918,UMGS1919,UMGS1920,UMGS1921,UMGS1922,UMGS1923,UMGS1924,UMGS1925,UMGS1926,UMGS1927,UMGS1928,UMGS1929,UMGS1930,UMGS1931,UMGS1932,UMGS1933,UMGS1934,UMGS1935,UMGS1936,UMGS1937,UMGS1938,UMGS1939,UMGS1940,UMGS1941,UMGS1942,UMGS1943,UMGS1944,UMGS1945,UMGS1946,UMGS1948,UMGS1949,UMGS1950,UMGS1951,UMGS1952,UMGS1953,UMGS1954,UMGS1955,UMGS1956,UMGS1958,UMGS1959,UMGS1960,UMGS1962,UMGS1963,UMGS1964,UMGS1965,UMGS1966,UMGS1967,UMGS1968,UMGS1969,UMGS1970,UMGS1971,UMGS1972,UMGS1973,UMGS1974,UMGS1975,UMGS1976,UMGS1977,UMGS1979,UMGS1980,UMGS1981,UMGS1982,UMGS1983,UMGS1984,UMGS1985,UMGS1986,UMGS1987,UMGS1988,UMGS1989,UMGS1990,UMGS1991,UMGS1992,UMGS1993,UMGS1994,UMGS1995,UMGS1996,UMGS1999,UMGS2000,UMGS2001,UMGS2002,UMGS2003,UMGS2004,UMGS2005,UMGS2006,UMGS2007,UMGS2008,UMGS2009,UMGS2010,UMGS2011,UMGS2012,UMGS2013,UMGS2014,UMGS2016,UMGS2017,UMGS2018,UMGS2019,UMGS2020,UMGS2021,UMGS2022,UMGS2023,UMGS2024,UMGS2025,UMGS2026,UMGS2027,UMGS2028,UMGS2029,UMGS2030,UMGS2031,UMGS2032,UMGS2033,UMGS2034,UMGS2035,UMGS2036,UMGS2037,UMGS2038,UMGS2039,UMGS2040,UMGS2041,UMGS2042,UMGS2043,UMGS2044,UMGS2045,UMGS2047,UMGS2048,UMGS2049,UMGS2050,UMGS2051,UMGS2052,UMGS2053,UMGS2054,UMGS2055,UMGS2056,UMGS2057,UMGS2058,UMGS2059,UMGS2060,UMGS2061,UMGS2062,UMGS2063,UMGS2064,UMGS2065,UMGS2066,UMGS2067,UMGS2068,UMGS2069,UMGS2070,UMGS2071,UMGS2072,UMGS2073,UMGS2074,UMGS2075,UMGS2076,UMGS2078,UMGS2079"

names = names.split(",")

separator = ''

for i in names:
    lst1 = ["python MGS-gut/scripts/rename_multifasta_prefix.py -f genomes/", " ", ".fa -p ", " ", " > ", " ", "r.fa"]
    lst1[1] = i
    lst1[3] = i
    lst1[5] = i
    os.system(separator.join(lst1))
    lst2 = ["mv ", " ", "r.fa Renamed_genomes_test"]
    lst2[1] = i
    os.system(separator.join(lst2))