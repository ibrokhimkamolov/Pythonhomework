#checks if the number is more than 50.8

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 + num2 > 50.8:
    print("The sum of num1 and num2 is greater than 50.8.")
else:
    print("The sum of num1 and num2 is not greater than 50.8.")

print("-"*50)

if 10 <= num1 <= 20:
    print("The num1 is between 10 and 20.")
else:
    print("The num1 is not between 10 and 20.")

print("-"*50)

if 10 <= num2 <= 20:
    print("The num2 is between 10 and 20.")
else:
    print("The num2 is not between 10 and 20.")