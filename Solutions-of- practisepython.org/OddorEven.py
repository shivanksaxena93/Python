# With Extras

x = int(input("Enter a number to check if its odd or even \n"))
if x != 0:
    if x % 2 == 0:
        if x % 4 ==0:
            print("The number {} is even and multiple of 4".format(x))
        else:
            print("The number {} is even".format(x))
    else:
        print("The number {} is odd".format(x))
else:
    print("0 is neither odd nor even")
