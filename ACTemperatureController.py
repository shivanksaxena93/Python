# AC Temperature Controller using while
print("Enter the temperature")
temperature = int(input())
while temperature >= 68 and temperature <= 77:
    print("The temperature is being maintained at {} degree Fahrenheit".format(temperature))
    temperature = temperature - 1
