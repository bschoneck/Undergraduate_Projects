#!/usr/local/bin/python3
#compare.py

Output = open("CheckMvsTax.txt", "w")

Tax = open("Taxonomy.txt", "r")

lst1 = []
lst2 = []
count = 0
for line1 in Tax:
    line1.strip()
    lst1.append(line1)

Tax.close()

CheckM = open("CheckM_Out.txt", "r")
for line2 in CheckM:
    line1.strip()
    lst2.append(line2)

CheckM.close()

for line1 in lst1:
    correct = True
    #line1.strip()
    temp1 = line1.split()
    for i in range(len(temp1)):
        try:
            if temp1[i] == "Family":
                temp1[i-1] = "Clostridiales_Family_XI"
                temp1.remove("Family")
                temp1.remove("XI")
        except:
            pass
        """
        try:
            temp1.remove("NA")
        except:
            pass
        """
    #print(line1)

    for line2 in lst2:
        #line2.strip()
        temp2 = line2.split()

        if temp1[0] == temp2[0]:
            """
            if len(temp1) != len(temp2):
                for i in range((len(temp1)-len(temp2))):
                    temp2.append("NA")
            for i in range(2,len(temp1)):
                if temp2[i] == "Clostridiales_Family_XI._Incertae_Sedis":
                    temp2[i] = "Clostridiales_Family_XI"
                if temp2[i][len(temp2[i])-1] == '2':
                    temp2[i] = temp2[i].replace('2', '')
                    temp2[i] = temp2[i].replace('_', '')
                if temp2[i][len(temp2[i])-1] == '3':
                    temp2[i] = temp2[i].replace('3', '')
                    temp2[i] = temp2[i].replace('_', '')
            break
    Output.write(temp1[0])
    Output.write("\t")
    for i in range(2,len(temp1)):
        Output.write(temp1[i])
        Output.write("\t")
    Output.write("||\t")
    for i in range(2,len(temp2)):
        if temp2[i][len(temp2[i])-1] == '2':
            temp2[i] = temp2[i].replace('2', '')
            temp2[i] = temp2[i].replace('_', '')
        if temp2[i][len(temp2[i])-1] == '3':
            temp2[i] = temp2[i].replace('3', '')
            temp2[i] = temp2[i].replace('_', '')
        Output.write(temp2[i])
        if i != len(temp2)-1:
            Output.write("\t")
    Output.write("\n")
    """
            if len(temp1) != len(temp2):
                for i in range((len(temp1)-len(temp2))):
                    temp2.append("NA")
                correct = False
                break
            else:
                for i in range(2,len(temp1)):
                    if temp2[i] == "Clostridiales_Family_XI._Incertae_Sedis":
                        temp2[i] = "Clostridiales_Family_XI"
                    if temp2[i][len(temp2[i])-1] == '2':
                        temp2[i] = temp2[i].replace('2', '')
                        temp2[i] = temp2[i].replace('_', '')
                    if temp2[i][len(temp2[i])-1] == '3':
                        temp2[i] = temp2[i].replace('3', '')
                        temp2[i] = temp2[i].replace('_', '')
                    #if temp1[i] != temp2[i]:
                        #correct = False
                        #break
            break

    if correct == False:
        count+=1
        Output.write(temp1[0])
        Output.write("\t")
        for i in range(2,len(temp1)):
            Output.write(temp1[i])
            Output.write("\t")
        Output.write("||\t")
        for i in range(2,len(temp2)):
            if temp2[i][len(temp2[i])-1] == '2':
                temp2[i] = temp2[i].replace('2', '')
                temp2[i] = temp2[i].replace('_', '')
            if temp2[i][len(temp2[i])-1] == '3':
                temp2[i] = temp2[i].replace('3', '')
                temp2[i] = temp2[i].replace('_', '')
            Output.write(temp2[i])
            if i != len(temp2)-1:
                Output.write("\t")
        Output.write("\n")

print(count)
Output.close()
