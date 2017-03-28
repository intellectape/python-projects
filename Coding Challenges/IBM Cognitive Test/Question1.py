n = int(input())
p = int(input())
q = int(input())

p_str = str(p)
q_str = str(q)

def checkCondition_1(p, q, i): 
    return i % p == 0 and i % q != 0

def checkCondition_2(p_str, q_str, i_str):
    return (p_str in i_str) and not(q_str in i_str)

for i in range(1, n):
    i_str = str(i)

    if checkCondition_1(p, q, i) and checkCondition_2(p_str, q_str, i_str):
        print("WATSON")
    elif checkCondition_1(p, q, i):
        print("WAT")
    elif checkCondition_2(p_str, q_str, i_str):
        print("SON")
    else:
        print(i)
    if i < n:
        print(" ")




g1 = { "mary" : set(["Bob", "Sam"]),
    "Bob": set(["john"]),
    "Sam": set(["Pete", "Katie"]),
    "Pete": set(["bixie"]),
    "Katie": set(),
    "john": set(),
    "bixie": set()}