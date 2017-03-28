import re

string =  str(input())
stringList = string.split('|')

def removeCases(string):
    string = string.lower()
    string = re.sub( '\s+', ' ', string ).strip()
    string = string.replace("\"","")
    string = string.replace(",",".")
    string = re.sub('-+','-',string)

    return string

def compare():

    for i in stringList:  
        for j in stringList:
            if i != j:
                if comparison(i, j):
                    if len(i) < len(j):
                        ss = j.split()
                        nn = i.split()
                        if set(nn) in set(ss):
                            stringList.pop(stringList.index(i))
                    if len(i) >= len(j):
                        stringList.pop(stringList.index(j))
    if stringList[0] == stringList[1]:
        stringList.pop(1)
    
    printstr = ''
    for i in stringList:
        if printstr == '':
            printstr += str(i)
        else:
            printstr = printstr + '|' + str(i)
    return printstr

def compareFunction(dList):
    dummyList = dList
    indexList = []
    for i in dummyList:
        for j in dummyList:
            if i != j:
                if comparison(i, j):
                    if len(i) <= len(j):
                        stringSplit_1 = i.split()
                        stringSplit_2 = j.split()
                        if set(stringSplit_1) == set(stringSplit_2):
                            dummyList.pop(dummyList.index(j))
                        if set(stringSplit_1) in set(stringSplit_2):
                            dummyList.pop(dummyList.index(i))
            print(dummyList)
    if dummyList[0] == dummyList[1]:
        dummyList.pop(1)
    return dummyList
                            
def comparison(string1, string2):
    if len(string1) <= len(string2):
        smallerString = string1
        largerString = string2
    else:
        smallerString = string2
        largerString = string1

    if smallerString in largerString:
        return True
    else:
        return False

def changeString(stringList):

    for i in range(len(stringList)):
        stringList[i] = removeCases(stringList[i])

