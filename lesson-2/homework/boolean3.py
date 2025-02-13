#if negative or positive and if even

number = int(input("Enter a number: "))

# Check if the number is positive and even
if number > 0 and number % 2 == 0:
    print("The number is positive and yes it is even.")
else:
    print("The number is either not positive or no it is not even.")