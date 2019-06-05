import datetime
from colorama import Fore
from dateutil import parser

from infrastructure import state
from infrastructure.switchlang import switch


def run():
    action = get_action()
    with switch(action) as obj:
        obj.case('C', create_account)

''' obj.case('L', log_into_account)

        obj.case('V', view_your_order)
        obj.case('U', update_product_availability)
        obj.case('R', register_a_product)
        s.case('m', lambda: 'change_mode')

        s.case('?', show_commands)
        s.case('', lambda: None)
        s.case(['x', 'bye', 'exit', 'exit()'], hosts.exit_app)

        s.default(unknown_command)

    state.reload_user_app()'''


def get_action():
    # text let the customer/user know they're logged in
    action = input('put a letter ples:')
    return action


def create_account():
    name = input('Enter your full name: \n')
    email = input('Enter your email address: ')
    error_msg('Successfully created an account')

# def log_into_account():


# def view_orders():


# def update_product_availability():


# def register_a_product():


def success_msg(text):
        print(Fore.LIGHTGREEN_EX + text)


def error_msg(text):
        print(Fore.LIGHTRED_EX + text)