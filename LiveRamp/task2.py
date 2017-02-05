# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

indexOfMin  = 0
indexOfMax = 0

def solution(A):
    # write your code in Python 2.7
    
    i = 0
    j = len(A)
    global indexOfMin
    global indexOfMax
    
    # Updating Index of First Value which is more than the non-decreasing order value.
    for i in range(len(A)):
        if A[i] > A[i + 1]:
            indexOfMin = i
            break

    # Updating Index of First Value which is more than the decreasing order value.
    for j in range(len(A) - 1, -1, -1):
        if A[j] < A[j - 1]:
            indexOfMax = j
            break

    # Code for 
    if not A[indexOfMin:indexOfMax]:
        minimum = A[indexOfMin]
        maximum = A[indexOfMax]
    else:
        minimum = min(A[indexOfMin:indexOfMax])
        maximum = max(A[indexOfMin:indexOfMax])
    
    
    for i in range(0, indexOfMin):
        if A[i] > minimum:
            indexOfMin = i
            break
        
    
    for j in range(len(A)-1, indexOfMax, -1):
        if A[j] < maximum:
            indexOfMax = j
            break
        
        
    print indexOfMax
    print indexOfMin
    return (indexOfMax - indexOfMin + 1)

