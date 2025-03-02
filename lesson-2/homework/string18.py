#first and last word

string = str(input("Enter your words: "))
first_word = string.split(' ')[0]
last_word = string.split(' ')[-1]

print(first_word)
print(last_word)