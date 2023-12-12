version = "0.0.2"
print("*********************************")
print("Welcome to Gessing Game v{}!".format(version))
print("*********************************")

secret_number = 42

input_str = input("Enter your number: ")
print("Your number is: {}".format(input_str))
# input returns a STRING, we need convert it to integer and compare to 
# SECRET_NUMBER bellow 
input_number = int(input_str)

correct = secret_number == input_number
greater = input_number > secret_number
less = input_number < secret_number

if (correct):
    print("You got it!")
else:
    if(greater):
        print("You failed! Your number is greater than the secret number")
    elif(less):
        print("You failed! Your number is less than the secret number")

print("End")