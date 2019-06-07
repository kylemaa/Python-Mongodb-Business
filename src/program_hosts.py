import datetime
from colorama import Fore
from dateutil import parser
import services.data_service as data_service
import infrastructure.state as state
from infrastructure.switchlang import switch


def run():
    action = get_action()
    with switch(action) as obj:
        obj.case('C', create_account)
        obj.case('L', log_into_account)

        obj.case('V', view_your_order)
        obj.case('U', update_product_availability)
        obj.case('R', register_a_product)
        s.case('M', lambda: 'change_mode')

        s.case('?', show_commands)
        s.case('', lambda: None)
        s.case(['X', 'bye', 'exit', 'exit()', 'EXIT'], hosts.exit_app)

        s.default(unknown_command)


def get_action():
    # text let the customer/user know they're logged in
    action = input('put a letter ples:')
    return action


def create_account():
    name = input('Enter your full name: \n')
    email = input('Enter your email address: ')

    old_user_account = data_service.find_account_by_email(email)
    if old_user_account:
        error_msg('Failed. This email is already registered.')
        return

    state.active_user_account = data_service.create_account(name, email)
    success_msg('Successfully created an account')


def log_into_account():
    email = input('Enter your email address: ')
    account = data_service.find_account_by_email(email)
    if not account:
        error_msg('Failed. Cannot find this account in database')
        return

    state.active_user_account = account
    success_msg('Successfully logged into your account')


def view_your_orders():
    if not state.active_user_account:
        error_msg('You must login first to view your customers orders')
        return


def update_product_availability():
    if not state.active_user_account:
        error_msg('You must login first to update your products')
        return


def register_a_product():
    if not state.active_user_account:
        error_msg('You must login first to register your products')
        return


def success_msg(text):
    print(Fore.LIGHTGREEN_EX + text)


def error_msg(text):
    print(Fore.LIGHTRED_EX + text)