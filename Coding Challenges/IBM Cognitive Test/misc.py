import re

string =  str(input())
stringList = string.split('|')

d = dict()

def removeCases(string):
    string = string.lower()
    string = re.sub( '\s+', ' ', string ).strip()
    string = string.replace("\"","")
    string = string.replace(",",".")
    string = re.sub('-+','-',string)

    return string

def changeString(string):
    li = list()
    for i in range(len(string)):
        li.append(removeCases(string[i]))
    return li

def compare():
    global stringList

    dummyList = changeString(stringList)

    for i in dummyList:
        if i not in d.keys():
            d[i] = list()
    
    for i in range(len(dummyList)):
        d[dummyList[i]].append(stringList[i])
    
    for i in (dummyList):
        for j in (dummyList):
            if i != j:
                if comparison(i, j):
                    if len(i) <= len(j):
                        stringSplit_1 = i.split()
                        stringSplit_2 = j.split()
                        print(stringSplit_1)
                        print(stringSplit_2)
                        if compareList(stringSplit_1, stringSplit_2):
                            if len(stringSplit_1) < len(stringSplit_2) :
                                k = dummyList.pop(dummyList.index(i))
                                print(k)
                            else:
                                k = dummyList.pop(dummyList.index(j))
                                print(k)
    if dummyList[0] == dummyList[1]:
        dummyList.pop(1)

    printList = []

    for i in dummyList:
        if i not in printList:
            printList.append(max(d[i], key=len))
    
    printstr = ""

    for i in printList:
        if printstr == '':
            printstr += str(i)
        else:
            printstr = printstr + '|' + str(i)
    print(printstr)

def compare2(string):
    global stringList

    dummyList = changeString(stringList)

    for i in dummyList:
        if i not in d.keys():
            d[i] = list()
    
    for i in range(len(dummyList)):
        d[dummyList[i]].append(stringList[i])
    
    for i in (dummyList):
        for j in (dummyList):
            if i != j:
                if comparison(i, j):
                    if len(i) <= len(j):
                        stringSplit_1 = i.split()
                        stringSplit_2 = j.split()
                        print(stringSplit_1)
                        print(stringSplit_2)
                        if compareList(stringSplit_1, stringSplit_2):
                            if len(stringSplit_1) < len(stringSplit_2) :
                                k = dummyList.pop(dummyList.index(i))
                                print(k)
                            else:
                                k = dummyList.pop(dummyList.index(j))
                                print(k)
    if dummyList[0] == dummyList[1]:
        dummyList.pop(1)

    printList = []

    for i in dummyList:
        if i not in printList:
            printList.append(max(d[i], key=len))
    
    printstr = ""

    for i in printList:
        if printstr == '':
            printstr += str(i)
        else:
            printstr = printstr + '|' + str(i)
    print(printstr)

def compareList(list1, list2):
    if list1 == list2:
        return True
    else:
        longList = list1 if len(list1) >= len(list2) else list2
        shortList = list1 if len(list1) <= len(list2) else list2
        maxLen = len(longList)
        minLen = len(shortList)
        for i in shortList:
            for j in longList:
                if i == j:
                    longList.pop(longList.index(j))
        
        if len(longList) == maxLen - minLen:
            return True
        else:
            return False

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