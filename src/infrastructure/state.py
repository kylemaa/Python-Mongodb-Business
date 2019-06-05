from data.owner import Owner
import services.data_service as data_service


# Set the value of the owner's object to none or start
active_app_user: Owner = None


def reload_user_app():
    global active_app_user
    if not active_app_user:
        return
    else:
        active_app_user = data_service.find_account_by_email(active_app_user.email)
