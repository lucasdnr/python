def play():
    version = "0.0.1"
    print("*********************************")
    print("Welcome to Hangman Game v{}!".format(version))
    print("*********************************")

    secret_word = "banana".upper()
    hanged = False
    got_it = False
    error = 0
    found_letters = ["_", "_", "_", "_", "_", "_"]

    # first print to show to user how many letters the secret_word have
    print(found_letters)

    while (not got_it and not hanged):
        guess = input("Choose a letter: ")
        # removing spaces from input
        guess = guess.strip().upper()

        if (guess in secret_word):
            index = 0
            # searching for character in the string
            for letter in secret_word:
                if (guess == letter):
                    found_letters[index] = letter
                    # print(f"I found the letter {letter} at position {index}")
                index += 1
        else:
            error += 1
            print("You missed! You have {} attempts more.".format(
                len(found_letters)-error))

        hanged = error == len(secret_word)
        got_it = "_" not in found_letters
        print(found_letters)

    if (got_it):
        print("You win!")
    else:
        print("You lose!")

    print("End")


# verifying if python is running or is running as a module
# we can create a hub of games so we can call this game as a module
if (__name__ == "__main__"):
    play()
