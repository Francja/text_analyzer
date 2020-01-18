import requests
import string
from collections import Counter

URL = "http://s3.zylowski.net/public/input/7.txt"
FILENAME = "file.txt"
PUNCTUATION = ".,!?:;()[]\"\'"


def menu():
    print("1. Download file",
          "2. Count letters",
          "3. Count words",
          "4. Count punctuation marks",
          "5. Count sentences",
          "6. Generate report",
          "7. Save statistics to file",
          "8. Close the application",
          sep="\n"
          )
    return input("Select option: ")


def download_file(url):
    r = requests.get(url)
    with open(FILENAME, 'w', encoding='utf8') as f:
        f.write(r.text)


def count_letters(text):
    num_letters = 0
    for char in text:
        if char.isalpha():
            num_letters +=1
    return num_letters


def count_words(text):
    num_words = sum([i.strip(string.punctuation).isalpha() for i in text.split()])  # list comprehension
    return num_words


def count_punctuation(text):
    num_punct = 0
    for x in text:
        if x in PUNCTUATION:
            num_punct += 1
    return num_punct


def get_report(text):
    for c in string.ascii_uppercase:
        counter = Counter(text.upper())
        print("%s: %i" % (c, counter[c]))


if __name__ == "__main__":
    while True:
        try:
            choice = int(menu())
            if choice<1 or choice>8:
                print("ERROR: You typed incorrect number. Select option by typing 1-8.")
                continue
        except ValueError:
            print("ERROR: You didn't type number. Select option by typing 1-8.")
            continue
        if choice == 1:
            download_file(URL)
            print("File downloaded.")
        elif 2 <= choice <= 6:
            try:
                with open(FILENAME, 'r') as file:
                    text = file.read()
            except FileNotFoundError:
                print("ERROR: File %s not found. Please download the file first." % FILENAME)
                continue
            if choice == 2:
                letters = count_letters(text)
                print("Number of letters in the file: %i" % letters)
            elif choice == 3:
                words = count_words(text)
                print("Number of words in the file: %i" % words)
            elif choice == 4:
                punctuations = count_punctuation(text)
                print("Number of punctuation marks in the file: %i" % punctuations)
            elif choice == 5:
                print("Selected option %s not yet implemented" % choice)  # TO DO, REPLACE AFTER IMPLEMENTATION
            elif choice == 6:
                print("Number of occurrences of each letter in the text:")
                get_report(text)
        elif choice == 7:
            print("Selected option %s not yet implemented" % choice)  # TO DO, REPLACE AFTER IMPLEMENTATION
        elif choice == 8:
            print("Selected option %s not yet implemented" % choice)  # TO DO, REPLACE AFTER IMPLEMENTATION
