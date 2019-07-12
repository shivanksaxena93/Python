def firstandlast(xyz):
    print([xyz[0],xyz[-1]])

firstandlast([int(x) for x in input("Enter a bunch of number \n").split()])


x = [int(x) for x in input("Enter a bunch of number \n").split()]

y = []
a = 0


for i in x:
    if a==0:
        y.append(x[a],x[len(x)-1])
        break
print(y)
