Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # variableName = value
>>> totalMarks = 95
>>> print(totalMarks)
95

>>> totalMarks = 100
>>> print(totalMarks)
100

>>> integerNumber = 10
>>> floatingNumber = 20.75
>>> print(floatingNumber)
20.75

>>> print(integerNumber)
10

>>> print(type(floatingNumber))
<class 'float'>

>>> floatingNumber = int(floatingNumber)
>>> print(type(floatingNumber))
<class 'int'>
>>> print(floatingNumber)
20
>>> string = 'I love python\'s book'
>>> print (string)
I love python's book
>>> string = "I love python's book"
>>> print(string)
I love python's book
>>> string.upper()
"I LOVE PYTHON'S BOOK"
>>> print(string)
I love python's book
>>> string.lower(string)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    string.lower(string)
TypeError: lower() takes no arguments (1 given)
>>> string.lower()
"i love python's book"
>>> string.replace("love","like")
"I like python's book"
>>> string[5]
'e'
>>> string[0:12]
'I love pytho'
>>> len(string)
20
>>> print("{}as it contains a lot of details about the programming language".format(string))
I love python's bookas it contains a lot of details about the programming language
>>> 10/5
2.0
>>> 10//5
2
>>> favouriteFruits =  ['Apple', 'Mango', 'Strawberry', 'Papaya']
>>> favouriteFruits
['Apple', 'Mango', 'Strawberry', 'Papaya']
>>> favouriteFruits[0]
'Apple'
>>> favouriteFruits[2]
'Strawberry'
>>> favouriteFruits[1] = 'Orange'
>>> favouriteFruits
['Apple', 'Orange', 'Strawberry', 'Papaya']
>>> # list.append
>>> # list.append()
>>> favouriteFruits.append('kiwi')
>>> favouriteFruits
['Apple', 'Orange', 'Strawberry', 'Papaya', 'kiwi']
>>> # list.insert()
>>> favouriteFruits.insert(1,'Mango')
>>> favouriteFruits
['Apple', 'Mango', 'Orange', 'Strawberry', 'Papaya', 'kiwi']
>>> #list.remove
>>> favouriteFruits.remove('straberry')
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    favouriteFruits.remove('straberry')
ValueError: list.remove(x): x not in list
>>> favouriteFruits.remove('strawberry')
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    favouriteFruits.remove('strawberry')
ValueError: list.remove(x): x not in list
>>> favouriteFruits
['Apple', 'Mango', 'Orange', 'Strawberry', 'Papaya', 'kiwi']
>>> favouriteFruits.remove('Strawberry')
>>> favouriteFruits
['Apple', 'Mango', 'Orange', 'Papaya', 'kiwi']
>>> # list.sort
>>> favouriteFruits.sort()
>>> favouriteFruits
['Apple', 'Mango', 'Orange', 'Papaya', 'kiwi']
>>> favouriteFruits.insert('Banana')
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    favouriteFruits.insert('Banana')
TypeError: insert() takes exactly 2 arguments (1 given)
>>> favouriteFruits.insert(5, 'Banana')
>>> favouriteFruits
['Apple', 'Mango', 'Orange', 'Papaya', 'kiwi', 'Banana']
>>> # list.reverse()
>>> favouriteFruits.reverse()
>>> favouriteFruits
['Banana', 'kiwi', 'Papaya', 'Orange', 'Mango', 'Apple']
>>> favouriteFruits
['Banana', 'kiwi', 'Papaya', 'Orange', 'Mango', 'Apple']
>>> favouriteFruits()sort
SyntaxError: invalid syntax
>>> favouriteFruits.sort()
>>> fav
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    fav
NameError: name 'fav' is not defined
>>> favouriteFruits
['Apple', 'Banana', 'Mango', 'Orange', 'Papaya', 'kiwi']
>>> favouriteFruits.reverse()
>>> favouriteFruits
['kiwi', 'Papaya', 'Orange', 'Mango', 'Banana', 'Apple']
>>> favouriteFruits.pop()
'Apple'
>>> favouriteFruits
['kiwi', 'Papaya', 'Orange', 'Mango', 'Banana']
>>> #tupleName = (object1, object 2, object3, object4)
>>> # tuple to store dates of world war 1 and world war 2
>>> historicWarDates = (1914, 1939)
>>> historicWarDates
(1914, 1939)
>>> historicWarDates[1] = 2017
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    historicWarDates[1] = 2017
TypeError: 'tuple' object does not support item assignment
>>> del(historicWarDates)
>>> historicWarDates
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    historicWarDates
NameError: name 'historicWarDates' is not defined
>>> # dictionaryName = {key1: value1, key2: value2}
>>> priceOfCamers = {"sony": 500, "nikon": 600,"canon": 700}
>>> priceOfCamers
{'sony': 500, 'nikon': 600, 'canon': 700}
>>> priceOfCamers["sony"]
500
>>> priceOfCamers['nikon'] = 800
>>> priceOfCamers
{'sony': 500, 'nikon': 800, 'canon': 700}
>>> priceOfCamers['nikon']
800
>>> priceOfCamers[800]
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    priceOfCamers[800]
KeyError: 800
>>> priceOfCamers.keys()
dict_keys(['sony', 'nikon', 'canon'])
>>> priceOfCamers.values
<built-in method values of dict object at 0x000001FF3062E168>
>>> priceOfCamers.values()
dict_values([500, 800, 700])
>>> copyOfPriceOfCamers = priceOfCamers.copy()
>>> copyOfPriceOfCamers
{'sony': 500, 'nikon': 800, 'canon': 700}
>>> #deleting a key value pair
>>> del priceOfCamers['sony']
>>> priceOfCamers
{'nikon': 800, 'canon': 700}
>>> # clearing the values of the dictionary
>>> priceOfCamers.clear
<built-in method clear of dict object at 0x000001FF3062E168>
>>> priceOfCamers.clear()
>>> priceOfCamers
{}
>>> # if-condition
>>> totalMarks
100
>>> totalMarks = 95
>>> totalMarks
95
>>> if totalMarks >=90:
	print('Congratulations you have secured an A grade')

	
