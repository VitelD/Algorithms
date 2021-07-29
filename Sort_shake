def shake(list):
    n = len(list)
    left = 0
    right = n - 1
    while left <= right:
        for i in range(right, left, -1):
            if list[i-1] > list[i]:
                list[i-1], list[i] = list[i], list[i-1]
        left += 1
        
        for i in range(left, right):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
        right -= 1

list = [5,9,7,1,3,4,8]
shake(list)
print(list)
