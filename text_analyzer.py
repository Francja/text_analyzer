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


if __name__ == "__main__":
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
