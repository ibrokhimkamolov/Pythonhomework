#polindrome check

word = input("Write a word to check if it is polndrome or not: ")

if word == word[::-1]:
    print(f"Your word {word} is polindrome")
else:
    print("Your word is not polidrome")