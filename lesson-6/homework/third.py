import os
import string
from collections import Counter

def create_sample_file():
    print("sample.txt not found. Please enter a paragraph to create the file:")
    text = input("Enter text: ")
    with open("sample.txt", "w", encoding="utf-8") as file:
        file.write(text)
    print("File created successfully!\n")

def count_word_frequency():
    if not os.path.exists("sample.txt"):
        create_sample_file()
    
    while True:
        try:
            top_n = int(input("Enter the number of top common words to display: "))
            if top_n <= 0:
                raise ValueError("Please enter a positive integer.")
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    
    word_count = Counter()
    total_words = 0
    
    with open("sample.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.lower().translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
            words = line.split()
            word_count.update(words)
            total_words += len(words)
    
    top_words = word_count.most_common(top_n)
    
    print(f"Total words: {total_words}")
    print(f"Top {top_n} most common words:")
    for word, count in top_words:
        times_label = "time" if count == 1 else "times"
        print(f"{word} - {count} {times_label}")
    
    with open("word_count_report.txt", "w", encoding="utf-8") as report:
        report.write("Word Count Report\n")
        report.write(f"Total Words: {total_words}\n")
        report.write(f"Top {top_n} Words:\n")
        for word, count in top_words:
            report.write(f"{word} - {count}\n")
    
    print("\nReport saved to word_count_report.txt")

def main():
    count_word_frequency()

if __name__ == "__main__":
    main()
