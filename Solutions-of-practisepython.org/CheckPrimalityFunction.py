x = int(input("Enter any number \n"))
flag = True
for i in range(2,x):
    if x % i == 0:
        flag = False

if flag == True:
    print("The number is prime")
else:
    print("The number is not prime")

