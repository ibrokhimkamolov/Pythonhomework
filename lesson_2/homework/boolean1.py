#empty or not

username = input("Enter your username: ")
password = input("Enter your password: ")

print(f"If it says False then you didn't enter your username, if it says True, then you did =====> {bool(username)}")
print(f"If it says False then you didn't enter your password, if it says True, then you did =====> {bool(password)}")

print("-"*50)

if username == "":
    print("You did not enter your username!")
else:
    print("Thank you for entering your username!")

if password == "":
    print("You did not enter your password!")
else:
    print("Thank you for entering your password!")
