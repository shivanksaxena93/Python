#Exceptional Handling using try and Catch

print("Please enter the lenth:")
length = int(input())
print("Please enter the width:")
width = int(input())
try:
    y = length / width
    print(y)
except ZeroDivisionError:
	print("Divison by zero is invalid! Kindly enter valid width.")
except NameError:
    print("There is a number missing. Kindly enter all the valid numbers")
except ValueError:
    print("Width not entered")
