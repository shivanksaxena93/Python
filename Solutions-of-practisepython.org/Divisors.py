x = int(input("Enter a number to check its divisors \n"))
y = []
i = 2
while i*i <= x:
    if x%i == 0:
        y.append(i)
        y.append(x//i)
    i +=1


if len(y)>0:
    print(y)
else:
    print("No factors found")


