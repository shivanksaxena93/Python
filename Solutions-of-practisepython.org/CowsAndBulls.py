import random
cow = 0
bull = 0
z = '0123456789'

x= "".join(random.sample(z,4))
y = input("Enter a 4 digit number \n")

if len(y) == 4:
    for i in range(len(x)):
        if x[i] == y[i]:
            cow += 1
        else:
            bull += 1
    if bull == 0:
        print("Game Over")
    else:
        print("You have {} cows and {} bulls".format(cow, bull))


    print("Computer selected {} number ".format(x))
else:
    print("Error You have not types 4 digit word")

