x = [i for i in input("Enter a sentence \n").split()]
y = []


for a in range(len(x)):
   y.append(x[len(x)-a-1])

print(" ".join(y))

