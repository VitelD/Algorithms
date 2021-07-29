def quicksort(list, left, right):
    if left < right:
        p = partition(list, left, right)
        quicksort(list, left, p-1)
        quicksort(list, p+1, right)
        
    return list

def partition(list, left, right):
    p = list[right]
    i = left
    
    for j in range(left, right):
        if list[j] <= p:
            list[i], list[j] = list[j], list[i]
            i += 1
    list[i], list[right] = list[right], list[i]
    
    return i

list = [15, 6, 1, 2, 1, 9, 19, 7]
quicksort(list, 0, len(list)-1)
print(list)
