#make acronyms

sentence = input("Enter a sentence: ")
words = sentence.split()

acronym = words[0][0].upper() + words[1][0].upper() + words[2][0].upper() + words[3][0].upper() + words[4][0].upper()

print("Shortened version:", acronym)