
import os


restaurants = [{'name': 'Happy Pizza', 'category': 'Pizza', 'active': False},
               {'name': 'Sushi Man', 'category': 'Sushi', 'active': True}]


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
    print('3. Update Status of Restaurant')
    print('4. Exit\n')


def exit_app():
    # clear console
    os.system('cls')
    # s.system('clear') for mac
    print('Exit')


def show_title(title):
    # clear console
    os.system('cls')
    # print specific message for this function
    line = '*' * (len(title) + 4)
    print(line)
    print(title)
    print(f'{line}\n')


def back_to_menu():
    input('\nPress any key to return to main menu ')
    main()


def invalid_option():
    print('Invalid Option!\n')
    back_to_menu()


def list_restaurants_handler():
    show_title('List of Restaurants')

    for restaurant in restaurants:
        name = restaurant['name']
        category = restaurant['category']
        active = 'Activated' if restaurant['active'] == True else 'Deactivated'

        print(f'- {name.ljust(20)} | {category.ljust(20)} | {active}')

    back_to_menu()


def new_restaurant_handler():
    show_title('New Restaurant')

    name = input('Enter the name of the restaurant you want to register: ')
    category = input(f'Enter the category name of the {name}: ')
    data = {'name': name, 'category': category, 'active': False}
    restaurants.append(data)
    print(f'The restaurant {name} was successfully created!')

    back_to_menu()


def update_status_restaurant_handler():
    restaurant_found = False

    show_title('Update Status of Restaurant')

    name = input(
        'Enter the name of the restaurant you want to change the status: ')

    for restaurant in restaurants:
        if name.upper() == restaurant['name'].upper():
            restaurant_found = True
            restaurant['active'] = not restaurant['active']
            message = f'Restaurant {name} has been successfully activated' if restaurant['active'] else f'Restaurant {
                name} has been successfully deactivated'
            print(message)

    if not restaurant_found:
        print('The restaurant was not found')

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
                update_status_restaurant_handler()
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
