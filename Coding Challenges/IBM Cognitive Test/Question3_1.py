
def bfs_paths(graph, start, goal):
    queue = [start]
    secondqueue = []
    while True:
        vertex = queue.pop(0)
        if len(graph[vertex]) != 0:
            for i in graph[vertex]:
                secondqueue.append(i)
            if goal not in secondqueue:
                newEl = secondqueue.pop(0)
                queue.append(newEl)
            else:
                if len(queue) == 0:
                    break
                else:
                    while queue:
                        ver = queue.pop(0)
                        for i in graph[ver]:
                            secondqueue.append(i)
                    break
    return secondqueue

g1 = dict()
first = ""

def takeinput2():
    inp = input()
    global first

    strList = inp.split(",")
    for string in strList:
        if '->' not in string:
            first = string
        else:
            string = string.split('->')
            if string[0] not in g1.keys():
                g1[string[0]] = set([string[1]])
                g1[string[1]] = set()
            else:
                g1[string[0]].add(string[1])
                if string[1] not in g1.keys():
                    g1[string[1]] = set()

def family(first):

    root = findRoot()
    path = bfs_paths(g1, root, first)
    return path


def findRoot():
    roots = []
    #finding the root
    for i in g1.keys():
        value = g1[i]
        if len(value) != 0:
            roots.append(i)
    root = ""
    allval = set()
    for j in g1.values():
        allval = allval | j

    root = list(set(roots) - allval)[0]
    return root

def main():
    takeinput2()
    global g1
    global first

    lst = family(first)
    printstr = ''
    for i in lst:
        if printstr == '':
            printstr += str(i)
        else:
            printstr = printstr + ',' + str(i)
    print(printstr)

if __name__=="__main__":
    main()