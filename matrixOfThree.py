# To create a incrementing Matrix
# 1 2 3
# 4 5 6
# 7 8 9

number = 1
for row in range (1,4):
  for column in range (1,4):
    print(number, end = " ")
    number = number + 1
  print()
