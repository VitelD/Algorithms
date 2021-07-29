def bubble(list):
    n = len(list)
    for i in range(n-1):
        for j in range(n-i-1):
            if list[j+1] < list[j]:
                list[j], list[j+1] = list[j+1], list[j]

list = [5,9,7,1,3,4,8]
bubble(list)
print(list)
