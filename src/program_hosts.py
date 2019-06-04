from src.infrastructure import state
from src.infrastructure import switchlang as switch


def run():
    action = get_action()
    with switch(action) as obj:
        obj.case('C', create_account)
        obj.case('L', log_into_account)


def get_action():
    # text let the customer/user know they're logged in
    text = '> '
    if state.active_account:
        text = f'{state.active_account.name}> '

    action = input(Fore.YELLOW + text + Fore.WHITE)
    return action


def create_account():


def log_into_account():