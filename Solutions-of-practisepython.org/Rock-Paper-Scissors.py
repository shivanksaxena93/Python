x = input("Input your value from ro, pa or sc \n")
y = ["ro", "pa", "sc"]

import random
z = random.choice(y)

if x == z:
    print("The computer played " + z)
    print("The match is draw")
elif x == "ro" and z == "sc":
    print("The computer played " + z)
    print("You won")
elif x == "sc" and z == "ro":
    print("The computer played " + z)
    print ("You Lost")
elif x == "sc" and z == "pa":
    print("The computer played " + z)
    print("You won")
elif x == "pa" and z == "sc":
    print("The computer played " + z)
    print("You Lost")
elif x == "pa" and z == "ro":
    print("The computer played " + z)
    print("You won")
elif x == "ro" and z == "pa":
    print("The computer played " + z)
    print("You Lost")
