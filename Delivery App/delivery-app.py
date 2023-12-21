
def print_welcome_message():
    version = "0.1.0"
    print("*********************************")
    print(f"Delivery App v{version}")
    print("*********************************")

def print_menu()
    print("1. New Restaurant")
    print("2. List Restaurants")
    print("3. Activate Restaurant")
    print("4. Exit")

def run():
    # welcome message
    print_welcome_message()
    
    # print menu with options
    print_menu

    # select an option
    option_selected = input('Choose an option: ')
    print(f'You choose the option {option_selected}')


# verifying if python is running or is running as a module
# we can create a hub of applications so we can call this app as a module
if (__name__ == "__main__"):
    run()
