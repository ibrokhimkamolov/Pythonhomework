#check if one string contains another

main_string = input("Enter the main string here: ")
inside_string = input("Enter the inside string, to check if it is there: ")

if inside_string in main_string:
    print("There is another string inside!!!!!")
else:
    print("There is not another string inside!!!!")