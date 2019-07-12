y = [5,7,9,10,5,6,3,7,2,64,6,2,3,5,7,9]
z = []
a=0

for x in y:
    if y[a] not in z:
        z.append(y[a])
    a +=1
print(z)

