a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


i = 0
j = 0

prev = 0

while i<len(a) and j<len(b):
    if a[i]==b[j]:
        if prev != a[i]:
            print(a[i])
            prev = a[i]
        i+=1
        j+=1
    elif a[i]<b[j]:
        i+=1
    elif a[i]>b[j]:
        j+=1
