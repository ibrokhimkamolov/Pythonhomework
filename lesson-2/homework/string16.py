#removing all occurances of that character

your_sentence = input("Enter your sentence: ")
character_to_remove = input("Enter the character you want to remove from your sentence: ")

removing = your_sentence.replace(character_to_remove, "")

print(removing)