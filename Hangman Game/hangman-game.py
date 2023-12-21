import random


def play():
    # print welcome message
    print_welcome_message()

    # get secret word from TXT file
    secret_word = load_secret_word()
    # load the structure that will show the letters list
    found_letters = load_found_letters(secret_word)

    # init variables
    hanged = False
    got_it = False
    error = 0

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
                len(secret_word)-error))

        hanged = error == len(secret_word)
        got_it = "_" not in found_letters
        print(found_letters)

    if (got_it):
        print("You win!")
    else:
        print(f"You lose! The word is {secret_word}")

    print("End")


def print_welcome_message():
    version = "0.0.1"
    print("*********************************")
    print(f"Welcome to Hangman Game v{version}!")
    print("*********************************")


def load_secret_word():
    # file handler - open words file
    # file = open("words.txt", "r")
    # file.close()
    words = []
    with open("words.txt") as file:
        for line in file:
            line = line.strip()
            words.append(line)

    # get a random word
    word_index = random.randrange(0, len(words))

    # set variables
    secret_word = words[word_index].upper()

    return secret_word


def load_found_letters(secret_word):
    return ["_" for letter in secret_word]


# verifying if python is running or is running as a module
# we can create a hub of games so we can call this game as a module
if (__name__ == "__main__"):
    play()
