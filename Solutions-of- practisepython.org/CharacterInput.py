x = input("Enter your name \n")
y = int(input("Hello {}, Please enter your age \n".format(x)))
z = int(input("Enter a number to print copies \n"))

p = 0
while p < z:
    if y == 100:
        print("Congrats you already turned 100")
        p += 1
    elif y < 100:
        print("You will turn 100 in {} years".format(100-y))
        p += 1
    else:
        print("You crossed 100 by {} years".format(y - 100))
        p += 1