Congratulations you have secured an A grade
>>> totalMarks
95
>>> if totalMarks >= 100:
	print('Congratulations you are a merit holder')

	
>>> # if- else condition
>>> if totalMarks >=96:
	print('Congratulation you have cleared the examination')
else:
	print('Thank you fro your time and better luck next time')

	
Thank you fro your time and better luck next time
>>> if-elif condition
SyntaxError: invalid syntax
>>> #if-elif condition
>>> totalMarks = 60
>>> if totalMarks >=90:
	print('congratulations you have scored an A grade')
elif totalMarks >= 40:
	print('congratulations you have cleared the exam')
else:
	print('Sorry you have failed the examination')

	
congratulations you have cleared the exam
>>> # nested-if condition
>>> totalMarks = 100
>>> if totalMarks >=90:
	print('congratulation you have score an A grade')
	if totalMarks == 100:
		print('You are also a merit holder')

		
congratulation you have score an A grade
You are also a merit holder
>>> totalMarks
100
>>> totalMarks = 95
>>> percentageOfAttendance = 93
>>> if totalMarks >= 90 and percentageOfAttendance >= 80
SyntaxError: invalid syntax
>>> if totalMarks >= 90 and percentageOfAttendance >=80:
	print('You are a very discplined student')

	
You are a very discplined student
>>> # or
>>> if totalMarks >=90 or attendance >=95:
	print('You have been passed')

	
You have been passed
Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> totalMarks = 95
>>> percentageOfAttendance = 93
>>> if totalMarks >=40 and percentageOfAttendance >= 70:
	print('You are qualified for the examination')
elif totalMarks >= 40 or percentageOfAttendance >= 70:
	print('You lack one criteria for qualification. Kindly contact you department')
else:
	print('Sorry you are not allowed to appear for the examination')

	
You are qualified for the examination
>>> totalMarks = 35
>>> if totalMarks >=40 and percentageOfAttendance >= 70:
	print('You are qualified for the examination')
elif totalMarks >= 40 or percentageOfAttendance >= 70:
	print('You lack one criteria for qualification. Kindly contact you department')
else:
	print('Sorry you are not allowed to appear for the examination')


You lack one criteria for qualification. Kindly contact you department
>>> percentageOfAttendance = 55
>>> if totalMarks >=40 and percentageOfAttendance >= 70:
	print('You are qualified for the examination')
elif totalMarks >= 40 or percentageOfAttendance >= 70:
	print('You lack one criteria for qualification. Kindly contact you department')
else:
	print('Sorry you are not allowed to appear for the examination')


Sorry you are not allowed to appear for the examination
>>> totalMarks = 55
>>> if totalMarks >=40 and percentageOfAttendance >= 70:
	print('You are qualified for the examination')
elif totalMarks >= 40 or percentageOfAttendance >= 70:
	print('You lack one criteria for qualification. Kindly contact you department')
else:
	print('Sorry you are not allowed to appear for the examination')


You lack one criteria for qualification. Kindly contact you department
>>> number = 27
>>> number
27
>>> if number % 3 = 0:
    print('The number is divisibe by 3. Checking for divisibility by 7')
elif number % 7 = 0:
    print ('The number is multiple of 3 and 7.')
else:
    print ('The number are not multiple of 3 and 7')
    
SyntaxError: invalid syntax
>>> if number % 3 == 0:
    print('The number is divisibe by 3. Checking for divisibility by 7')
