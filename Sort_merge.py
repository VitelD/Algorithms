# my favorite sort algorithm
def merge(list):
    if len(list) <= 1:
        return list[:]
    
    mid = len(list) // 2
    L, R = list[:mid], list[mid:]
    L = merge(L)
    R = merge(R)
    return mergesort(L, R)
    
def mergesort(L, R):   
    i = j = 0
    C = []
    while (i < len(L)) and (j < len(R)):
        if L[i] <= R[j]:
            C.append(L[i])
            i += 1
        else:
            C.append(R[j])
            j += 1

    while i < len(L):
        C.append(L[i])
        i += 1
    while j < len(R):
        C.append(R[j])
        j += 1
    
    return C

list = [15, 6, 1, 2, 1, 9, 19, 7]
a = merge(list)
print(a)
