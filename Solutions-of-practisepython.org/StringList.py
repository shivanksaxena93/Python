x = input("Enter any word \n").lower()
i = 0
flag = True

while i < len(x):
    if x[i] == x[len(x)-1-i]:
        i += 1
    else:
        flag = False
        break
if flag == True:
    print("The word is pallindrome")
else:
    print("The word is a not a pallindrome")

