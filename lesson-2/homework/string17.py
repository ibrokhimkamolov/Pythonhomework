#removing all vowels

string = input("Enter a sentence you want to remove all vowels from: ")
updated_string = string.replace('a', '*').replace('e', '*').replace('i', '*').replace('o', '*').replace('u', '*').replace('A', '*').replace('E', '*').replace('I', '*').replace('O', '*').replace('U', '*')

print(updated_string)