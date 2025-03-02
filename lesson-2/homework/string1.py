#program that asks for name and year of birth, then returns with the age

name = str(input("What is your name? "))
year_of_birth = int(input("When were you born? "))

age = 2025 - year_of_birth

print(f"Your name is {name} and you are {age} years old.")