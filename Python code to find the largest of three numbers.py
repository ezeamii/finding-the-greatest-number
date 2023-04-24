# this pragram is to find the greatest amongst three numbers
num1 = float(input("What is the first number: "))
num2 = float(input("What is the second number: "))
num3 = float(input("What is the third number: "))

if num1 > num2 and num1 > num3:
    print(num1, "is the greatest number")
elif num2 > num1 and num2 > num3:
    print(num2, "is the greatest number")
elif num3 > num1 and num3 > num2:
    print(num3, "is the greatest number")
else:
    print("Please input three different numbers.")