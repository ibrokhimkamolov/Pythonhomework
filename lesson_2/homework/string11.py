#check if a string contains any digits

txt = input("Enter your sentence that needs to be checked: ")

num1 = txt.count("1")
num2 = txt.count("2")
num3 = txt.count("3")
num4 = txt.count("4")
num5 = txt.count("5")
num6 = txt.count("6")
num7 = txt.count("7")
num8 = txt.count("8")
num9 = txt.count("9")
num0 = txt.count("0")

if num1 == 0 and num2 == 0 and num3 == 0 and num4 == 0 and num5 == 0 and num6 == 0 and num7 == 0 and num8 == 0 and num9 == 0 and num0 == 0:
    print("There are no digits in your sentence!")
else:
    print("There is a digit in your sentence!")