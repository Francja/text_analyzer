import os
import pathlib
import requests
import string
from collections import Counter

URL = "http://s3.zylowski.net/public/input/7.txt"
FILENAME = "file.txt"
STAT_FILENAME = "statystyki.txt"
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
          sep="\n")
    return input("Select option: ")


def download_file(url):
    r = requests.get(url)
    with open(FILENAME, 'w', encoding='utf8') as f:
        f.write(r.text)


def count_letters(text):
    num_letters = 0
    for char in text:
        if char.isalpha():
            num_letters += 1
    return num_letters


def count_words(text):
    num_words = sum([i.strip(string.punctuation).isalpha() for i in text.split()])  # list comprehension
    return num_words


def count_punctuation(text):
    num_punctuation = 0
    for char in text:
        if char in PUNCTUATION:
            num_punctuation += 1
    return num_punctuation


def get_report(text):
    for char in string.ascii_uppercase:
        counter = Counter(text.upper())
        print("%s: %i" % (char, counter[char]))


def count_sentences(text):
    return text.count('.')


def save_file(text):
    file = open("statystyki.txt", 'w+')
    file.writelines(text)
    file.close()


def remove_files():
    file_path = pathlib.Path(FILENAME)
    if file_path.exists():
        os.remove(file_path)
    stat_file_path = pathlib.Path(STAT_FILENAME)
    if stat_file_path.exists():
        os.remove(stat_file_path)


if __name__ == "__main__":
    while True:
        try:
            choice = int(menu())
            if choice < 1 or choice > 8:
                print("ERROR: You typed incorrect number. Select option by typing 1-8.")
                continue
        except ValueError:
            print("ERROR: You didn't type number. Select option by typing 1-8.")
            continue
        if choice == 1:
            download_file(URL)
            print("File downloaded.")
        elif 2 <= choice <= 7:
            try:
                with open(FILENAME, 'r') as file:
                    text_from_file = file.read()
            except FileNotFoundError:
                print("ERROR: File %s not found. Please download the file first." % FILENAME)
                continue
            if choice == 2:
                letters = count_letters(text_from_file)
                print("Number of letters in the file: %i" % letters)
            elif choice == 3:
                words = count_words(text_from_file)
                print("Number of words in the file: %i" % words)
            elif choice == 4:
                punctuations = count_punctuation(text_from_file)
                print("Number of punctuation marks in the file: %i" % punctuations)
            elif choice == 5:
                sentences = count_sentences(text_from_file)
                print("Number of sentences in the file: %s" % sentences)
            elif choice == 6:
                print("Number of occurrences of each letter in the text:")
                get_report(text_from_file)
            elif choice == 7:

                words = "Number of words in the file: %i \n" % count_words(text_from_file)
                letters = "Number of letters in the file: %i \n" % count_letters(text_from_file)
                punctuations = "Number of punctuations in the file: %i \n" % count_punctuation(text_from_file)
                sentences = "Number of sentences in the file: %i \n" % count_sentences(text_from_file)

                save_file([words, letters, punctuations, sentences])
                print("Saved FIle")
        elif choice == 8:
            remove_files()
            break
