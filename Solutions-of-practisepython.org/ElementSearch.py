# Brute force
x = [int(i) for i in input("Enter few numbers").split()]
y = int(input("Enter any number"))

if y in x :
    print("{} number is there in list".format(y))

# Binary Search


import math
x = [int(i) for i in input("Enter few numbers \n").split()]
y = int(input("Enter any number \n"))

p = sorted(x)
z = math.ceil(len(p)/2)


pow = 0

cow = 0

print(z)
print(p)

if y > p[z-1]:
    for i in range(z-1,len(p)):
        if y == p[i]:
            pow += 1
            break
        else:
            pass
elif y <= p[z]:
    for j in range(z+1):
        if y == p[j]:
            cow += 1
            break
        else:
            pass
        break
if cow > 1 or pow > 1 :
    print("Present")
else:
    print("Not present")
