# Drinking age at the Pubs
print("Enter your age in years")
age = int(input())
balanceYears = 18 - age
expiredAge = age - 55
if age >= 18 and age <= 55:
    print("You are {} years of age,therefore you are permitted to enter and enjoy the drinks".format(age))
elif age < 18:
    print("You still have to {}  years to enjoy your first beer".format(balanceYears))
else:
    print("Drinking is not good for your health being as you have expired you years of enjoying drink by {} years".format(expiredAge))
age = age - 1
