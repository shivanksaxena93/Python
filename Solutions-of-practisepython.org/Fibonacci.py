x = int(input("Enter the number to generate fibonnaci series \n" ))
y = [int(b)for b in input("Enter initial numbers \n").split()]

a = 2

if x == 0:
    print(y)

if x == 1 or x == 2:
    print(y)

if x > 2:
    y.append(y[len(y)-1] + y[len(y) - 2])
    print(y)
