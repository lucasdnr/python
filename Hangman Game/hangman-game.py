def play():
    version = "0.0.1"
    print("*********************************")
    print("Welcome to Hangman Game v{}!".format(version))
    print("*********************************")

    secret_word = "banana"
    hanged = False
    got_it = False

    while (not got_it and not hanged):
        guess = input("Choose a letter: ")

        index = 0
        for letter in secret_word:
            if (guess == letter):
                print(f"I found the letter {letter} at position {index}")
            index = index + 1

    print("End")

# verifying if python is running or is running as a module
# we can create a hub of games so we can call this game as a module
if (__name__ == "__main__"):
    play()
