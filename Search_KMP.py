def prefix(image):
    # O(n)
    prefix = []
    i = 0
    j = 1
    prefix.append(0)
    
    while i != len(image)-1:
        if image[i] == image[j]:
            prefix.append(j+1)
            i += 1
            j += 1
        elif (j == 0):
            prefix.append(0)
            i += 1
        else:
            j = prefix[j-1]
    
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

            
im = 'ABCDABD'
stroka = 'ABC ABCDAB ABCDABCDABDE'
pi = prefix(im)
print(KMP(stroka, im, pi))

        
    
