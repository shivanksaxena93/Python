#Check if a number is a multiple of 3. If it is, also check if it a multiple of 7.
print ("Enter a number")
number = int(input())
if number % 3 == 0:
    print('The number is divisibe by 3.')
    if number % 7 == 0:
        print ('The number is also a multiple of 7')
    else:
        print ('The number is a multiple of 3 but not 7')
