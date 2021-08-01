def prefix(image):
    # O(n)
    prefix = []
    i = 1
    prefix.append(0)
    
    while i != len(image):
        j = prefix[i-1]
        while j > 0 and image[i] != image[j]:
            j = prefix[j-1]
        if image[i] == image[j]:
            j += 1
        prefix.append(j)
        i += 1
    
    return prefix

def KMP(mas, image, p):
    # O(m)
    n = len(image)
    m = len(mas)
    k = l = 0
    
    while k != m:
        if mas[k] ==  image[l]:
            k += 1
            l += 1
            if l == n:
                return k-l
        elif l == 0:
            k += 1
            if k == m:
                return -1
        else:
            l = p[l-1]

im = 'abcabcd'
stroka = 'ABC ABCDAB abcabcd ABCDABCDABDE'
pi = prefix(im)
print(KMP(stroka, im, pi))
