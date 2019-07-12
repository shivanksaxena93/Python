# a = [1,1,2,3,5,8,13,21,34,55,89]

d = []
for i in a:
    if i < 5:
        d.append(i)

print(d)

# Extras
a = [1,1,2,3,5,8,13,21,34,55,89]

print ([i for i in a if i < 5])

x = int(input("Enter a number \n"))

a = [1,1,2,3,5,8,13,21,34,55,89]

b = [i for i in a if i < x]
print (b)
