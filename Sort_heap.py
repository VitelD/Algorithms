import random

def heapsort(list):
    n = len(list)
    buildheap(list)
    H = []
    size = n
    
    while size >= 1:
        H.append(list[0])
        list[0], list[size-1] = list[size-1], list[0]
        list.pop()
        size -= 1
        heapify(list, 0, size)
    
    return H
    
def buildheap(list):
    n = len(list)
    par = (n-2) // 2

    while par >= 0:
        heapify(list, par, n)
        par -= 1
        
        
def heapify(list, i, size):
    left = 2*i+1
    right = 2*i+2
    
    if left < size and list[left] > list[i]:
        j = left
    else:
        j = i
        
    if right < size and list[right] >  list[j]:
        j = right
    
    if j != i:
        list[i], list[j] = list[j], list[i]
        heapify(list, j, size)

list = []
for i in range(9):
    k = random.randint(0, 15)
    list.append(k)
print(list)
H = heapsort(list)
print(H)
