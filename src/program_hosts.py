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

        obj.case('V', view_your_shipments)
        obj.case('U', update_product_availability)
        obj.case('R', register_a_product)
        obj.case('M', lambda: 'change_mode')

        obj.case('?', show_user_options)
        obj.case('', lambda: None)
        obj.case(['X', 'bye', 'exit', 'exit()', 'EXIT'], hosts.exit_app)

        s.default(unknown_command)


def show_user_options():
    print('Press the letter in [ ] to indicate your selection')
    print('[C] to Create new account')
    print('[L] to Log into existing account')
    print('[V] to View your order(s)')
    print('[M] to return to Main Menu')
    print('[X] to exit this app')
    print()


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


def view_your_shipments():
    if not state.active_user_account:
        error_msg('You must login first to view your customers orders')
        return
    shipments = data_service.find_orders_for_user(state.active_user_account)

    orders = [
        (s, o)
        for s in shipments
        for o in o.orders
        if o.ordered_date is not None
    ]

    print("You have {} orders.".format(len(orders)))



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