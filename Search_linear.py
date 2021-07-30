import random

#algo
def linear_search(list, el):
    for i in range(len(list)):
        if list[i] == el:
            return i

#some unnecessary stuff
list = []
k = random.randint(0, 10)
for i in range(10):
    j = random.randint(0, 50)
    list.append(j)
    if i == k:
        element = j

print('List: ', list)
print('Element: ', element)
print('Index of element is ', linear_search(list, element))
