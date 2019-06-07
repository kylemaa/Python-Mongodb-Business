from data.owners import Owner
import services.data_service as data_service


# Set the value of the owner's object to none or start
active_user_account: Owner = None


def reload_user_app():
    global active_user_account
    if not active_user_account:
        return

    active_user_account = data_service.find_account_by_email(active_user_account.email)
