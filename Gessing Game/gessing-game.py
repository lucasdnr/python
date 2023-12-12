version = "0.0.1"
print("*********************************")
print("Welcome to Gessing Game v{}!".format(version))
print("*********************************")

secret_number = 42

input_str = input("Enter your number: ")
print("Your number is: {}".format(input_str))
# input returns a STRING, we need convert it to integer and compare to 
# SECRET_NUMBER bellow 
input_number = int(input_str)

if (secret_number == input_number):
    print("You got it!")
else:
    print("You failed!")

print("End")