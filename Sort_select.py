def minimum(list, pos, n):
    min_pos = pos
    for i in range(pos, n):
        if list[i] < list[min_pos]:
            min_pos = i
    return min_pos

def select(list):
    n = len(list)
    
    for i in range(n-1):
        min = minimum(list, i, n)
        list[min], list[i] = list[i], list[min]

list = [6, 1, 19, 2, 6, 4, 15]
select(list)
print(list)
