from heapsort import *

def bin(list, el):
    '''
    n = len(list)
    mid = n // 2
    if el > mid:
        res = bin(list[:mid-1], el)
    elif el < mid:
        res = bin(list[mid+1:], el)
    else:
        res = mid
    '''
    left = 0
    right = len(list) - 1
    mid = 0
    
    while left <= right:
        mid = (right+left) // 2
        
        if el == list[mid]:
            return mid
        
        if el > list[mid]:
            right = mid-1
            
        elif el < list[mid]:
            left = mid+1
        

# some unnecessary stuff
list = []
k = random.randint(0, 9)
for i in range(10):
    j = random.randint(0, 50)
    list.append(j)
    if i == k:
        element = j

print('List: ', list)
print('Element: ', element)

# apply only if array is already sorted
H = heapsort(list)
# now we have an array in non-increasing order
print('Sorted list is ', H)
print('Index of element in sorted list is ', bin(H, element))
