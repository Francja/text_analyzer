import requests

URL = "http://s3.zylowski.net/public/input/6.txt"
FILENAME = "file.txt"


def menu():
    print("1. Download file",
          "2. Count letters",
          "3. Count words",
          "4. Count punctuation marks",
          "5. Count sentences",
          "6. Generate report",
          "7. Save statistics to file",
          "8. Close the application",
          sep = "\n"
          )
    return input("Select option: ")


def download_file(url):
    r = requests.get(url)
    with open(FILENAME, 'w', encoding='utf8') as f:
        f.write(r.text)


def open_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File %s not found." % FILENAME)


def count_letters(text):
    num_letters = 0
    for char in text:
        if char.isalpha():
            num_letters +=1
    return num_letters


if __name__ == "__main__":
    #download_file(URL)
    while True:
        try:
            choice = int(menu())
            if choice<1 or choice>8:
                print("You typed incorrect number. Select option by typing 1-8.")
                continue
        except ValueError:
            print("You didn't type number. Select option by typing 1-8.")
            continue
        print("Selected option: %s" % choice)
        if choice == 1:
            download_file(URL)
            print("File downloaded.")
        elif choice == 2:
            letters = count_letters(open_file(FILENAME))
            print("Number of letters in the file: %i" % letters)
