def find_factors(number):
    if number <= 0:
        print("Enter a positive integer.")
    
    for n in range(1, number + 1):
        if number % n == 0:
            print(f"{n} is a factor of {number}")

num = int(input("Enter a positive integer: "))
find_factors(num)