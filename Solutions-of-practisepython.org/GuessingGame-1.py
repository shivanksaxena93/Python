
import random
y = (random.randint(0,9))
x = int(input("Enter a number between 0 to 9 \n"))

if y == x:
    print("Exactly right answer")
elif abs(y - x) >= 3:
    print("Not close ")
elif abs(y - x) < 3:
    print("Too Close ")
print("Computer selected {} ".format(y))
