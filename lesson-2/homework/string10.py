#this will print out the number of words in the sentence

sentence = input("Give me a sentence, and I will return the number of words it has: ")
without_spaces= sentence.replace(" ", "")

print(len(without_spaces))