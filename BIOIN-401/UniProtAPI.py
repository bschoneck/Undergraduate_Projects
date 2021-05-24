import urllib.parse
import urllib.request
import time

url = 'https://www.uniprot.org/uniprot/'

filename_in = ["toUniProt/UMGS", " ", ".txt"]

filename_out = ["fromUniProt/UMGS", " ", ".txt"]

UMGS = ['1038', '1059', '1073', '1092', '118', '1189', '121', '1233', '1256', '126', '1268', '1287', '1316', '1322', '1329', '1338', '1355', '136', '1403', '141', '1414', '144', '15', '1500', '151', '1535', '1552', '158', '17', '170', '1745', '175', '1753', '1764', '177', '1774', '181', '1812', '1817', '183', '1857', '1884', '1894', '1912', '1926', '1956', '1959', '199', '2003', '201', '2025', '2035', '205', '2076', '2079', '208', '220', '225', '227', '248', '255', '26', '269', '282', '29', '304', '328', '33', '347', '351', '369', '38', '380', '39', '4', '41', '410', '411', '422', '426', '43', '437', '463', '47', '475', '479', '480', '488', '504', '52', '54', '561', '564', '566', '572', '573', '59', '6', '63', '65', '672', '676', '682', '691', '74', '744', '760', '766', '774', '776', '78', '795', '813', '816', '89', '90', '908', '920', '923', '93', '935', '94', '971', '987']

UMGS = ['987']

separator1 = ""
separator2 = " OR "

for i in range(len(UMGS)):
    print("Starting UMGS", UMGS[i])
    start = time.time()
    query_id = []
    query_id_lst = []

    filename_in_temp = filename_in
    filename_in_temp[1] = UMGS[i]
    filename_in_temp = separator1.join(filename_in_temp)

    file_in = open(filename_in_temp, "r")

    filename_out_temp = filename_out
    filename_out_temp[1] = UMGS[i]
    filename_out_temp = separator1.join(filename_out_temp)

    file_out = open(filename_out_temp, "w")

    for line in file_in:
        line.strip()
        line = line.replace('\n', '')
        query_id.append(line)

        if len(query_id) >= 500:
            query_id_lst.append(query_id)
            query_id = []

    query_id_lst.append(query_id)
    query_id = []

    for i in range(len(query_id_lst)):
        start2 = time.time()
        query_id_str = separator2.join(query_id_lst[i])

        params = {
        'from': 'ACC+ID',
        'to': 'ID',
        'format': 'tab',
        'query': query_id_str,
        'columns': 'id,lineage(PHYLUM),lineage(CLASS),lineage(ORDER),lineage(FAMILY),lineage(GENUS)'
        }

        data = urllib.parse.urlencode(params)
        data = data.encode('utf-8')
        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as f:
            temp = f.readline()
            #response = f.readline()
            response = f.read()
        print(response.decode('utf-8'))
        file_out.write(response.decode('utf-8'))
        file_out.write("\n")
        end2 = time.time()
        print("Time elapsed: ", end2-start2)

        end = time.time()
        print("Finished UMGS", UMGS[i])
        print("Time elapsed: ", end-start)
        file_in.close()
        file_out.close()
"""
url = 'https://www.uniprot.org/uploadlists/'

params = {
'from': 'ACC+ID',
'to': 'ENSEMBL_ID',
'format': 'tab',
'query': 'P40925 P40926 O43175 Q9UM73 P97793'
}

data = urllib.parse.urlencode(params)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as f:
   response = f.read()
print(response.decode('utf-8'))
"""
