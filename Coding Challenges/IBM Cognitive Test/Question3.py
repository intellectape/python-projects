def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


g1 = dict()

#g1 = dict()

first = ""
second = ""

def takeinput():
    inp = input()

    strList = inp.split(",")
    sd = []
    for string in strList:
        if '->' not in string:
            sd.append(string)
        else:
            string = string.split('->')
            if string[0] not in g1.keys():
                g1[string[0]] = set([string[1]])
                g1[string[1]] = set()
            else:
                g1[string[0]].add(string[1])
                if string[1] not in g1.keys():
                    g1[string[1]] = set()
    global first
    global second
    first = sd[0]
    second = sd[1]


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


def manager(first, second):
    root = findRoot()
    path_1 = list(dfs_paths(g1, root, first))
    path_2 = list(dfs_paths(g1, root, second))

    k_1 = [i for i in path_1[0]]
    k_2 = [i for i in path_2[0]]

    print(k_1)
    print(k_2)

    k = None
    if k_1 == None or k_2 == None:
        print("No path exists.")
    else:
        i = 0
        while (i < len(k_1) and i < len(k_2)):
            if k_1[i] != k_2[i]:
                break
            i += 1
        if len(k_1) < len(k_2) and k_1[-1] == k_2[len(k_1)-1]:
            k = k_1[-2]
        elif len(k_1) > len(k_2) and k_2[-1] == k_1[len(k_2)-1]:
            k = k_2[-2]
        else:
            k = k_1[i-1]

    print(k)

def main():
    takeinput()
    global g1
    global first
    global second

    manager(first, second)

if __name__=="__main__":
    main()