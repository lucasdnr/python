import random

version = "0.1.0"
print("*********************************")
print("Welcome to Gessing Game v{}!".format(version))
print("*********************************")

secret_number = random.randrange(1, 101)
print(secret_number)
points = 1000  # initial points of user

# asking for the difficulty to user, the difficulty define the number of attempts
# the user will have
print("What is the difficulty level?")
print("(1) Easy (2) Normal (3) Pro")

level = int(input("Set the level: "))

if (level == 1):
    total_attempts = 20
elif (level == 2):
    total_attempts = 10
else:
    total_attempts = 5

# the user has several attempts defined by the total_attempts variable
for attempt in range(1, total_attempts + 1):
    print("Attempt {} of {}".format(attempt, total_attempts))
    input_str = input("Enter your number between 1 and 100: ")
    print("Your number is: {}".format(input_str))
    # input returns a STRING, we need convert it to integer and compare to
    # SECRET_NUMBER bellow
    input_number = int(input_str)

    if (input_number < 1 or input_number > 100):
        print("You must enter a number between 1 and 100!")
        continue

    # treating all possibilities
    correct = secret_number == input_number
    greater = input_number > secret_number
    less = input_number < secret_number

    if (correct):
        # using string interpolation from python v3
        print(f"You got it! Total points {points}")
        break  # exit from loop
    else:
        if (greater):
            print("You failed! Your number is greater than the secret number")
        elif (less):
            print("You failed! Your number is less than the secret number")

        # for each failed attempt we will discount from initial points the number
        # of input_number
        # using Absolute number to convert negative numbers
        lost_points = abs(secret_number - input_number)
        points = points - lost_points

print("End")
