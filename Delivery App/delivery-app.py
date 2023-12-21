
import os

restaurants = ['Pizza', 'Sushi']


def print_welcome_message():
    # clear console
    os.system('cls')

    version = '0.1.0'
    print('*********************************')
    print(f'v{version}')
    print("""
██████╗░███████╗██╗░░░░░██╗██╗░░░██╗███████╗██████╗░██╗░░░██╗  ░█████╗░██████╗░██████╗░
██╔══██╗██╔════╝██║░░░░░██║██║░░░██║██╔════╝██╔══██╗╚██╗░██╔╝  ██╔══██╗██╔══██╗██╔══██╗
██║░░██║█████╗░░██║░░░░░██║╚██╗░██╔╝█████╗░░██████╔╝░╚████╔╝░  ███████║██████╔╝██████╔╝
██║░░██║██╔══╝░░██║░░░░░██║░╚████╔╝░██╔══╝░░██╔══██╗░░╚██╔╝░░  ██╔══██║██╔═══╝░██╔═══╝░
██████╔╝███████╗███████╗██║░░╚██╔╝░░███████╗██║░░██║░░░██║░░░  ██║░░██║██║░░░░░██║░░░░░
╚═════╝░╚══════╝╚══════╝╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░  ╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░""")
    print('*********************************')


def print_menu():
    print('1. New Restaurant')
    print('2. List Restaurants')
    print('3. Activate Restaurant')
    print('4. Exit')


def exit_app():
    # clear console
    os.system('cls')
    # s.system('clear') for mac
    print('Exit')


def show_title(title):
    # clear console
    os.system('cls')
    # print specific message for this function
    print(title)


def back_to_menu():
    input('\nPress any key to return to main menu ')
    main()


def invalid_option():
    print('Invalid Option!\n')
    back_to_menu()


def list_restaurants_handler():
    show_title('List Restaurants\n')

    for restaurant in restaurants:
        print(f'.{restaurant}')

    back_to_menu()


def new_restaurant_handler():
    show_title('New Restaurant\n')

    name = input('Enter the name of the restaurant you want to register: ')
    restaurants.append(name)
    print(f'The restaurant {name} was successfully created!')

    back_to_menu()


def choose_option():
    try:
        # select an option
        option_selected = int(input('Choose an option: '))
        match option_selected:
            case 1:
                # add new restaurant
                new_restaurant_handler()
            case 2:
                # return a list of restaurants
                list_restaurants_handler()
            case 3:
                # activate a restaurant
                print('Activate Restaurant')
            case 4:
                # exit app
                exit_app()
            case _:
                # invalid option
                invalid_option()
    except:
        invalid_option()


def main():
    # welcome message
    print_welcome_message()

    # print menu with options
    print_menu()

    # receive the input option from user and run the appropriate function of option
    choose_option()


# verifying if python is running or is running as a module
# we can create a hub of applications so we can call this app as a module
if (__name__ == '__main__'):
    main()
