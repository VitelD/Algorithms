def insert(list):
    left = 1
    right = len(list) 
    for i in range(left, right):
        j = i
        while (j !=0 ) and (list[j-1] > list[j]):
            list[j-1], list[j] = list[j], list[j-1]
            j -=1

list = [6, 1, 19, 2, 6, 4, 15]
insert(list)
print(list)