elif number % 7 == 0:
    print ('The number is multiple of 3 and 7.')
else:
    print ('The number are not multiple of 3 and 7')

    
The number is divisibe by 3. Checking for divisibility by 7
>>> 
>>> 
>>> 
>>> number = 21
>>> if number % 3 == 0:
    print('The number is divisibe by 3. Checking for divisibility by 7')
elif number % 7 == 0:
    print ('The number is multiple of 3 and 7.')
else:
    print ('The number are not multiple of 3 and 7')

    
The number is divisibe by 3. Checking for divisibility by 7
>>> if number % 3 == 0 and number % 7 == 0
SyntaxError: invalid syntax
>>> if number % 3 == 0 and number % 7 == 0:
	print ("The number is multiple of 3 and 7")
else:
	print ("The number is not a multiple of 3 and 7")

	
The number is multiple of 3 and 7
>>> number = 27
>>> if number % 3 == 0 and number % 7 == 0:
	print ("The number is multiple of 3 and 7")
else:
	print ("The number is not a multiple of 3 and 7")

	
The number is not a multiple of 3 and 7
>>> number
27
>>> if number % 3 == 0:
    print('The number is divisibe by 3. Checking for divisibility by 7')
    if number % 7 == 0:
        print ('The number is multiple of 3 and 7.')
    else:
        print ('The number are not multiple of 3 and 7')

        
The number is divisibe by 3. Checking for divisibility by 7
The number are not multiple of 3 and 7
>>> if number % 3 == 0:
    print('The number is divisibe by 3. Checking for divisibility by 7')
    if number % 7 == 0:
        print ('The number is multiple of 3 and 7.')
    else:
        print ('The number is a multiple of 3 but not 7')

        
The number is divisibe by 3. Checking for divisibility by 7
The number is a multiple of 3 but not 7
>>> number = 21
>>> if number % 3 == 0:
    print('The number is divisibe by 3. Checking for divisibility by 7')
    if number % 7 == 0:
        print ('The number is multiple of 3 and 7.')
    else:
        print ('The number is a multiple of 3 but not 7')

        
The number is divisibe by 3. Checking for divisibility by 7
The number is multiple of 3 and 7.
>>> print ("Enter a number")
Enter a number
>>> number = input()
5
>>> 
>>> number
'5'
>>> # For loop
>>> For variablename in sequence name
SyntaxError: invalid syntax
>>> #For variablename in sequence name
>>> # For variablename in sequence name
>>> fruits = ["Apple","Mango","Banana","Strawberry"]
>>> for fruit in fruits:
	print(fruit)

	
Apple
Mango
Banana
Strawberry
>>> # Range
>>> for alphabets in range(A, Z):
	print(alphabets)

	
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    for alphabets in range(A, Z):
NameError: name 'A' is not defined
>>> for numbers in ranger(1,6):
	print(numbers)

	
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    for numbers in ranger(1,6):
NameError: name 'ranger' is not defined
>>> for numbers in range(1, 6):
	print (numbers)

	
1
2
3
4
5
>>> # Functioning of an AC using while loop
>>> temperature = input()
50
>>> while temperature >=40 and temperature =<60:
	
SyntaxError: invalid syntax
>>> while temperature >=40 and temperature <= 60:
	print("Room temperature is being maintained at {} degree fahrenhiet".format(temperature))
	temperature = temperature-1

	
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    while temperature >=40 and temperature <= 60:
TypeError: '>=' not supported between instances of 'str' and 'int'
>>> # An infinite loop
>>> while True:
	print("This Loop runs forever")

	
This Loop runs forever





# Area of the Rectangle
>>> lengthOne = 8
>>> widthOne  = 3
>>> areaOne = lengthOne*widthOne
>>> areaOne
24
>>> lenthTwo = 10
>>> widthTwo = 4
>>> areaTwo = lenthTwo*widthTwo
>>> areaTwo
40


>>> # Using a function
def computeArea(length, width):
	area = length * width
	print(area)

>>> computeArea(lengthOne, widthOne)
24
>>> computeArea(lenthTwo,widthTwo)
40
>>> 

length = 8
>>> width = 0
>>> length/width
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    length/width
ZeroDivisionError: division by zero

>>>try:
	length = 10
	width = 0
	length/width
except Exception:
	print("Divison by zero is invalid! Kindly enter valid width.")

	      
Divison by zero is invalid! Kindly enter valid width.

>>> del(width)
	      
>>> width
	      
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    width
NameError: name 'width' is not defined
>>> try:
	length = 10
	width = 0
	length/width
except ZeroDivisionError:
	print("Divison by zero is invalid! Kindly enter valid width.")
except NameError:
	      print("There is a number missing. Kindly enter all the valid numbers")

	      
Divison by zero is invalid! Kindly enter valid width.
>>> 
