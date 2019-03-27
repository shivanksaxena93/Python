# Checking the number which is maximum


print('Please enter the first number')
x = int(input())
print('Please enter the second number')
y = int(input())
def maxNum(x, y):
    if x > y:
        print("The number {} which is the first number is greater".format(x))
    elif x < y:
        print("The number {} which is the second number is greater".format(y))
    else:
        print("Both the numbers are equal")
maxNum(x, y)
