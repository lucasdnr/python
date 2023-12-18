def play():
    version = "0.0.1"
    print("*********************************")
    print("Welcome to Hangman Game v{}!".format(version))
    print("*********************************")


# verifying if python is running or is running as a module
# we can create a hub of games so we can call this game as a module
if (__name__ == "__main__"):
    play()
